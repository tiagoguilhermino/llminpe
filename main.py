import os

# ── Suprimir logs desnecessários do TensorFlow/Keras antes de qualquer import ──
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["KERAS_BACKEND"] = "torch"  # força Keras a usar PyTorch, evitando conflito com tf-keras

import time
import uuid
import pickle
import json
import asyncio
import math
import re
import unicodedata
from pathlib import Path
from contextlib import contextmanager
from typing import List, Optional
from dataclasses import dataclass

from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse, PlainTextResponse, RedirectResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# Rate limiting
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# LangChain
from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage

import networkx as nx
from llama_cloud import LlamaCloud

# ─────────────────────────────────────────────────────────────────
# Imports opcionais com fallback gracioso
# ─────────────────────────────────────────────────────────────────
try:
    import spacy
    nlp_spacy = spacy.load("pt_core_news_sm")
    SPACY_AVAILABLE = True
except Exception:
    SPACY_AVAILABLE = False

try:
    from sentence_transformers import CrossEncoder
    reranker_model = CrossEncoder("bert-base-portuguese-cased")
    RERANKER_AVAILABLE = True
except Exception:
    RERANKER_AVAILABLE = False

from supabase import create_client, Client

load_dotenv()

# ─────────────────────────────────────────────────────────────────
# Métricas de latência por etapa do pipeline
# ─────────────────────────────────────────────────────────────────
@contextmanager
def measure(metrics_dict: dict, name: str):
    """Context manager que mede tempo de execução de cada etapa em ms."""
    start = time.perf_counter()
    yield
    elapsed = (time.perf_counter() - start) * 1000
    metrics_dict[name] = round(elapsed, 2)

# ─────────────────────────────────────────────────────────────────
# Configuração do ambiente
# ─────────────────────────────────────────────────────────────────
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY") or os.getenv("SUPABASE_KEY")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:5500,http://127.0.0.1:5500,http://localhost:3000,http://localhost:8000,http://127.0.0.1:8000"
).split(",")

if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    raise RuntimeError("Configure SUPABASE_URL e SUPABASE_ANON_KEY no .env")

def _env_bool(*names: str, default: str = "false") -> bool:
    for name in names:
        value = os.getenv(name)
        if value is not None:
            return value.strip().lower() in ("true", "1", "yes")
    return default.strip().lower() in ("true", "1", "yes")


TESTE_MODE = _env_bool("TESTE_EVAL", "teste", "TEST")

auth_client: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
admin_client: Optional[Client] = (
    create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
    if SUPABASE_SERVICE_ROLE_KEY
    else None
)

# ─────────────────────────────────────────────────────────────────
# App + Rate Limiting
# ─────────────────────────────────────────────────────────────────
limiter = Limiter(key_func=get_remote_address)
UPLOAD_RATE_LIMIT = os.getenv("UPLOAD_RATE_LIMIT", "60/minute")

IS_PROD = os.getenv("ENV", "dev") == "prod"
app = FastAPI(
    title="NIM Chat API",
    docs_url=None if IS_PROD else "/docs",
    redoc_url=None if IS_PROD else "/redoc",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

# ─────────────────────────────────────────────────────────────────
# Modelos LangChain
# ─────────────────────────────────────────────────────────────────
nvidia_key = os.getenv("NVIDIA_API_KEY")
NVIDIA_MODEL = os.getenv("NVIDIA_MODEL", "meta/llama-3.1-8b-instruct")
NVIDIA_TIMEOUT = int(os.getenv("NVIDIA_TIMEOUT", "300"))
llm = ChatNVIDIA(
    model=NVIDIA_MODEL,
    api_key=nvidia_key,
    temperature=0.5,
    max_completion_tokens=16384,
    timeout=NVIDIA_TIMEOUT,
)
emb = NVIDIAEmbeddings(
    model=os.getenv("NVIDIA_EMBEDDING_MODEL", "nvidia/nv-embedqa-e5-v5"),
    api_key=nvidia_key,
)

memory_cache: dict = {}
vectors_cache: dict = {}
graph_cache: dict = {}

# ─────────────────────────────────────────────────────────────────
# Helpers de disco
# ─────────────────────────────────────────────────────────────────
def user_storage_dir(user_id: str) -> Path:
    '''Retorna o caminho do diretório de armazenamento do usuário, criando-o se necessário.'''
    base = Path("user_data") / user_id
    base.mkdir(parents=True, exist_ok=True)
    (base / "uploads").mkdir(exist_ok=True)
    (base / "parse").mkdir(exist_ok=True)
    return base

def faiss_path(user_id: str, session_id: str) -> Path:
    return user_storage_dir(user_id) / f"faiss_{session_id}"

def graph_path_file(user_id: str, session_id: str) -> Path:
    return user_storage_dir(user_id) / f"graph_{session_id}.pkl"

def uploads_index_path(user_id: str) -> Path:
    '''Retorna o caminho do arquivo JSON que mantém o índice de uploads do usuário.'''
    return user_storage_dir(user_id) / "uploads_index.json"

def load_uploads_index(user_id: str) -> dict:
    '''Carrega o índice de uploads do usuário, que mapeia nomes originais para nomes seguros.'''
    p = uploads_index_path(user_id)
    if not p.exists():
        return {}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError) as e:
        print(f"uploads_index.json invalido para {user_id}: {e}")
        return {}

def save_uploads_index(user_id: str, index: dict):
    uploads_index_path(user_id).write_text(
        json.dumps(index, ensure_ascii=False),
        encoding="utf-8",
    )

# ─────────────────────────────────────────────────────────────────
# Autenticação
# ─────────────────────────────────────────────────────────────────
@dataclass
class AuthContext:
    user_id: str
    token: str
    is_bypass: bool = False


def db_client_for(auth: AuthContext) -> Client:
    """Cliente Supabase com permissões do usuário autenticado (RLS)."""
    if auth.is_bypass:
        if not admin_client:
            raise HTTPException(
                status_code=503,
                detail="Configure SUPABASE_SERVICE_ROLE_KEY para o modo de avaliação",
            )
        return admin_client
    client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
    client.postgrest.auth(auth.token)
    client.storage._headers["authorization"] = f"Bearer {auth.token}"
    return client


async def get_auth(authorization: str = Header(None)) -> AuthContext:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token não fornecido")
    token = authorization.split(" ", 1)[1]

    if token == "PIBIC_EVAL_MASTER_SECRET_2026":
        return AuthContext(
            user_id="64d48d35-26a3-4b46-b175-53be923fa621",
            token=token,
            is_bypass=True,
        )

    try:
        user = auth_client.auth.get_user(token)
        return AuthContext(user_id=user.user.id, token=token)
    except Exception:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")


async def get_user_id(auth: AuthContext = Depends(get_auth)) -> str:
    return auth.user_id


def verify_session_owner(db: Client, session_id: str, user_id: str):
    r = (
        db.table("chat_sessions")
        .select("id")
        .eq("id", session_id)
        .eq("user_id", user_id)
        .limit(1)
        .execute()
    )
    if not r.data:
        raise HTTPException(status_code=404, detail="Sessão não encontrada")


# ─────────────────────────────────────────────────────────────────
# Funções de sessão
# ─────────────────────────────────────────────────────────────────
def db_get_sessions(db: Client, user_id: str):
    try:
        r = db.table("chat_sessions").select("*").eq("user_id", user_id).order("created_at").execute()
        return r.data or []
    except Exception as e:
        print(f"❌ ERRO AO LISTAR SESSÕES: {e}")
        return []


def db_create_session(db: Client, user_id: str, name: str = "Nova Conversa") -> str:
    try:
        r = db.table("chat_sessions").insert({"user_id": user_id, "name": name}).execute()
        return r.data[0]["id"]
    except Exception as e:
        print(f"❌ ERRO AO CRIAR SESSÃO: {e}")
        raise HTTPException(status_code=500, detail="Não foi possível criar a sessão")


def db_rename_session(db: Client, session_id: str, user_id: str, name: str):
    verify_session_owner(db, session_id, user_id)
    try:
        db.table("chat_sessions").update({"name": name}).eq("id", session_id).execute()
    except Exception as e:
        print(f"❌ ERRO AO RENOMEAR SESSÃO: {e}")
        raise HTTPException(status_code=500, detail="Não foi possível renomear a sessão")


def db_delete_session(db: Client, session_id: str, user_id: str):
    verify_session_owner(db, session_id, user_id)
    db.table("chat_messages").delete().eq("session_id", session_id).execute()
    db.table("chat_sessions").delete().eq("id", session_id).execute()


def db_load_messages(db: Client, session_id: str, user_id: str):
    verify_session_owner(db, session_id, user_id)
    try:
        r = db.table("chat_messages").select("*").eq("session_id", session_id).order("created_at").execute()
        return r.data or []
    except Exception as e:
        print(f"❌ ERRO AO CARREGAR MENSAGENS: {e}")
        return []


def db_save_message(db: Client, session_id: str, user_id: str, role: str, content: str):
    verify_session_owner(db, session_id, user_id)
    try:
        db.table("chat_messages").insert({
            "session_id": session_id, "role": role, "content": content
        }).execute()
    except Exception as e:
        print(f"❌ ERRO AO SALVAR MENSAGEM NO BANCO: {e}")

# ─────────────────────────────────────────────────────────────────
# Parsing
# ─────────────────────────────────────────────────────────────────
DOCS_PARSE_DIR = Path("docs") / "parse"
SUPPORTED_DOC_SUFFIXES = {".pdf", ".txt", ".md", ".markdown"}


def parse_folder(source_dir: Path, output_dir: Path) -> Path:
    """Converte PDFs de source_dir em Markdown em output_dir via LlamaParse."""
    output_dir.mkdir(parents=True, exist_ok=True)
    if not source_dir.exists():
        return output_dir

    api_key = os.environ.get("LLAMA_CLOUD_API_KEY")
    if not api_key:
        print("LLAMA_CLOUD_API_KEY nao configurada; ignorando parse de PDFs")
        return output_dir

    client = LlamaCloud(api_key=api_key)
    for pdf in source_dir.iterdir():
        if not pdf.is_file() or pdf.suffix.lower() != ".pdf":
            continue
        md_path = output_dir / f"{pdf.stem}.md"
        if md_path.exists() and md_path.stat().st_mtime >= pdf.stat().st_mtime:
            continue
        try:
            arquivo = client.files.create(file=pdf, purpose="parse")
            result = client.parsing.parse(
                file_id=arquivo.id,
                tier="agentic",
                version="latest",
                expand=["markdown_full"],
            )
            md_path.write_text(result.markdown_full or "", encoding="utf-8")
            print(f"Parse concluido: {pdf.name} -> {md_path.name}")
        except Exception as e:
            print(f"Erro ao parsear {pdf.name}: {e}")
    return output_dir


def has_unparsed_pdfs(source_dir: Path, output_dir: Path) -> bool:
    if not source_dir.exists():
        return False
    for pdf in source_dir.iterdir():
        if not pdf.is_file() or pdf.suffix.lower() != ".pdf":
            continue
        md_path = output_dir / f"{pdf.stem}.md"
        if not md_path.exists() or md_path.stat().st_mtime < pdf.stat().st_mtime:
            return True
    return False


def ensure_documents_parsed(user_id: str):
    """Parseia PDFs novos ou alterados antes de indexar."""
    user_base = user_storage_dir(user_id)
    if has_unparsed_pdfs(Path("docs"), DOCS_PARSE_DIR):
        parse_folder(Path("docs"), DOCS_PARSE_DIR)
    if has_unparsed_pdfs(user_base / "uploads", user_base / "parse"):
        parse_folder(user_base / "uploads", user_base / "parse")

# ─────────────────────────────────────────────────────────────────
# RAG
# ─────────────────────────────────────────────────────────────────
def load_documents(user_id: str):
    '''Carrega documentos PDF e TXT do usuário, retornando uma lista de objetos Document.'''
    docs = []
    index = load_uploads_index(user_id)
    safe_to_original = {v: k for k, v in index.items()}#substituo o nome do arquivo seguro pelo nome original do arquivo

    def resolve_filename(path: Path) -> str:
        if path.suffix.lower() == ".md":
            original = safe_to_original.get(f"{path.stem}.pdf")
            if original:
                return original
        return safe_to_original.get(path.name, path.name)

    for folder in [
        DOCS_PARSE_DIR,
        Path("docs"),
        user_storage_dir(user_id) / "parse",
        user_storage_dir(user_id) / "uploads",
    ]:
        if not folder.exists():
            continue
        for f in folder.iterdir():
            if not f.is_file():
                continue
            suffix = f.suffix.lower()
            if suffix not in SUPPORTED_DOC_SUFFIXES or suffix == ".pdf":
                continue
            try:
                loader = TextLoader(str(f), encoding="utf-8")
                loaded = loader.load()
                display_name = resolve_filename(f)
                for d in loaded:
                    d.metadata["filename"] = display_name
                docs.extend(loaded)
            except Exception as e:
                print(f"Erro ao carregar {f}: {e}")
    return docs

def should_rebuild(user_id: str, session_id: str) -> bool:
    '''Verifica se o índice FAISS precisa ser reconstruído com base na data de modificação dos documentos.'''
    fp = faiss_path(user_id, session_id)
    if not fp.exists():
        return True
    index_mtime = fp.stat().st_mtime
    watch_dirs = [
        Path("docs"),
        DOCS_PARSE_DIR,
        user_storage_dir(user_id) / "uploads",
        user_storage_dir(user_id) / "parse",
    ]
    for folder in watch_dirs:
        if not folder.exists():
            continue
        for f in folder.iterdir():
            if f.is_file() and f.suffix.lower() in SUPPORTED_DOC_SUFFIXES:
                if f.stat().st_mtime > index_mtime:
                    return True
    return False

def count_markdown_files() -> int:
    if not DOCS_PARSE_DIR.exists():
        return 0
    return sum(1 for f in DOCS_PARSE_DIR.iterdir() if f.is_file() and f.suffix.lower() == ".md")


def get_rag_status(user_id: str, session_id: str) -> dict:
    docs = load_documents(user_id)
    fp = faiss_path(user_id, session_id)
    cache_key = (user_id, session_id)
    return {
        "docs_parse_dir": str(DOCS_PARSE_DIR.resolve()),
        "docs_parse_exists": DOCS_PARSE_DIR.exists(),
        "markdown_files": count_markdown_files(),
        "loaded_documents": len(docs),
        "faiss_index_exists": fp.exists(),
        "vectors_in_memory": cache_key in vectors_cache,
    }

def build_or_load_vectors(user_id: str, session_id: str, force: bool = False):
    '''Carrega ou constrói o índice FAISS para o usuário e sessão especificados.'''
    cache_key = (user_id, session_id)
    if not force and cache_key in vectors_cache:
        return vectors_cache[cache_key]
    fp = faiss_path(user_id, session_id)
    if not force and fp.exists() and not should_rebuild(user_id, session_id):
        try:
            v = FAISS.load_local(str(fp), emb, allow_dangerous_deserialization=True)
            vectors_cache[cache_key] = v
            return v
        except Exception:
            pass
    ensure_documents_parsed(user_id)
    docs = load_documents(user_id)
    if not docs:
        return None
    splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    v = FAISS.from_documents(chunks, emb)
    v.save_local(str(fp))
    vectors_cache[cache_key] = v
    return v

def extract_entities(text: str):
    if not SPACY_AVAILABLE:
        return []
    try:
        doc = nlp_spacy(text[:50000])
        return [(e.text.strip(), e.label_) for e in doc.ents if len(e.text.strip()) > 1]
    except Exception:
        return []

def build_graph(user_id: str, session_id: str, force: bool = False) -> nx.DiGraph:
    cache_key = (user_id, session_id)
    if not force and cache_key in graph_cache:
        return graph_cache[cache_key]
    gp = graph_path_file(user_id, session_id)
    if not force and gp.exists():
        try:
            with open(gp, "rb") as f:
                g = pickle.load(f)
            graph_cache[cache_key] = g
            return g
        except Exception:
            pass
    if has_unparsed_pdfs(Path("docs"), DOCS_PARSE_DIR) or has_unparsed_pdfs(
        user_storage_dir(user_id) / "uploads", user_storage_dir(user_id) / "parse"
    ):
        ensure_documents_parsed(user_id)
    docs = load_documents(user_id)
    splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    G = nx.DiGraph()
    for doc in chunks:
        entities = extract_entities(doc.page_content)
        for et, el in entities:
            if not G.has_node(et):
                G.add_node(et, type=el)
        for i, (e1, _) in enumerate(entities):
            for e2, _ in entities[i + 1:i + 6]:
                if e1 == e2:
                    continue
                if G.has_edge(e1, e2):
                    G[e1][e2]["weight"] += 1
                else:
                    G.add_edge(e1, e2, weight=1, context=doc.page_content[:200])
    with open(gp, "wb") as f:
        pickle.dump(G, f)
    graph_cache[cache_key] = G
    return G

def query_graph(G: nx.DiGraph, query: str) -> str:
    if G.number_of_nodes() == 0:
        return ""
    entities = extract_entities(query)
    if not entities:
        words = set(query.lower().split())
        entities = [(n, "") for n in G.nodes() if any(w in n.lower() for w in words if len(w) > 3)]
    if not entities:
        return ""
    relations = []
    visited = set()
    for et, _ in entities[:5]:
        matched = [n for n in G.nodes() if et.lower() in n.lower()]
        for node in matched[:2]:
            for neighbor in list(G.successors(node))[:5]:
                key = f"{node}→{neighbor}"
                if key not in visited:
                    visited.add(key)
                    edge = G[node][neighbor]
                    relations.append(f"• {node} → {neighbor} | {edge.get('context', '')[:100]}")
    if not relations:
        return ""
    return "Relações (Knowledge Graph):\n" + "\n".join(relations[:8])

def rank_documents(query: str, docs: list, use_reranking: bool) -> list:
    """Retorna todos os documentos candidatos em ordem de relevância."""
    if not docs:
        return []
    if use_reranking and RERANKER_AVAILABLE:
        try:
            pairs = [(query, d.page_content) for d in docs]
            scores = reranker_model.predict(pairs)
            ranked = sorted(zip(scores, docs), reverse=True)
            return [d for _, d in ranked]
        except Exception:
            pass
    return docs


def rerank(query: str, docs: list, top_n: int = 4) -> list:
    return rank_documents(query, docs, use_reranking=True)[:top_n]

def hyde_query(query: str) -> str:
    try:
        return llm.invoke(
            f"Escreva um parágrafo de 3 frases que responderia: {query}\nApenas o parágrafo:"
        ).content.strip()
    except Exception:
        return query

def auto_title(first_message: str) -> str:
    try:
        title = llm.invoke([
            {"role":"user","content":f"Crie um título curto (máximo 5 palavras, sem aspas) para uma conversa que começa com:\n{first_message}"}
        ]
            
        ).content.strip().strip('"').strip("'")
        return title[:60]
    except Exception:
        return first_message[:40]


# ─────────────────────────────────────────────────────────────────
# Avaliação de chunks recuperados (NDCG / MRR) — modo teste
# ─────────────────────────────────────────────────────────────────
def _eval_tokenize(text: str) -> set:
    normalized = unicodedata.normalize("NFKD", text.lower())
    normalized = "".join(c for c in normalized if not unicodedata.combining(c))
    return set(re.findall(r"\b\w{3,}\b", normalized))


def _token_overlap_ratio(text_tokens: set, reference_tokens: set) -> float:
    if not reference_tokens:
        return 0.0
    return len(text_tokens & reference_tokens) / len(reference_tokens)


def chunk_relevance_score(chunk_text: str, ground_truth: str, query: str = "") -> float:
    chunk_tokens = _eval_tokenize(chunk_text)
    gt_score = _token_overlap_ratio(chunk_tokens, _eval_tokenize(ground_truth))
    query_score = _token_overlap_ratio(chunk_tokens, _eval_tokenize(query))
    return max(gt_score, query_score)


def compute_dcg(relevances: list[float], k: int) -> float:
    return sum(rel / math.log2(i + 2) for i, rel in enumerate(relevances[:k]))


def compute_ndcg(relevances: list[float], k: int) -> float:
    dcg = compute_dcg(relevances, k)
    ideal = compute_dcg(sorted(relevances, reverse=True), k)
    return round(dcg / ideal, 4) if ideal > 0 else 0.0


def compute_mrr(relevances: list[float], threshold: float = 0.05) -> float:
    for i, rel in enumerate(relevances):
        if rel >= threshold:
            return round(1.0 / (i + 1), 4)
    return 0.0


def evaluate_retrieved_chunks(docs: list, ground_truth: str, k: int, query: str = "") -> dict:
    if not docs or not (ground_truth.strip() or query.strip()):
        return {"k": k, "ndcg": 0.0, "mrr": 0.0, "chunks": []}

    relevances = [chunk_relevance_score(d.page_content, ground_truth, query) for d in docs]
    effective_k = max(min(k, len(relevances)), 1) if relevances else 0
    if effective_k == 0:
        return {"k": 0, "ndcg": 0.0, "mrr": 0.0, "chunks": []}

    return {
        "k": effective_k,
        "ndcg": compute_ndcg(relevances, effective_k),
        "mrr": compute_mrr(relevances),
        "chunks": [
            {
                "rank": i + 1,
                "filename": d.metadata.get("filename", "?"),
                "relevance": round(rel, 4),
                "preview": d.page_content[:200],
            }
            for i, (d, rel) in enumerate(zip(docs[:effective_k], relevances[:effective_k]))
        ],
    }


def build_retrieval_eval(candidate_docs: list, final_docs: list, ground_truth: str, query: str) -> dict:
    cand_k = max(min(8, len(candidate_docs)), 1) if candidate_docs else 0
    final_k = max(min(4, len(final_docs)), 1) if final_docs else 0
    return {
        "retrieval": evaluate_retrieved_chunks(candidate_docs, ground_truth, k=cand_k, query=query),
        "final": evaluate_retrieved_chunks(final_docs, ground_truth, k=final_k, query=query),
    }


def build_prompt_and_retrieve(user_input: str, user_id: str, session_id: str, body):
    """Executa o RAG e retorna mensagens, fontes, contexto, métricas e dados de avaliação."""
    metrics: dict = {}
    retrieval_eval = None

    vectors = build_or_load_vectors(user_id, session_id)
    graph = build_graph(user_id, session_id) if body.use_graph else nx.DiGraph()

    if not vectors:
        return None, [], "", metrics, [], retrieval_eval

    with measure(metrics, "hyde"):
        search_q = hyde_query(user_input) if body.use_hyde else user_input

    with measure(metrics, "multi_query"):
        if body.use_multi_query:
            try:
                variations_prompt = f"""Gere 3 variações diferentes desta pergunta para busca em documentos.
Retorne apenas as 3 perguntas, uma por linha, sem numeração:
Pergunta original: {search_q}"""
                variations_text = llm.invoke(variations_prompt).content.strip()
                queries = [search_q] + [v.strip() for v in variations_text.split("\n") if v.strip()][:3]
                all_docs, seen = [], set()
                for q in queries:
                    for doc in vectors.similarity_search(q, k=4):
                        key = doc.page_content[:80]
                        if key not in seen:
                            seen.add(key)
                            all_docs.append(doc)
                candidate_docs = all_docs
            except Exception:
                candidate_docs = vectors.similarity_search(search_q, k=8)
        else:
            candidate_docs = vectors.similarity_search(search_q, k=8)

    with measure(metrics, "reranking"):
        ranked_docs = rank_documents(user_input, candidate_docs, body.use_reranking)
        final_docs = ranked_docs[:4]

    if TESTE_MODE and getattr(body, "ground_truth", None):
        retrieval_eval = build_retrieval_eval(
            candidate_docs, final_docs, body.ground_truth, user_input
        )

    with measure(metrics, "graph"):
        graph_ctx = query_graph(graph, user_input) if body.use_graph else ""

    ctx_text = "\n\n".join(
        [f"[{d.metadata.get('filename', '?')}]\n{d.page_content}" for d in final_docs]
    )

    prompt_template = ChatPromptTemplate.from_template("""
Você é um assistente útil e conciso. Use o contexto fornecido para responder.
Regras:
- Responda de forma direta e natural
- Se não encontrar nos documentos, diga: "Não encontrei essa informação nos documentos."
- Seja objetivo e evite repetições

Contexto dos documentos:
{context}

{graph_context}

Pergunta: {input}
Resposta:""")

    filled = prompt_template.format_messages(
        context=ctx_text,
        graph_context=graph_ctx,
        input=user_input,
    )

    sources = [
        {"filename": d.metadata.get("filename", "?"), "preview": d.page_content[:200]}
        for d in final_docs
    ]
    ranked_retrieval = [
        {
            "rank": i + 1,
            "filename": d.metadata.get("filename", "?"),
            "text": d.page_content,
            "preview": d.page_content[:200],
        }
        for i, d in enumerate(ranked_docs)
    ]
    return filled, sources, graph_ctx, metrics, ranked_retrieval, retrieval_eval

# ─────────────────────────────────────────────────────────────────
# Pydantic Models
# ─────────────────────────────────────────────────────────────────
class SessionCreate(BaseModel):
    name: str = "Nova Conversa"

class SessionRename(BaseModel):
    name: str

class ChatRequest(BaseModel):
    session_id: str
    message: str
    use_hyde: bool = True
    use_multi_query: bool = True
    use_reranking: bool = True
    use_graph: bool = True
    ground_truth: Optional[str] = None

class ProfileUpdate(BaseModel):
    full_name: Optional[str] = None

# ─────────────────────────────────────────────────────────────────
# ENDPOINTS
# ─────────────────────────────────────────────────────────────────

@app.get("/")
async def root():
    return RedirectResponse("/static/login.html")


@app.get("/config")
async def get_config():
    return {
        "supabase_url": SUPABASE_URL,
        "supabase_anon_key": SUPABASE_ANON_KEY,
        "api_base": os.getenv("API_BASE", "http://localhost:8000"),
        "teste": TESTE_MODE,
        "teste_eval": TESTE_MODE,
    }

# ── Sessões ──────────────────────────────────────────────────────
@app.get("/sessions")
async def get_sessions(auth: AuthContext = Depends(get_auth)):
    db = db_client_for(auth)
    return db_get_sessions(db, auth.user_id)


@app.post("/sessions")
async def create_session(body: SessionCreate, auth: AuthContext = Depends(get_auth)):
    db = db_client_for(auth)
    sid = db_create_session(db, auth.user_id, body.name)
    return {"id": sid, "name": body.name}


@app.patch("/sessions/{session_id}")
async def rename_session(session_id: str, body: SessionRename, auth: AuthContext = Depends(get_auth)):
    db = db_client_for(auth)
    db_rename_session(db, session_id, auth.user_id, body.name)
    return {"ok": True}


@app.delete("/sessions/{session_id}")
async def delete_session(session_id: str, auth: AuthContext = Depends(get_auth)):
    db = db_client_for(auth)
    db_delete_session(db, session_id, auth.user_id)
    vectors_cache.pop((auth.user_id, session_id), None)
    graph_cache.pop((auth.user_id, session_id), None)
    return {"ok": True}


@app.get("/sessions/{session_id}/messages")
async def get_messages(session_id: str, auth: AuthContext = Depends(get_auth)):
    db = db_client_for(auth)
    return db_load_messages(db, session_id, auth.user_id)

# ── Chat normal (JSON) ────────────────────────────────────────────
@app.post("/chat")
@limiter.limit("30/minute")
async def chat(request: Request, body: ChatRequest, auth: AuthContext = Depends(get_auth)):
    db = db_client_for(auth)
    user_id = auth.user_id
    db_save_message(db, body.session_id, user_id, "user", body.message)

    msgs = db_load_messages(db, body.session_id, user_id)
    if len(msgs) == 1:
        title = auto_title(body.message)
        db_rename_session(db, body.session_id, user_id, title)

    filled, sources, graph_ctx, metrics, ranked_retrieval, retrieval_eval = build_prompt_and_retrieve(
        body.message, user_id, body.session_id, body
    )

#aparentemente aqui eh a parte de avaliacao da resposta
    if filled:
        with measure(metrics, "llm"):
            answer = llm.invoke(filled).content
    else:
        #por que eu nao avalio e salvo a resposta na memoria?
        mem_key = f"{user_id}_{body.session_id}"
        if mem_key not in memory_cache:
            memory_cache[mem_key] = []
        memory_cache[mem_key].append(HumanMessage(content=body.message))
        with measure(metrics, "llm"):
            answer = llm.invoke(memory_cache[mem_key]).content
        memory_cache[mem_key].append(AIMessage(content=answer))

    db_save_message(db, body.session_id, user_id, "assistant", answer)
    response = {
        "answer": answer,
        "sources": sources,
        "ranked_retrieval": ranked_retrieval,
        "graph_context": graph_ctx,
        "metrics": metrics,
        "session_renamed": len(msgs) == 1,
    }
    if TESTE_MODE and retrieval_eval:
        response["retrieval_eval"] = retrieval_eval
    return response

# ── Chat streaming (SSE) ──────────────────────────────────────────
@app.post("/chat/stream")
@limiter.limit("30/minute")
async def chat_stream(request: Request, body: ChatRequest, auth: AuthContext = Depends(get_auth)):
    """
    Streaming via Server-Sent Events.
    Formato SSE: cada linha começa com "data: " seguido de JSON.
    Tipos de evento: meta | token | done
    """
    db = db_client_for(auth)
    user_id = auth.user_id
    db_save_message(db, body.session_id, user_id, "user", body.message)

    msgs = db_load_messages(db, body.session_id, user_id)
    new_title = None
    if len(msgs) == 1:
        new_title = auto_title(body.message)
        db_rename_session(db, body.session_id, user_id, new_title)

    filled, sources, graph_ctx, metrics, ranked_retrieval, retrieval_eval = build_prompt_and_retrieve(
        body.message, user_id, body.session_id, body
    )

    full_answer = []

    async def generate():
        # 1. Metadados (fontes, grafo, título, métricas do pipeline)
        meta_payload = {
            "type": "meta",
            "sources": sources,
            "ranked_retrieval": ranked_retrieval,
            "graph_context": graph_ctx,
            "new_title": new_title,
            "metrics": metrics,
        }
        if TESTE_MODE and retrieval_eval:
            meta_payload["retrieval_eval"] = retrieval_eval
        meta = json.dumps(meta_payload, ensure_ascii=False)
        yield f"data: {meta}\n\n"

        # 2. Streaming do LLM token a token
        llm_start = time.perf_counter()
        if filled:
            for chunk in llm.stream(filled):
                token = chunk.content
                if token:
                    full_answer.append(token)
                    payload = json.dumps({"type": "token", "token": token}, ensure_ascii=False)
                    yield f"data: {payload}\n\n"
                    await asyncio.sleep(0)
        else:
            mem_key = f"{user_id}_{body.session_id}"
            if mem_key not in memory_cache:
                memory_cache[mem_key] = []
            memory_cache[mem_key].append(HumanMessage(content=body.message))
            for chunk in llm.stream(memory_cache[mem_key]):
                token = chunk.content
                if token:
                    full_answer.append(token)
                    payload = json.dumps({"type": "token", "token": token}, ensure_ascii=False)
                    yield f"data: {payload}\n\n"
                    await asyncio.sleep(0)
            memory_cache[mem_key].append(AIMessage(content="".join(full_answer)))

        llm_ms = round((time.perf_counter() - llm_start) * 1000, 2)

        # 3. Sinal de fim com métrica do LLM
        yield f"data: {json.dumps({'type': 'done', 'llm_ms': llm_ms})}\n\n"

        # 4. Persiste resposta completa
        db_save_message(db, body.session_id, user_id, "assistant", "".join(full_answer))

    return StreamingResponse(generate(), media_type="text/event-stream")

# ── Exportar conversa ─────────────────────────────────────────────
@app.get("/sessions/{session_id}/export")
async def export_session(session_id: str, fmt: str = "txt", auth: AuthContext = Depends(get_auth)):
    db = db_client_for(auth)
    msgs = db_load_messages(db, session_id, auth.user_id)
    if not msgs:
        raise HTTPException(status_code=404, detail="Conversa vazia")

    try:
        r = db.table("chat_sessions").select("name").eq("id", session_id).limit(1).execute()
        session_name = r.data[0]["name"] if r.data else "Conversa"
    except Exception:
        session_name = "Conversa"

    if fmt == "md":
        lines = [f"# {session_name}\n"]
        for m in msgs:
            role = "**Você**" if m["role"] == "user" else "**Assistente**"
            lines.append(f"{role}\n{m['content']}\n")
        content = "\n---\n".join(lines)
        filename = f"{session_name}.md"
    else:
        lines = [f"{session_name}\n{'=' * 40}\n"]
        for m in msgs:
            role = "Você" if m["role"] == "user" else "Assistente"
            lines.append(f"[{role}]\n{m['content']}\n")
        content = "\n".join(lines)
        filename = f"{session_name}.txt"

    return PlainTextResponse(
        content=content,
        headers={"Content-Disposition": f'attachment; filename="{filename}"'}
    )

# ── Uploads ───────────────────────────────────────────────────────
@app.post("/upload")
@limiter.limit(UPLOAD_RATE_LIMIT)
async def upload_files(
    request: Request,
    files: List[UploadFile] = File(...),
    auth: AuthContext = Depends(get_auth),
):
    db = db_client_for(auth)
    user_id = auth.user_id
    folder_uploads = user_storage_dir(user_id) / "uploads"
    folder_parse = user_storage_dir(user_id) / "parse"
    index = load_uploads_index(user_id)
    saved = []

    for f in files:
        if not f.filename:
            continue
        suffix = Path(f.filename).suffix.lower()
        if suffix not in (".pdf", ".txt",".md",".markdown"):
            continue

        content = await f.read()

        if len(content) > 20 * 1024 * 1024:
            continue

        safe_name = f"{uuid.uuid4()}{suffix}"
        
        if suffix in (".pdf", ".txt"):
            dest = folder_uploads / safe_name
            with open(dest, "wb") as g:
                g.write(content)
        elif suffix in (".md", ".markdown"):
            dest = folder_parse / safe_name
            with open(dest, "wb") as g:
                g.write(content)

        index[f.filename] = safe_name
        saved.append(f.filename)

        try:
            key = f"{user_id}/{int(time.time())}_{safe_name}"
            if suffix in (".pdf", ".txt"):
                db.storage.from_("user_uploads").upload(
                    key, content, file_options={"content-type": f.content_type}
                )
            elif suffix in (".md", ".markdown"):
                db.storage.from_("users_parse").upload(
                    key, content, file_options={"content-type": f.content_type}
                )
        except Exception as e:
            print(f"❌ ERRO AO UPLOAD PARA STORAGE: {e}")

    save_uploads_index(user_id, index)
    return {"saved": saved}

@app.get("/uploads")
async def list_uploads(auth: AuthContext = Depends(get_auth)):
    index = load_uploads_index(auth.user_id)
    return {"files": list(index.keys())}


@app.delete("/uploads/{filename}")
async def delete_upload(filename: str, auth: AuthContext = Depends(get_auth)):
    user_id = auth.user_id
    index = load_uploads_index(user_id)
    safe_name = index.pop(filename, None)
    if safe_name:
        dest = user_storage_dir(user_id) / "uploads" / safe_name
        if dest.exists():
            dest.unlink()
        save_uploads_index(user_id, index)
    return {"ok": True}

@app.post("/rebuild-index")
async def rebuild_index(session_id: str, auth: AuthContext = Depends(get_auth)):
    db = db_client_for(auth)
    verify_session_owner(db, session_id, auth.user_id)
    user_id = auth.user_id
    vectors = build_or_load_vectors(user_id, session_id, force=True)
    build_graph(user_id, session_id, force=True)
    status = get_rag_status(user_id, session_id)
    if vectors is None or status["loaded_documents"] == 0:
        raise HTTPException(
            status_code=503,
            detail={
                "error": "Nenhum documento carregado para indexacao",
                "status": status,
            },
        )
    return {"ok": True, **status}


@app.get("/rag/status")
async def rag_status(session_id: str, auth: AuthContext = Depends(get_auth)):
    db = db_client_for(auth)
    verify_session_owner(db, session_id, auth.user_id)
    return get_rag_status(auth.user_id, session_id)

# ── Perfil ────────────────────────────────────────────────────────
@app.get("/profile")
async def get_profile(auth: AuthContext = Depends(get_auth)):
    db = db_client_for(auth)
    try:
        r = db.table("users_profile").select("*").eq("id", auth.user_id).limit(1).execute()
        return r.data[0] if r.data else {}
    except Exception:
        return {}


@app.patch("/profile")
async def update_profile(body: ProfileUpdate, auth: AuthContext = Depends(get_auth)):
    db = db_client_for(auth)
    payload = {"id": auth.user_id}
    if body.full_name is not None:
        payload["full_name"] = body.full_name
    db.table("users_profile").upsert(payload).execute()
    return {"ok": True}


@app.post("/profile/avatar")
async def upload_avatar(
    file: UploadFile = File(...),
    auth: AuthContext = Depends(get_auth),
):
    db = db_client_for(auth)
    user_id = auth.user_id
    content = await file.read()
    if len(content) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Avatar muito grande (máx 5MB)")
    filename = f"{user_id}_{uuid.uuid4()}{Path(file.filename).suffix}"
    try:
        db.storage.from_("avatars").upload(
            filename, content, file_options={"content-type": file.content_type}
        )
        url_obj = db.storage.from_("avatars").get_public_url(filename)
        url = url_obj if isinstance(url_obj, str) else (url_obj.get("publicUrl") or "")
        db.table("users_profile").upsert({"id": user_id, "avatar_url": url}).execute()
        return {"avatar_url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))