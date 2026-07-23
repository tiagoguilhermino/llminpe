import asyncio
import httpx
import time
import re
import json
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("EVAL_API_URL", os.getenv("API_BASE", "http://127.0.0.1:8000")).rstrip("/")
JWT_TOKEN = os.getenv("EVAL_JWT_TOKEN", "PIBIC_EVAL_MASTER_SECRET_2026")
REQUEST_TIMEOUT = float(os.getenv("EVAL_TIMEOUT", os.getenv("NVIDIA_TIMEOUT", "300")))
SLEEP_BETWEEN = float(os.getenv("EVAL_SLEEP", "5"))
# Caminho(s) do documento para o RAG. Aceita um arquivo ou vários separados por vírgula.
EVAL_DOCUMENTS = os.getenv("EVAL_DOCUMENTS", os.getenv("EVAL_DOCUMENT", ""))

TEST_QUESTION = "O que é o Goddard Profiling Algorithm?"
GROUND_TRUTH = (
    "É um algoritmo que capta precipitação na superfície e sua estrutura vertical a partir de observações de micro-ondas passivas de satélites."
)

CONFIGURATIONS = {
    "Baseline (FAISS)":    {"use_hyde": False, "use_multi_query": False, "use_reranking": False, "use_graph": False},
    "HyDE":                {"use_hyde": True,  "use_multi_query": False, "use_reranking": False, "use_graph": False},
    "Multi-Query":         {"use_hyde": False, "use_multi_query": True,  "use_reranking": False, "use_graph": False},
    "Reranking":           {"use_hyde": False, "use_multi_query": False, "use_reranking": True,  "use_graph": False},
    "Knowledge Graph":     {"use_hyde": False, "use_multi_query": False, "use_reranking": False, "use_graph": True},
    "HyDE + Reranking":    {"use_hyde": True,  "use_multi_query": False, "use_reranking": True,  "use_graph": False},
    "MQ + Reranking":      {"use_hyde": False, "use_multi_query": True,  "use_reranking": True,  "use_graph": False},
    "Todas as técnicas":   {"use_hyde": True,  "use_multi_query": True,  "use_reranking": True,  "use_graph": True}
}


def auth_headers() -> dict:
    return {"Authorization": f"Bearer {JWT_TOKEN}", "Content-Type": "application/json"}


def auth_headers_upload() -> dict:
    """Sem Content-Type: o httpx define o content-type sozinho, incluindo o boundary do multipart."""
    return {"Authorization": f"Bearer {JWT_TOKEN}"}


def resolve_eval_documents() -> list[Path]:
    """Retorna lista de arquivos .pdf/.txt configurados para o benchmark."""
    if not EVAL_DOCUMENTS.strip():
        return []
    paths = []
    for raw in EVAL_DOCUMENTS.split(","):
        p = Path(raw.strip())
        if not p.exists():
            print(f"⚠️  Documento não encontrado: {p}")
            continue
        if p.suffix.lower() not in (".pdf", ".txt"):
            print(f"⚠️  Formato não suportado (use .pdf ou .txt): {p}")
            continue
        paths.append(p)
    return paths


def tokenize(text: str) -> set:
    '''Transforma texto em conjunto de tokens (palavras com 3 ou mais caracteres, minúsculas).'''
    return set(re.findall(r"\b\w{3,}\b", text.lower()))


def parse_chat_response(endpoint: str, response: httpx.Response) -> tuple[str, dict]:
    """Extrai resposta e metadados do endpoint /chat (JSON) ou /chat/stream (SSE)."""
    if endpoint == "/chat":
        data = response.json()
        return data.get("answer", ""), data.get("metrics", {})

    answer_parts = []
    metrics = {}
    for line in response.text.splitlines(): #divido a resposta em linhas e coloco-as em uma lista
        if not line.startswith("data: "):
            continue #resposta não é do tipo SSE, ignoro
        try:
            #vou converter a linha em JSON, mas só a partir do 6º caractere, que é onde começa o JSON
            chunk = json.loads(line[6:]) 
        except json.JSONDecodeError:
            continue #ignoro linhas que não são JSON válido
        if chunk.get("type") == "token": #
            answer_parts.append(chunk.get("token", "")) #incluo o token na lista de partes da resposta
        elif chunk.get("type") == "meta":
            metrics = chunk.get("metrics", {}) #atualizo as métricas com os dados do chunk
    return "".join(answer_parts), metrics # junto todas as partes da resposta em uma única string e retorno junto com as métricas


def score_answer(answer: str) -> tuple[float, float]:
    '''Calcula métricas de Faithfulness e Relevancy entre resposta, ground truth e pergunta.'''
    ans_tokens = tokenize(answer)
    gt_tokens = tokenize(GROUND_TRUTH)
    q_tokens = tokenize(TEST_QUESTION)

    faith = len(ans_tokens & gt_tokens) / len(ans_tokens) if ans_tokens else 0.0 #mede o quanto da resposta é verdadeira (faithfulness)
    relev = len(q_tokens & ans_tokens) / len(q_tokens) if q_tokens else 0.0 #mede o quanto da resposta é relevante para a pergunta (relevancy)
    return faith, relev


async def check_api(client: httpx.AsyncClient) -> bool:
    '''Verifica se a API está acessível e responde corretamente em /config.'''
    try:
        r = await client.get(f"{API_URL}/config", timeout=10.0)
        if r.status_code != 200:
            print(f"❌ API respondeu {r.status_code} em /config")
            return False
        return True
    except httpx.RequestError as e:
        print(f"❌ API inacessível em {API_URL}: {e}")
        return False


async def create_eval_session(client: httpx.AsyncClient, name: str) -> str | None:
    """Cria sessão no Supabase via API (necessário após integração com auth)."""
    try:
        r = await client.post( #envio uma requisição POST para criar uma sessão de avaliação na API
            f"{API_URL}/sessions",
            json={"name": name},
            headers=auth_headers(),
            timeout=30.0,
        )
        if r.status_code == 200:
            return r.json().get("id") #retorno o ID da sessão criada
        if r.status_code == 503:
            print("❌ Bypass indisponível: configure SUPABASE_SERVICE_ROLE_KEY no .env do backend")
        else:
            print(f"❌ Falha ao criar sessão ({r.status_code}): {r.text[:200]}")
    except httpx.RequestError as e:
        print(f"❌ Erro de rede ao criar sessão: {e}")
    return None


async def upload_documents(client: httpx.AsyncClient, paths: list[Path]) -> list[str]:
    """Envia documentos para POST /upload (ficam em user_data do usuário de bypass)."""
    if not paths:
        return []

    files = []
    handles = []
    try:
        for p in paths:
            handle = p.open("rb") #transforma o arquivo em um objeto de arquivo binário para leitura
            handles.append(handle)
            mime = "application/pdf" if p.suffix.lower() == ".pdf" else "text/plain"
            files.append(("files", (p.name, handle, mime))) #insere o arquivo na lista de arquivos a serem enviados, com nome, handle e tipo MIME

        r = await client.post(
            f"{API_URL}/upload",
            headers=auth_headers_upload(),
            files=files,
            timeout=120.0,
        )
        if r.status_code == 200:
            saved = r.json().get("saved", [])
            print(f"📄 Documentos enviados: {', '.join(saved) or '(nenhum)'}")
            return saved
        print(f"❌ Falha no upload ({r.status_code}): {r.text[:200]}")
    except httpx.RequestError as e:
        print(f"❌ Erro de rede no upload: {e}")
    finally:
        for handle in handles:
            handle.close()
    return []


async def rebuild_index(client: httpx.AsyncClient, session_id: str) -> bool:
    """Recria índice FAISS e grafo para a sessão após upload de documentos."""
    try:
        r = await client.post(
            f"{API_URL}/rebuild-index",
            params={"session_id": session_id},
            headers=auth_headers(),
            timeout=300.0,
        )
        if r.status_code == 200:
            return True
        print(f"⚠️  rebuild-index falhou ({r.status_code}): {r.text[:120]}")
    except httpx.RequestError as e:
        print(f"⚠️  Erro ao recriar índice: {e}")
    return False


async def test_endpoint(client: httpx.AsyncClient, name: str, toggles: dict, *, has_documents: bool) -> dict:
    '''Faz os testes de benchmark para uma técnica específica, retornando métricas de desempenho.'''
    session_id = await create_eval_session(client, f"Eval — {name}")
    if not session_id:
        return {"Técnica": name, "Faithfulness": 0.0, "Relevancy": 0.0, "Tempo": 0.0}

    if has_documents:
        await rebuild_index(client, session_id)

    payload = {
        "session_id": session_id,
        "message": TEST_QUESTION,
        **toggles,
    }

    await asyncio.sleep(SLEEP_BETWEEN)

    for endpoint in ["/chat", "/chat/stream"]:
        start_time = time.perf_counter()
        try:
            response = await client.post(
                f"{API_URL}{endpoint}",
                json=payload,
                headers=auth_headers(),
                timeout=REQUEST_TIMEOUT,
            )

            if response.status_code == 200:
                elapsed = time.perf_counter() - start_time
                answer, metrics = parse_chat_response(endpoint, response)
                faith, relev = score_answer(answer)

                print(f"  ✅ {name} — {elapsed:.1f}s via {endpoint}")
                if metrics:
                    print(f"     métricas: {metrics}")
                return {
                    "Técnica": name,
                    "Faithfulness": round(faith, 3),
                    "Relevancy": round(relev, 3),
                    "Tempo": round(elapsed, 1),
                }

            print(f"  [DEBUG] {name} / {endpoint} → HTTP {response.status_code}: {response.text[:120]}")

        except httpx.ReadTimeout:
            print(f"  [DEBUG] {name} / {endpoint} → timeout ({REQUEST_TIMEOUT}s)")
        except httpx.RequestError as e:
            print(f"  [DEBUG] {name} / {endpoint} → {type(e).__name__}: {str(e)[:80]}")

    print(f"  ❌ {name} falhou (verifique API em {API_URL} e SUPABASE_SERVICE_ROLE_KEY)")
    return {"Técnica": name, "Faithfulness": 0.0, "Relevancy": 0.0, "Tempo": 0.0}


async def main():
    print("🚀 Benchmark RAG — 1 pergunta por técnica")
    print(f"   API:     {API_URL}")
    print(f"   Timeout: {REQUEST_TIMEOUT}s")
    print(f"   Token:   {'*' * 10 if JWT_TOKEN else '[NÃO DEFINIDO]'}")

    doc_paths = resolve_eval_documents()
    if doc_paths:
        print(f"   Docs:    {', '.join(p.name for p in doc_paths)}")
    else:
        print("   Docs:    pasta docs/ do servidor (ou defina EVAL_DOCUMENTS no .env)")
    print()

    results = []
    async with httpx.AsyncClient() as client:
        if not await check_api(client):
            sys.exit(1)

        uploaded = []
        if doc_paths:
            uploaded = await upload_documents(client, doc_paths)
            if not uploaded:
                print("❌ Nenhum documento foi aceito pelo servidor. Abortando.")
                sys.exit(1)

        has_documents = bool(doc_paths) or bool(uploaded)

        for name, toggles in CONFIGURATIONS.items():
            res = await test_endpoint(client, name, toggles, has_documents=has_documents)
            results.append(res)

    print("\n" + "=" * 70)
    print(f"{'TÉCNICA':<25} | {'FAITH.':<8} | {'RELEV.':<8} | {'TEMPO (s)':<10}")
    print("=" * 70)
    for r in results:
        print(f"{r['Técnica']:<25} | {r['Faithfulness']:<8.3f} | {r['Relevancy']:<8.3f} | {r['Tempo']:<10}")
    print("=" * 70)

    passed = sum(1 for r in results if r["Tempo"] > 0)
    print(f"\n{passed}/{len(results)} técnicas concluídas com sucesso")


if __name__ == "__main__":
    asyncio.run(main())
