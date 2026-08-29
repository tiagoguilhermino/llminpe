import argparse
import csv
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
import traceback

from dotenv import load_dotenv

from rag_engine import RagOptions, add_documents, build_or_load_vectors, rebuild_index, answer_question

load_dotenv()

CONFIGURATIONS = {
    "Baseline (FAISS)": RagOptions(False, False, False, False),
    "HyDE": RagOptions(True, False, False, False),
    "Multi-Query": RagOptions(False, True, False, False),
    "Reranking": RagOptions(False, False, True, False),
    "Knowledge Graph": RagOptions(False, False, False, True),
    "HyDE + Reranking": RagOptions(True, False, True, False),
    "MQ + Reranking": RagOptions(False, True, True, False),
    "Todas as técnicas": RagOptions(True, True, True, True),
}


def load_dataset(path: Path, limit: int | None) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"Dataset nao encontrado: {path}")
    required = {"chunk", "resposta", "pergunta"}
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError(f"CSV deve conter as colunas: {sorted(required)}")
        rows = []
        for row in reader:
            values = {key: (row.get(key) or "").strip() for key in required}
            if all(values.values()):
                rows.append(values)
            if limit and len(rows) >= limit:
                break
    return rows


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower().strip())


def chunk_matches(expected: str, retrieved: str, minimum: int = 60) -> bool:
    expected, retrieved = normalize(expected), normalize(retrieved)
    if not expected or not retrieved:
        return False
    prefix = expected[: min(150, len(expected))]
    if len(prefix) >= minimum and prefix in retrieved:
        return True
    maximum = min(len(expected), len(retrieved), 150)
    for size in range(maximum, minimum - 1, -1):
        for start in range(maximum - size + 1):
            if expected[start : start + size] in retrieved:
                return True
    return False


def find_rank(expected: str, ranked: list[dict]) -> int | None:
    for item in ranked:
        if chunk_matches(expected, item.get("text", item.get("preview", ""))):
            return int(item["rank"])
    return None


def faithfulness(answer: str, reference: str) -> float:
    try:
        from bert_score import score
    except ImportError:
        return 0.0
    try:
        _, _, f1 = score([answer], [reference], lang="pt", verbose=False)
        return float(f1.item())
    except Exception as exc:
        print(f"  BERTScore indisponivel: {exc}")
        return 0.0

def is_overloaded_error(exc: Exception) -> bool:
    response = getattr(exc, "response", None)

    if response is not None and getattr(response, "status_code", None) == 503:
        return True

    message = str(exc).lower()
    return (
        "503" in message
        or "service unavailable" in message
        or "overloaded" in message
        or "temporarily unavailable" in message
    )

def evaluate_configuration(name: str, options: RagOptions, dataset: list[dict]) -> tuple[dict, list[dict]]:
    faith_scores, mrr_scores, recall_scores, ranks = [], [], [], []
    details = []
    started = time.perf_counter()
    for number, row in enumerate(dataset, 1):
        continuar = True
        while(continuar):
            try:
                continuar = True
                question_started = time.perf_counter()
                result = answer_question(row["pergunta"], options)
                answer = result["answer"]
                ranked = result["ranked_retrieval"]
                rank = find_rank(row["chunk"], ranked)
                mrr = 1 / rank if rank else 0.0
                recall = mrr if rank and rank <= 4 else 0.0
                faith = faithfulness(answer, row["resposta"])
                faith_scores.append(faith)
                mrr_scores.append(mrr)
                recall_scores.append(recall)
                if rank:
                    ranks.append(rank)
                details.append({
                    "tecnica": name,
                    "linha": number,
                    "pergunta": row["pergunta"],
                    "resposta": answer,
                    "rank": rank,
                    "faithfulness": round(faith, 6),
                    "mrr": round(mrr, 6),
                    "recall_at_4": round(recall, 6),
                    "metrics": result["metrics"],
                    "sources": result["sources"],
                })
                elapsed = time.perf_counter() - question_started
                print(f"  OK {name} linha {number}/{len(dataset)} - {elapsed:.1f}s | faith={faith:.3f} mrr={mrr:.3f} r@4={recall:.3f} rank={rank or '-'}")
                print(f"     pipeline: {result['metrics']}")
                continuar = False
            except Exception as exc:
                if is_overloaded_error(exc):
                    print(
                        f"  ATENCAO {name} linha {number}: "
                        "servidor sobrecarregado - tentando novamente em 2s"
                    )
                    time.sleep(2)
                    continue
                else:
                    print(f"  FALHA {name} linha {number}: {exc}")
                    traceback.print_exc()
                    continuar = False
    processed = len(faith_scores)
    if not processed:
        return {"Tecnica": name, "Faithfulness": 0.0, "MRR": 0.0, "Recall@4": 0.0, "Rank_medio": 0.0, "Tempo_s": 0.0, "Linhas": 0}, details
    return {
        "Tecnica": name,
        "Faithfulness": round(sum(faith_scores) / processed, 3),
        "MRR": round(sum(mrr_scores) / processed, 3),
        "Recall@4": round(sum(recall_scores) / processed, 3),
        "Rank_medio": round(sum(ranks) / len(ranks), 2) if ranks else 0.0,
        "Tempo_s": round(time.perf_counter() - started, 1),
        "Linhas": processed,
    }, details


def save_results(summary: list[dict], details: list[dict]) -> None:
    results_dir = Path("user_data") / "local_demo" / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    (results_dir / f"benchmark_{stamp}.json").write_text(json.dumps({"summary": summary, "details": details}, ensure_ascii=False, indent=2), encoding="utf-8")
    if summary:
        with (results_dir / f"benchmark_{stamp}.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=summary[0].keys())
            writer.writeheader()
            writer.writerows(summary)
    print(f"Resultados salvos em {results_dir}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Benchmark local das tecnicas RAG")
    parser.add_argument("--dataset", default=os.getenv("EVAL_DATASET", "Dataset_eval_RAG_INPE.csv"))
    parser.add_argument("--limit", type=int, default=int(os.getenv("EVAL_LIMIT", "0")) or None)
    parser.add_argument("--rebuild", action="store_true", help="Reconstrói FAISS e grafo")
    parser.add_argument("--document", action="append", default=[], help="Documento adicional local; pode repetir")
    args = parser.parse_args()
    try:
        dataset = load_dataset(Path(args.dataset), args.limit)
        if not dataset:
            raise ValueError("Dataset vazio apos os filtros")
        if args.document:
            print(f"Documentos adicionados: {add_documents([Path(path) for path in args.document])}")
        print("Benchmark RAG local - sem FastAPI, Supabase ou localhost")
        print(f"Dataset: {args.dataset} ({len(dataset)} linhas)")
        print("APIs externas: NVIDIA e LlamaParse")
        if args.rebuild:
            print(f"Indice reconstruido: {rebuild_index()}")
        else:
            print("Indice: carregando ou construindo conforme os documentos")
            if build_or_load_vectors() is None:
                raise RuntimeError("Nenhum documento encontrado")
        summary, details = [], []
        for name, options in CONFIGURATIONS.items():
            result, rows = evaluate_configuration(name, options, dataset)
            summary.append(result)
            details.extend(rows)
        print("\n" + "=" * 95)
        print(f"{'TECNICA':<25} | {'FAITH.':<8} | {'MRR':<8} | {'R@4':<8} | {'RANK':<8} | {'TEMPO (s)':<10} | LINHAS")
        print("=" * 95)
        for row in summary:
            print(f"{row['Tecnica']:<25} | {row['Faithfulness']:<8.3f} | {row['MRR']:<8.3f} | {row['Recall@4']:<8.3f} | {row['Rank_medio']:<8.2f} | {row['Tempo_s']:<10} | {row['Linhas']}")
        print("=" * 95)
        print(f"\n{sum(row['Linhas'] > 0 for row in summary)}/{len(summary)} tecnicas concluidas")
        save_results(summary, details)
        return 0
    except Exception as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
