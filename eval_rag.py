import asyncio
import httpx
import time
import re
import json
import os
import sys
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("EVAL_API_URL", os.getenv("API_BASE", "http://127.0.0.1:8000")).rstrip("/")
JWT_TOKEN = os.getenv("EVAL_JWT_TOKEN", "PIBIC_EVAL_MASTER_SECRET_2026")
REQUEST_TIMEOUT = float(os.getenv("EVAL_TIMEOUT", os.getenv("NVIDIA_TIMEOUT", "300")))
SLEEP_BETWEEN = float(os.getenv("EVAL_SLEEP", "5"))

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
    "Todas as técnicas":   {"use_hyde": True,  "use_multi_query": True,  "use_reranking": True,  "use_graph": True},
}


def auth_headers() -> dict:
    return {"Authorization": f"Bearer {JWT_TOKEN}", "Content-Type": "application/json"}


def tokenize(text: str) -> set:
    return set(re.findall(r"\b\w{3,}\b", text.lower()))


def parse_chat_response(endpoint: str, response: httpx.Response) -> tuple[str, dict]:
    """Extrai resposta e metadados do endpoint /chat (JSON) ou /chat/stream (SSE)."""
    if endpoint == "/chat":
        data = response.json()
        return data.get("answer", ""), data.get("metrics", {})

    answer_parts = []
    metrics = {}
    for line in response.text.splitlines():
        if not line.startswith("data: "):
            continue
        try:
            chunk = json.loads(line[6:])
        except json.JSONDecodeError:
            continue
        if chunk.get("type") == "token":
            answer_parts.append(chunk.get("token", ""))
        elif chunk.get("type") == "meta":
            metrics = chunk.get("metrics", {})
    return "".join(answer_parts), metrics


def score_answer(answer: str) -> tuple[float, float]:
    ans_tokens = tokenize(answer)
    gt_tokens = tokenize(GROUND_TRUTH)
    q_tokens = tokenize(TEST_QUESTION)

    faith = len(ans_tokens & gt_tokens) / len(ans_tokens) if ans_tokens else 0.0
    relev = len(q_tokens & ans_tokens) / len(q_tokens) if q_tokens else 0.0
    return faith, relev


async def check_api(client: httpx.AsyncClient) -> bool:
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
        r = await client.post(
            f"{API_URL}/sessions",
            json={"name": name},
            headers=auth_headers(),
            timeout=30.0,
        )
        if r.status_code == 200:
            return r.json().get("id")
        if r.status_code == 503:
            print("❌ Bypass indisponível: configure SUPABASE_SERVICE_ROLE_KEY no .env do backend")
        else:
            print(f"❌ Falha ao criar sessão ({r.status_code}): {r.text[:200]}")
    except httpx.RequestError as e:
        print(f"❌ Erro de rede ao criar sessão: {e}")
    return None


async def test_endpoint(client: httpx.AsyncClient, name: str, toggles: dict) -> dict:
    session_id = await create_eval_session(client, f"Eval — {name}")
    if not session_id:
        return {"Técnica": name, "Faithfulness": 0.0, "Relevancy": 0.0, "Tempo": 0.0}

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
    print(f"   Token:   {'*' * 10 if JWT_TOKEN else '[NÃO DEFINIDO]'}\n")

    results = []
    async with httpx.AsyncClient() as client:
        if not await check_api(client):
            sys.exit(1)

        for name, toggles in CONFIGURATIONS.items():
            res = await test_endpoint(client, name, toggles)
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
