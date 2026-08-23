import asyncio
import csv
import httpx
import time
import re
import json
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

try:
    from bert_score import score as bert_score_fn
    BERTSCORE_AVAILABLE = True
except ImportError:
    BERTSCORE_AVAILABLE = False

API_URL = os.getenv("EVAL_API_URL", os.getenv("API_BASE", "http://127.0.0.1:8000")).rstrip("/")
JWT_TOKEN = os.getenv("EVAL_JWT_TOKEN", "PIBIC_EVAL_MASTER_SECRET_2026")
REQUEST_TIMEOUT = float(os.getenv("EVAL_TIMEOUT", os.getenv("NVIDIA_TIMEOUT", "300")))
REBUILD_TIMEOUT = float(os.getenv("EVAL_REBUILD_TIMEOUT", "600"))
UPLOAD_TIMEOUT = float(os.getenv("EVAL_UPLOAD_TIMEOUT", "120"))
SLEEP_BETWEEN = float(os.getenv("EVAL_SLEEP", "3"))
RETRY_ATTEMPTS = int(os.getenv("EVAL_RETRY_ATTEMPTS", "3"))
RETRY_DELAY = float(os.getenv("EVAL_RETRY_DELAY", "10"))
DOCS_PARSE_DIR = Path("docs") / "parse"
EVAL_DOCUMENTS = os.getenv("EVAL_DOCUMENTS", os.getenv("EVAL_DOCUMENT", ""))
EVAL_DATASET = os.getenv("EVAL_DATASET", "Dataset_eval_RAG_INPE.csv")
EVAL_LIMIT = int(os.getenv("EVAL_LIMIT", "0")) or None
BERT_MODEL = os.getenv("EVAL_BERT_MODEL", "bert-base-multilingual-cased")


def resolve_eval_device() -> str:
    explicit = os.getenv("EVAL_DEVICE", "").strip()
    if explicit:
        return explicit
    try:
        import torch
        return "cuda" if torch.cuda.is_available() else "cpu"
    except ImportError:
        return "cpu"


EVAL_DEVICE = resolve_eval_device()

CONFIGURATIONS = {
    "Baseline (FAISS)":    {"use_hyde": False, "use_multi_query": False, "use_reranking": False, "use_graph": False},
    "HyDE":                {"use_hyde": True,  "use_multi_query": False, "use_reranking": False, "use_graph": False},
    "Multi-Query":         {"use_hyde": False, "use_multi_query": True,  "use_reranking": False, "use_graph": False},
    "Reranking":           {"use_hyde": False, "use_multi_query": False, "use_reranking": True,  "use_graph": False},
    "Knowledge Graph":     {"use_hyde": False, "use_multi_query": False, "use_reranking": False, "use_graph": True},
    "HyDE + Reranking":    {"use_hyde": True,  "use_multi_query": False, "use_reranking": True,  "use_graph": False},
    "MQ + Reranking":      {"use_hyde": False, "use_multi_query": True,  "use_reranking": True,  "use_graph": False},
    "Todas as técnicas":   {"use_hyde": True,  "use_multi_query": True,  "use_reranking": True,  "use_graph": True},
}


def auth_headers() -> dict:
    return {"Authorization": f"Bearer {JWT_TOKEN}", "Content-Type": "application/json"}


def auth_headers_upload() -> dict:
    return {"Authorization": f"Bearer {JWT_TOKEN}"}


def load_eval_dataset(path: str | Path, limit: int | None = None) -> list[dict]:
    """Carrega o CSV de avaliação com colunas chunk, resposta e pergunta."""
    dataset_path = Path(path)
    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset não encontrado: {dataset_path}")

    required = {"chunk", "resposta", "pergunta"}
    rows: list[dict] = []
    with dataset_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            raise ValueError(f"CSV deve conter colunas {sorted(required)}; encontrado: {reader.fieldnames}")
        for row in reader:
            chunk = (row.get("chunk") or "").strip()
            resposta = (row.get("resposta") or "").strip()
            pergunta = (row.get("pergunta") or "").strip()
            if not chunk or not resposta or not pergunta:
                continue
            rows.append({"chunk": chunk, "resposta": resposta, "pergunta": pergunta})
            if limit and len(rows) >= limit:
                break
    return rows

def list_server_docs() -> list[Path]:
    """Arquivos em docs/ ja disponiveis ao servidor (nao precisam de upload)."""
    docs_folder = Path("docs")
    if not docs_folder.is_dir():
        return []
    return [
        p for p in docs_folder.iterdir()
        if p.is_file() and p.suffix.lower() in (".pdf", ".txt")
    ]


def list_unparsed_pdfs(docs: list[Path]) -> list[Path]:
    """PDFs em docs/ que ainda nao possuem Markdown em docs/parse/."""
    missing = []
    for pdf in docs:
        if pdf.suffix.lower() != ".pdf":
            continue
        md_path = DOCS_PARSE_DIR / f"{pdf.stem}.md"
        if not md_path.exists() or md_path.stat().st_mtime < pdf.stat().st_mtime:
            missing.append(pdf)
    return missing


def ensure_local_markdown(docs: list[Path]) -> bool:
    """Converte PDFs locais para Markdown antes de chamar a API (evita timeout no rebuild)."""
    missing = list_unparsed_pdfs(docs)
    if not missing:
        return True

    print(f"  {len(missing)} PDF(s) sem Markdown em docs/parse/.")
    print("  Convertendo localmente via LlamaParse (pode levar varios minutos)...")
    try:
        from preparse_docs import parse_folder

        parsed = parse_folder(Path("docs"), DOCS_PARSE_DIR)
        still_missing = list_unparsed_pdfs(docs)
        if still_missing:
            print(f"  Ainda faltam {len(still_missing)} Markdown(s). Verifique LLAMA_CLOUD_API_KEY e os logs.")
            return False
        print(f"  Markdown pronto ({parsed} PDF(s) convertido(s) agora).")
        return True
    except Exception as exc:
        print(f"  Falha ao converter PDFs localmente: {exc}")
        print("  Execute manualmente: python preparse_docs.py")
        return False


def resolve_upload_documents() -> list[Path]:
    """Arquivos extras definidos em EVAL_DOCUMENTS (enviados via POST /upload)."""
    if not EVAL_DOCUMENTS.strip():
        return []
    paths = []
    for raw in EVAL_DOCUMENTS.split(","):
        p = Path(raw.strip())
        if not p.exists():
            print(f"  Documento nao encontrado: {p}")
            continue
        if p.suffix.lower() not in (".pdf", ".txt"):
            print(f"  Formato nao suportado (use .pdf ou .txt): {p}")
            continue
        if p.resolve() in {d.resolve() for d in list_server_docs()}:
            continue
        paths.append(p)
    return paths


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower().strip())


def chunks_match(expected: str, retrieved: str, min_overlap: int = 60) -> bool:
    """Verifica se o trecho esperado corresponde a um chunk recuperado."""
    a = normalize_text(expected)
    b = normalize_text(retrieved)
    if not a or not b:
        return False

    prefix_len = min(len(a), 150, len(b))
    prefix = a[:prefix_len]
    if len(prefix) >= min_overlap and prefix in b:
        return True

    retrieved_prefix = b[: min(len(b), 150)]
    if len(retrieved_prefix) >= min_overlap and retrieved_prefix in a:
        return True

    max_size = min(len(a), len(b))
    for size in range(max_size, min_overlap - 1, -1):
        for start in range(len(a) - size + 1):
            if a[start : start + size] in b:
                return True
    return False


def find_chunk_rank(expected_chunk: str, ranked_retrieval: list[dict]) -> int | None:
    for item in ranked_retrieval:
        rank = item.get("rank")
        text = item.get("text") or item.get("preview", "")
        if rank and chunks_match(expected_chunk, text):
            return int(rank)
    return None


def score_retrieval(expected_chunk: str, ranked_retrieval: list[dict]) -> tuple[float, float]:
    rank = find_chunk_rank(expected_chunk, ranked_retrieval)
    if not rank:
        return 0.0, 0.0
    mrr = 1.0 / rank
    recall_at_4 = mrr if rank <= 4 else 0.0
    return mrr, recall_at_4


def score_faithfulness(answer: str, reference: str) -> float:
    if not BERTSCORE_AVAILABLE:
        print("  bert-score nao instalado; faithfulness = 0.0")
        return 0.0
    if not answer.strip() or not reference.strip():
        return 0.0
    try:
        _, _, f1 = bert_score_fn(
            cands=[answer],
            refs=[reference],
            lang="pt",
            model_type=BERT_MODEL,
            device=EVAL_DEVICE,
            batch_size=1,
            verbose=False,
        )
        return float(f1.item())
    except Exception as exc:
        print(f"  BERTScore falhou: {exc}")
        return 0.0


def parse_chat_response(response: httpx.Response) -> tuple[str, dict, list]:
    data = response.json()
    return (
        data.get("answer", ""),
        data.get("metrics", {}),
        data.get("ranked_retrieval", []),
    )


async def post_with_retry(client: httpx.AsyncClient, url: str, **kwargs) -> httpx.Response | None:
    """Repete requisicoes quando o servidor cai ou desconecta no meio da resposta."""
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            return await client.post(url, **kwargs)
        except (httpx.ConnectError, httpx.RemoteProtocolError, httpx.ReadError) as exc:
            if attempt == RETRY_ATTEMPTS:
                raise
            wait = RETRY_DELAY * attempt
            print(
                f"  Conexao perdida ({type(exc).__name__}); "
                f"tentativa {attempt}/{RETRY_ATTEMPTS} em {wait:.0f}s..."
            )
            await asyncio.sleep(wait)
            if not await check_api(client):
                print("  Servidor indisponivel. Reinicie com: uvicorn main:app --host 127.0.0.1 --port 8000")
    return None


async def check_api(client: httpx.AsyncClient) -> bool:
    try:
        r = await client.get(f"{API_URL}/config", timeout=10.0)
        if r.status_code != 200:
            print(f"  API respondeu {r.status_code} em /config")
            return False
        return True
    except httpx.RequestError as exc:
        print(f"  API inacessivel em {API_URL}: {exc}")
        return False


async def create_eval_session(client: httpx.AsyncClient, name: str) -> str | None:
    try:
        r = await client.post(
            f"{API_URL}/sessions",
            json={"name": name},
            headers=auth_headers(),
            timeout=30.0,
        )
        if r.status_code == 200:
            return r.json().get("id")
        if r.status_code == 503:
            print("  Bypass indisponivel: configure SUPABASE_SERVICE_ROLE_KEY no .env do backend")
        else:
            print(f"  Falha ao criar sessao ({r.status_code}): {r.text[:200]}")
    except httpx.RequestError as exc:
        print(f"  Erro de rede ao criar sessao: {exc}")
    return None


async def upload_documents(client: httpx.AsyncClient, paths: list[Path]) -> list[str]:
    if not paths:
        return []

    handles: list = []
    try:
        files = []
        for p in paths:
            handle = p.open("rb")
            handles.append(handle)
            if p.suffix.lower() == ".pdf":
                mime = "application/pdf"
            elif p.suffix.lower() in (".md", ".markdown"):
                mime = "text/markdown"
            else:
                mime = "text/plain"
            files.append(("files", (p.name, handle, mime)))

        r = await client.post(
            f"{API_URL}/upload",
            headers=auth_headers_upload(),
            files=files,
            timeout=UPLOAD_TIMEOUT,
        )
        if r.status_code == 200:
            saved = r.json().get("saved", [])
            print(f"  Documentos enviados ({len(saved)}): {', '.join(saved) or '(nenhum)'}")
            return saved
        if r.status_code == 429:
            print(f"  Rate limit no upload (429). Aguarde 1 minuto ou reinicie o eval.")
        print(f"  Falha no upload ({r.status_code}): {r.text[:200]}")
    except httpx.TimeoutException:
        print(f"  Timeout no upload ({UPLOAD_TIMEOUT}s). Aumente EVAL_UPLOAD_TIMEOUT.")
    except httpx.RequestError as exc:
        print(f"  Erro de rede no upload: {exc or type(exc).__name__}")
    finally:
        for handle in handles:
            handle.close()
    return []


async def fetch_rag_status(client: httpx.AsyncClient, session_id: str) -> dict:
    try:
        r = await client.get(
            f"{API_URL}/rag/status",
            params={"session_id": session_id},
            headers=auth_headers(),
            timeout=30.0,
        )
        if r.status_code == 200:
            return r.json()
    except httpx.RequestError:
        pass
    return {}


async def rebuild_index(client: httpx.AsyncClient, session_id: str) -> bool:
    try:
        r = await client.post(
            f"{API_URL}/rebuild-index",
            params={"session_id": session_id},
            headers=auth_headers(),
            timeout=REBUILD_TIMEOUT,
        )
        if r.status_code == 200:
            data = r.json()
            print(
                "  rebuild-index concluido "
                f"({data.get('loaded_documents', '?')} docs, "
                f"{data.get('markdown_files', '?')} .md em docs/parse)."
            )
            return True
        if r.status_code == 503:
            detail = r.json().get("detail", {})
            status = detail.get("status", detail) if isinstance(detail, dict) else detail
            print(f"  rebuild-index: servidor nao carregou documentos.")
            if isinstance(status, dict):
                print(
                    f"    docs/parse existe: {status.get('docs_parse_exists')} | "
                    f".md encontrados: {status.get('markdown_files')} | "
                    f"docs carregados: {status.get('loaded_documents')}"
                )
                print(f"    caminho no servidor: {status.get('docs_parse_dir')}")
            return False
        if r.status_code == 429:
            print("  rebuild-index bloqueado por rate limit (429). Aguarde 1 minuto.")
        print(f"  rebuild-index falhou ({r.status_code}): {r.text[:200]}")
    except httpx.TimeoutException:
        print(f"  rebuild-index excedeu timeout ({REBUILD_TIMEOUT}s). Aumente EVAL_REBUILD_TIMEOUT.")
    except httpx.RequestError as exc:
        print(f"  Erro ao recriar indice: {exc or type(exc).__name__}")
    return False


async def probe_rag(client: httpx.AsyncClient, session_id: str, question: str) -> tuple[bool, int, str]:
    """Verifica se o servidor retornou trechos ranqueados (RAG ativo)."""
    try:
        response = await client.post(
            f"{API_URL}/chat",
            json={
                "session_id": session_id,
                "message": question,
                "use_hyde": False,
                "use_multi_query": False,
                "use_reranking": False,
                "use_graph": False,
            },
            headers=auth_headers(),
            timeout=REQUEST_TIMEOUT,
        )
    except httpx.ReadTimeout:
        return False, 0, f"timeout ({REQUEST_TIMEOUT}s)"
    except httpx.RequestError as exc:
        return False, 0, str(exc or type(exc).__name__)
    if response.status_code != 200:
        return False, 0, f"HTTP {response.status_code}"
    _, _, ranked = parse_chat_response(response)
    if ranked:
        return True, len(ranked), ""
    return False, 0, "ranked_retrieval vazio"


async def ensure_documents_indexed(
    client: httpx.AsyncClient,
    session_id: str,
    server_docs: list[Path],
    upload_paths: list[Path],
    probe_question: str,
) -> bool:
    """Garante indice RAG pronto; faz upload local se o servidor nao enxergar docs/."""
    if not server_docs and not upload_paths:
        print("  Aviso: nenhum documento local; metricas de retrieval podem ficar em 0.")

    if server_docs and not ensure_local_markdown(server_docs):
        return False

    if upload_paths:
        uploaded = await upload_documents(client, upload_paths)
        if not uploaded:
            print("  Nenhum documento extra foi aceito pelo servidor.")
            return False

    if server_docs or upload_paths:
        print("  Recriando indice RAG (uma vez para todas as tecnicas)...")
        if not await rebuild_index(client, session_id):
            print("  rebuild-index falhou.")
            return False

        if probe_question:
            ok, n, probe_err = await probe_rag(client, session_id, probe_question)
            if ok:
                print(f"  RAG ativo ({n} trechos no probe).")
                return True

            status = await fetch_rag_status(client, session_id)
            md_count = status.get("markdown_files", 0)
            loaded = status.get("loaded_documents", 0)
            print(f"  Probe falhou: {probe_err}.")
            if md_count > 0 and loaded > 0:
                print(
                    "  Servidor ve os documentos e o indice existe, mas a busca nao retornou trechos. "
                    "Pode ser timeout no chat ou pergunta de probe sem match."
                )
                return True
            if md_count > 0 and loaded == 0:
                print(
                    "  Servidor ve docs/parse/ mas nao conseguiu carregar os arquivos. "
                    "Verifique encoding/permissoes dos .md."
                )
                return False
            if server_docs:
                print(
                    "  Servidor nao ve docs/parse/ (markdown_files=0). "
                    "Confirme volume ./docs:/app/docs e recrie o container."
                )
                print("  Enviando Markdown parseado (docs/parse/) como fallback...")
                md_paths = sorted(DOCS_PARSE_DIR.glob("*.md")) if DOCS_PARSE_DIR.exists() else []
                if not md_paths:
                    print("  Nenhum .md em docs/parse/. Execute: python preparse_docs.py")
                    return False
                uploaded = await upload_documents(client, md_paths)
                if not uploaded:
                    print("  Upload dos Markdowns locais falhou.")
                    return False
                if not await rebuild_index(client, session_id):
                    print("  rebuild-index apos upload falhou.")
                    return False
                ok, n, probe_err = await probe_rag(client, session_id, probe_question)
                if ok:
                    print(f"  RAG ativo apos upload ({n} trechos no probe).")
                    return True
                print(f"  Probe apos upload falhou: {probe_err}.")

        print("  RAG inativo: ranked_retrieval vazio. MRR/Recall@4 ficarao em 0.")
        return False

    return True


async def test_endpoint(
    client: httpx.AsyncClient,
    name: str,
    toggles: dict,
    *,
    session_id: str,
    dataset: list[dict],
) -> dict:
    
    empty = {
        "Técnica": name,
        "Faithfulness": 0.0,
        "MRR": 0.0,
        "Recall@4": 0.0,
        "Rank_médio": 0.0,
        "Tempo": 0.0,
        "Linhas": 0,
    }

    faith_scores: list[float] = []
    mrr_scores: list[float] = []
    recall_scores: list[float] = []
    ranks: list[int] = []
    total_time = 0.0
    processed = 0

    for idx, row in enumerate(dataset, start=1):
        payload = {
            "session_id": session_id,
            "message": row["pergunta"],
            **toggles,
        }
        await asyncio.sleep(SLEEP_BETWEEN)

        start_time = time.perf_counter()
        try:
            response = await post_with_retry(
                client,
                f"{API_URL}/chat",
                json=payload,
                headers=auth_headers(),
                timeout=REQUEST_TIMEOUT,
            )
        except httpx.ReadTimeout:
            print(f"  [DEBUG] {name} linha {idx} → timeout ({REQUEST_TIMEOUT}s)")
            continue
        except httpx.RequestError as exc:
            print(f"  [DEBUG] {name} linha {idx} → {type(exc).__name__}: {str(exc)[:80]}")
            continue

        if response is None:
            continue

        if response.status_code != 200:
            print(f"  [DEBUG] {name} linha {idx} → HTTP {response.status_code}: {response.text[:120]}")
            continue

        elapsed = time.perf_counter() - start_time
        total_time += elapsed
        answer, metrics, ranked = parse_chat_response(response)

        faith = score_faithfulness(answer, row["resposta"])
        mrr, recall4 = score_retrieval(row["chunk"], ranked)
        rank = find_chunk_rank(row["chunk"], ranked)

        faith_scores.append(faith)
        mrr_scores.append(mrr)
        recall_scores.append(recall4)
        if rank is not None:
            ranks.append(rank)
        processed += 1

        print(
            f"  OK {name} linha {idx}/{len(dataset)} — {elapsed:.1f}s "
            f"| faith={faith:.3f} mrr={mrr:.3f} r@4={recall4:.3f} rank={rank or '-'}"
        )
        if metrics:
            print(f"     pipeline: {metrics}")

    if processed == 0:
        print(f"  {name} falhou em todas as linhas")
        return empty

    return {
        "Técnica": name,
        "Faithfulness": round(sum(faith_scores) / processed, 3),
        "MRR": round(sum(mrr_scores) / processed, 3),
        "Recall@4": round(sum(recall_scores) / processed, 3),
        "Tempo": round(total_time, 1),
        "Linhas": processed,
        "Rank_médio": round(sum(ranks) / processed, 2) if ranks else 0.0, #penaliza rank=0 para linhas sem match
    }


async def main():
    try:
        dataset = load_eval_dataset(EVAL_DATASET, limit=EVAL_LIMIT)
    except (FileNotFoundError, ValueError) as exc:
        print(f"  {exc}")
        sys.exit(1)

    if not dataset:
        print("  Dataset vazio apos filtros.")
        sys.exit(1)

    print("Benchmark RAG — dataset CSV")
    print(f"   API:      {API_URL}")
    print(f"   Dataset:  {EVAL_DATASET} ({len(dataset)} linhas)")
    print(f"   Timeout:  {REQUEST_TIMEOUT}s")
    print(f"   Sleep:    {SLEEP_BETWEEN}s")
    print(f"   BERT:     {BERT_MODEL} ({EVAL_DEVICE})")
    print(f"   Token:    {'*' * 10 if JWT_TOKEN else '[NÃO DEFINIDO]'}")

    server_docs = list_server_docs()
    upload_paths = resolve_upload_documents()
    has_documents = bool(server_docs) or bool(upload_paths)

    if server_docs:
        print(f"   Docs:     {len(server_docs)} arquivo(s) em docs/ (indexados pelo servidor, sem upload)")
    if upload_paths:
        print(f"   Upload:   {', '.join(p.name for p in upload_paths)}")
    if not has_documents:
        print("   Docs:     nenhum (coloque PDFs em docs/ ou defina EVAL_DOCUMENTS no .env)")
    

    results = []
    async with httpx.AsyncClient() as client:
        if not await check_api(client):
            sys.exit(1)

        session_id = await create_eval_session(client, "Eval — benchmark")
        if not session_id:
            sys.exit(1)

        probe_question = dataset[0]["pergunta"] if dataset else ""
        if not await ensure_documents_indexed(
            client, session_id, server_docs, upload_paths, probe_question
        ):
            if server_docs or upload_paths:
                print("  Abortando: indice RAG nao ficou pronto.")
                sys.exit(1)

        for name, toggles in CONFIGURATIONS.items():
            res = await test_endpoint(
                client,
                name,
                toggles,
                session_id=session_id,
                dataset=dataset,
            )
            results.append(res)

    print("\n" + "=" * 90)
    print(f"{'TÉCNICA':<25} | {'FAITH.':<8} | {'MRR':<8} | {'R@4':<8} | {'RANK':<8} | {'TEMPO (s)':<10} | {'LINHAS':<6}")
    print("=" * 90)
    for row in results:
        print(
            f"{row['Técnica']:<25} | {row['Faithfulness']:<8.3f} | {row['MRR']:<8.3f} | "
            f"{row['Recall@4']:<8.3f} | {row['Rank_médio']:<8.2f} | {row['Tempo']:<10} | {row['Linhas']:<6}"
        )
    print("=" * 90)

    passed = sum(1 for row in results if row["Linhas"] > 0)
    print(f"\n{passed}/{len(results)} técnicas concluídas com sucesso")


if __name__ == "__main__":
    asyncio.run(main())
