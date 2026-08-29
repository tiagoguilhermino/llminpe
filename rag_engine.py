import json
import os
import pickle
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import networkx as nx
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from llama_cloud import LlamaCloud

ENV_FILE = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=ENV_FILE, override=True)

USER_ID = "local_demo"
BASE_DIR = Path("user_data") / USER_ID
DOCUMENTS_DIR = Path("docs")
PUBLIC_PARSE_DIR = DOCUMENTS_DIR / "parse"
PARSE_DIR = BASE_DIR / "parse"
UPLOADS_DIR = BASE_DIR / "uploads"
RESULTS_DIR = BASE_DIR / "results"
INDEX_DIR = BASE_DIR / "faiss_index"
GRAPH_FILE = BASE_DIR / "knowledge_graph.pkl"
UPLOADS_INDEX_FILE = BASE_DIR / "uploads_index.json"
SUPPORTED_SUFFIXES = {".pdf", ".txt", ".md", ".markdown"}


@dataclass(frozen=True)
class RagOptions:
    use_hyde: bool = True
    use_multi_query: bool = True
    use_reranking: bool = True
    use_graph: bool = True


def _ensure_directories() -> None:
    for directory in (BASE_DIR, PARSE_DIR, UPLOADS_DIR, RESULTS_DIR):
        directory.mkdir(parents=True, exist_ok=True)


def _build_models() -> tuple[Any, Any]:
    api_key = os.getenv("NVIDIA_API_KEY")
    embedding_key = os.getenv("OPENAI_EMBEDDING_MODEL_KEY")
    if not api_key:
        raise RuntimeError("Configure NVIDIA_API_KEY no arquivo .env")
    model = os.getenv("NVIDIA_MODEL", "meta/llama-3.1-8b-instruct").strip()
    embedding_model = os.getenv(
        "OPENAI_EMBEDDING_MODEL", "nvidia/nv-embedqa-e5-v5"
    ).strip()
    timeout = int(os.getenv("NVIDIA_TIMEOUT", "120"))
    max_tokens = int(os.getenv("NVIDIA_MAX_COMPLETION_TOKENS", "16384"))
    llm = ChatNVIDIA(
        model=model,
        api_key=api_key,
        temperature=0.5,
        max_completion_tokens=max_tokens,
        timeout=timeout,
    )
    
    
    embeddings   = OpenAIEmbeddings(model=embedding_model, openai_api_key=embedding_key)
    return llm, embeddings


llm: Any = None
embeddings: Any = None
vectors_cache: Any = None
graph_cache: nx.DiGraph | None = None


def _models() -> tuple[Any, Any]:
    global llm, embeddings
    if llm is None or embeddings is None:
        llm, embeddings = _build_models()
    return llm, embeddings

try:
    import spacy

    nlp = spacy.load("pt_core_news_sm")
except Exception:
    nlp = None

try:
    from sentence_transformers import CrossEncoder

    reranker = CrossEncoder("bert-base-portuguese-cased")
except Exception:
    reranker = None


def _load_upload_index() -> dict[str, str]:
    if not UPLOADS_INDEX_FILE.exists():
        return {}
    try:
        value = json.loads(UPLOADS_INDEX_FILE.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def _save_upload_index(index: dict[str, str]) -> None:
    UPLOADS_INDEX_FILE.write_text(
        json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def add_documents(paths: list[Path]) -> list[str]:
    """Copia documentos para o armazenamento local sem upload HTTP."""
    _ensure_directories()
    index = _load_upload_index()
    saved = []
    for source in paths:
        if not source.is_file() or source.suffix.lower() not in SUPPORTED_SUFFIXES:
            continue
        destination = UPLOADS_DIR / source.name
        destination.write_bytes(source.read_bytes())
        index[source.name] = source.name
        saved.append(source.name)
    _save_upload_index(index)
    return saved


def parse_pdfs() -> int:
    """Converte PDFs locais com LlamaParse e preserva os Markdown gerados."""
    _ensure_directories()
    pdf_targets = [
        *[(pdf, PUBLIC_PARSE_DIR / f"{pdf.stem}.md") for pdf in DOCUMENTS_DIR.glob("*.pdf")],
        *[(pdf, PARSE_DIR / f"{pdf.stem}.md") for pdf in UPLOADS_DIR.glob("*.pdf")],
    ]
    pending = [
        (pdf, target) for pdf, target in pdf_targets
        if not target.exists() or target.stat().st_mtime < pdf.stat().st_mtime
    ]
    if not pending:
        return 0
    api_key = os.getenv("LLAMA_CLOUD_API_KEY")
    if not api_key:
        raise RuntimeError(
            f"{len(pending)} PDF(s) precisam de parse. Configure LLAMA_CLOUD_API_KEY."
        )
    client = LlamaCloud(api_key=api_key)
    parsed = 0
    for pdf, target in pending:
        target.parent.mkdir(parents=True, exist_ok=True)
        print(f"  Parseando {pdf.name} com LlamaParse...")
        uploaded = client.files.create(file=pdf, purpose="parse")
        result = client.parsing.parse(
            file_id=uploaded.id,
            tier="agentic",
            version="latest",
            expand=["markdown_full"],
        )
        target.write_text(result.markdown_full or "", encoding="utf-8")
        parsed += 1
    return parsed


def _documents():
    _ensure_directories()
    parse_pdfs()
    upload_index = _load_upload_index()
    reverse_index = {value: key for key, value in upload_index.items()}
    documents = []
    folders = (PUBLIC_PARSE_DIR, PARSE_DIR, DOCUMENTS_DIR, UPLOADS_DIR)
    for folder in folders:
        for path in sorted(folder.iterdir()):
            if not path.is_file() or path.suffix.lower() not in {".txt", ".md", ".markdown"}:
                continue
            try:
                loaded = TextLoader(str(path), encoding="utf-8").load()
            except Exception as exc:
                print(f"  Ignorando {path}: {exc}")
                continue
            filename = reverse_index.get(path.name, path.name)
            if path.suffix.lower() == ".md":
                filename = reverse_index.get(f"{path.stem}.pdf", filename)
            for document in loaded:
                document.metadata["filename"] = filename
            documents.extend(loaded)
    return documents


def _source_mtime() -> float:
    paths = [path for folder in (DOCUMENTS_DIR, PUBLIC_PARSE_DIR, PARSE_DIR, UPLOADS_DIR) if folder.exists() for path in folder.iterdir() if path.is_file()]
    return max((path.stat().st_mtime for path in paths), default=0.0)


def build_or_load_vectors(force: bool = False):
    global vectors_cache
    _, current_embeddings = _models()
    if vectors_cache is not None and not force:
        return vectors_cache
    marker = INDEX_DIR / "index.faiss"
    if not force and marker.exists() and marker.stat().st_mtime >= _source_mtime():
        vectors_cache = FAISS.load_local(str(INDEX_DIR), current_embeddings, allow_dangerous_deserialization=True)
        return vectors_cache
    documents = _documents()
    if not documents:
        return None
    chunks = RecursiveCharacterTextSplitter.from_language(language="markdown",chunk_size=400, chunk_overlap=50).split_documents(documents)
    vectors_cache = FAISS.from_documents(chunks, current_embeddings)
    vectors_cache.save_local(str(INDEX_DIR))
    return vectors_cache


def _entities(text: str):
    if nlp is None:
        return []
    return [(entity.text.strip(), entity.label_) for entity in nlp(text[:50000]).ents if len(entity.text.strip()) > 1]


def build_graph(force: bool = False) -> nx.DiGraph:
    global graph_cache
    if graph_cache is not None and not force:
        return graph_cache
    if GRAPH_FILE.exists() and not force and GRAPH_FILE.stat().st_mtime >= _source_mtime():
        with GRAPH_FILE.open("rb") as handle:
            graph_cache = pickle.load(handle)
        return graph_cache
    graph = nx.DiGraph()
    for document in RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50).split_documents(_documents()):
        entities = _entities(document.page_content)
        for name, label in entities:
            graph.add_node(name, type=label)
        for index, (first, _) in enumerate(entities):
            for second, _ in entities[index + 1:index + 6]:
                if first != second:
                    graph.add_edge(first, second, weight=graph.get_edge_data(first, second, {}).get("weight", 0) + 1, context=document.page_content[:200])
    with GRAPH_FILE.open("wb") as handle:
        pickle.dump(graph, handle)
    graph_cache = graph
    return graph


def _graph_context(graph: nx.DiGraph, query: str) -> str:
    names = [name for name, _ in _entities(query)]
    if not names:
        words = {word.lower() for word in query.split() if len(word) > 3}
        names = [node for node in graph.nodes if any(word in node.lower() for word in words)]
    relations = []
    for name in names[:5]:
        for node in [node for node in graph.nodes if name.lower() in node.lower()][:2]:
            for neighbor in list(graph.successors(node))[:5]:
                edge = graph[node][neighbor]
                relations.append(f"{node} -> {neighbor} | {edge.get('context', '')[:100]}")
    return "Relações (Knowledge Graph):\n" + "\n".join(relations[:8]) if relations else ""


def _rank(query: str, documents: list, use_reranking: bool) -> list:
    if not documents or not use_reranking or reranker is None:
        return documents
    try:
        scores = reranker.predict([(query, document.page_content) for document in documents])
        return [document for _, document in sorted(zip(scores, documents), reverse=True)]
    except Exception:
        return documents


def _hyde(query: str) -> str:
    try:
        return _invoke_llm(
            f"Escreva um parágrafo de 3 frases que responderia: {query}\nApenas o parágrafo:"
        ).content.strip()
    except Exception as exc:
        print(f"  HyDE falhou: {type(exc).__name__}: {exc}")
        raise


def _is_transient_error(error: Exception) -> bool:
    error_name = type(error).__name__.lower()
    error_text = str(error).lower()
    return any(
        marker in error_name or marker in error_text
        for marker in ("timeout", "connecterror", "connection reset", "temporarily unavailable")
    )


def _invoke_llm(prompt: Any):
    current_llm, _ = _models()
    attempts = max(1, int(os.getenv("NVIDIA_RETRY_ATTEMPTS", "2")))
    delay = float(os.getenv("NVIDIA_RETRY_DELAY", "5"))
    for attempt in range(1, attempts + 1):
        try:
            return current_llm.invoke(prompt)
        except Exception as error:
            if not _is_transient_error(error) or attempt == attempts:
                raise
            print(
                f"  NVIDIA demorou ou perdeu a conexão; nova tentativa "
                f"{attempt + 1}/{attempts} em {delay:g}s..."
            )
            time.sleep(delay)

def similarity_search_with_retry(vectors, query: str, k: int = 4):
    attempts = 3

    for attempt in range(1, attempts + 1):
        try:
            return vectors.similarity_search(query, k=k)
        except Exception as exc:
            if attempt == attempts or not _is_transient_error(exc):
                raise

            print(f"  Embedding indisponível; tentativa {attempt + 1}/{attempts}")
            time.sleep(5)
            
def answer_question(query: str, options: RagOptions) -> dict:
    metrics = {}
    vectors = build_or_load_vectors()
    if vectors is None:
        return {"answer": "Nenhum documento disponível para consulta.", "sources": [], "ranked_retrieval": [], "metrics": metrics}
    started = time.perf_counter()
    graph = build_graph() if options.use_graph else nx.DiGraph()
    metrics["graph"] = round((time.perf_counter() - started), 2)
    search_query = _hyde(query) if options.use_hyde else query
    metrics["hyde"] = round((time.perf_counter() - started), 2)
    queries = [search_query]
    if options.use_multi_query:
        time.sleep(0.5) # tempo pra API do NVIDIA não reclamar de muitas requisições
        text = _invoke_llm(
            f"Gere 3 variações desta pergunta, uma por linha, sem numeração:\n{search_query}"
        ).content
        queries.extend(line.strip() for line in text.splitlines() if line.strip())
        metrics["multi_query"] = round((time.perf_counter() - started), 2)
    candidates, seen = [], set()
    for current_query in queries[:4]:
        for document in similarity_search_with_retry(vectors, current_query, k=4):
            key = document.page_content[:100]
            if key not in seen:
                seen.add(key)
                candidates.append(document)
    ranked = _rank(query, candidates, options.use_reranking)
    if options.use_reranking:
        metrics["rerank"] = round((time.perf_counter() - started), 2)
    final_documents = ranked[:4]
    context = "\n\n".join(f"[{doc.metadata.get('filename', '?')}]\n{doc.page_content}" for doc in final_documents)
    prompt = ChatPromptTemplate.from_template("""
Você é um assistente útil e conciso. Use o contexto fornecido para responder.
Se não encontrar nos documentos, diga: "Não encontrei essa informação nos documentos."

Contexto dos documentos:
{context}

{graph_context}

Pergunta: {input}
Resposta:
""").format_messages(context=context, graph_context=_graph_context(graph, query), input=query)
    llm_started = time.perf_counter()
    answer = _invoke_llm(prompt).content
    metrics["llm"] = round((time.perf_counter() - llm_started), 2)
    return {
        "answer": answer,
        "sources": [{"filename": doc.metadata.get("filename", "?"), "preview": doc.page_content[:200]} for doc in final_documents],
        "ranked_retrieval": [{"rank": index, "filename": doc.metadata.get("filename", "?"), "text": doc.page_content, "preview": doc.page_content[:200]} for index, doc in enumerate(ranked, 1)],
        "metrics": metrics,
    }


def rebuild_index() -> dict:
    global vectors_cache, graph_cache
    vectors_cache = None
    graph_cache = None
    vectors = build_or_load_vectors(force=True)
    graph = build_graph(force=True)
    return {"loaded_documents": len(_documents()), "faiss_index_exists": vectors is not None, "graph_nodes": graph.number_of_nodes()}