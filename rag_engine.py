import json
import os
import pickle
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any


import networkx as nx
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
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

_CHUNK_SIZE = 1200
_CHUNK_OVERLAP = 150
_MIN_CHUNK_CHARS = 80
_HEADER_KEYS = ("h1", "h2", "h3")
_KEEP_WHOLE_TITLES = re.compile(
    r"^(abstract|plain language summary|resumo)\b",
    re.IGNORECASE,
)
_SKIP_SECTION_TITLES = re.compile(
    r"^(references|bibliography|referências|bibliografia)\b",
    re.IGNORECASE,
)
_SPECIAL_TITLES = (
    "Abstract",
    "Plain Language Summary",
    "Resumo",
)
_SPECIAL_TITLE_ALT = "|".join(re.escape(title) for title in _SPECIAL_TITLES)
_SPECIAL_HEADING_RE = re.compile(
    rf"^(?:(?P<hashes>\#{{1,3}})\s+|\*\*)(?P<title>{_SPECIAL_TITLE_ALT})(?:\*\*)?[ \t]*",
    re.IGNORECASE | re.MULTILINE,
)
_SPECIAL_BOUNDARY_RE = re.compile(
    rf"^(?:\#{{1,3}}\s+\S|\*\*(?:{_SPECIAL_TITLE_ALT}|Keywords|Index Terms)\*\*)",
    re.IGNORECASE | re.MULTILINE,
)
_REFERENCE_HEADING_RE = re.compile(
    r"^(#{1,3}\s+|\*\*)(References|Bibliography|Referências|Bibliografia)(\*\*)?\s*$",
    re.IGNORECASE | re.MULTILINE,
)
_APPENDIX_HEADING_RE = re.compile(
    r"^(#{1,3}\s+)(appendix|supplementary|supporting information)\b",
    re.IGNORECASE | re.MULTILINE,
)
_ATOMIC_BLOCK_RE = re.compile(
    r"(```[\s\S]*?```|\$\$[\s\S]*?\$\$|<table\b[\s\S]*?</table>|(?:^[ \t]*\|.+\|[ \t]*(?:\n|$))+)",
    re.IGNORECASE | re.MULTILINE,
)


def _collapse_blank_lines(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _clean_llamaparse_artifacts(text: str) -> str:
    cleaned = text
    cleaned = re.sub(r"(?im)^.*Downloaded from https?://\S+.*$", "", cleaned)
    cleaned = re.sub(r"(?m)^\s*---\s*$", "", cleaned)
    cleaned = re.sub(r"(?m)^\d+\s+of\s+\d+\s*$", "", cleaned)
    cleaned = re.sub(r"(?m)^\d{1,3}(?:,\d{3})+\s*$", "", cleaned)
    cleaned = re.sub(r"(?m)^\d{5,6}\s*$", "", cleaned)
    cleaned = re.sub(r"(?im)^Check for updates(?: icon)?\s*$", "", cleaned)
    cleaned = re.sub(
        r"(?m)^[A-Z][A-Z’'\-]+(?:\s+[A-Z][A-Z’'\-]+){0,5}\s+ET AL\.\s*$",
        "",
        cleaned,
    )
    cleaned = re.sub(r"(?m)^.+ et al\.:.+$", "", cleaned)
    cleaned = re.sub(r"(?im)^©\s*\d{4}\b.*$", "", cleaned)
    cleaned = re.sub(r"(?im)^This is an open access article.*$", "", cleaned)
    cleaned = re.sub(r"(?im)^.*\bAll Rights Reserved\.?\s*$", "", cleaned)
    cleaned = re.sub(r"(?m)^10\.\d{4,}/\S+\s*$", "", cleaned)
    cleaned = re.sub(r"(?im)^VOLUME \d+,\s*\d{4}\s*$", "", cleaned)
    cleaned = re.sub(r"(?im)^The associate editor coordinating.*$", "", cleaned)
    cleaned = re.sub(r"(?im)^.*\blogo\s*$", "", cleaned)
    cleaned = re.sub(r"(?im)^Digital Object Identifier\s+\S+\s*$", "", cleaned)
    return _drop_repeated_running_headers(_collapse_blank_lines(cleaned))


def _drop_repeated_running_headers(text: str) -> str:
    seen: set[tuple[str, str]] = set()
    kept: list[str] = []
    for line in text.splitlines():
        match = re.match(r"^(#{1,3})\s+(.+?)\s*$", line)
        if match:
            level, title = match.group(1), match.group(2).strip()
            key = (level, title.casefold())
            numbered = bool(re.match(r"^\d", title))
            if level == "#" and not numbered and key in seen:
                continue
            seen.add(key)
        kept.append(line)
    return "\n".join(kept)


def _normalize_section_title(title: str) -> str:
    stripped = re.sub(r"^#+\s*", "", title).strip()
    if _KEEP_WHOLE_TITLES.match(stripped):
        return stripped.title()
    return stripped


def _extract_labeled_sections(text: str) -> tuple[list[tuple[str, str]], str]:
    spans: list[tuple[int, int, str]] = []
    for match in _SPECIAL_HEADING_RE.finditer(text):
        body_start = match.end()
        boundary = _SPECIAL_BOUNDARY_RE.search(text, body_start)
        end = boundary.start() if boundary else len(text)
        if end <= body_start:
            continue
        spans.append((match.start(), end, match.group("title")))

    extracted: list[tuple[str, str]] = []
    remaining = text
    for start, end, title in sorted(spans, reverse=True):
        body = text[start:end]
        remaining = remaining[:start] + remaining[end:]
        extracted.append((_normalize_section_title(title), body.strip()))
    extracted.reverse()
    return extracted, _collapse_blank_lines(remaining)


def _drop_reference_sections(text: str) -> str:
    matches = list(_REFERENCE_HEADING_RE.finditer(text))
    if not matches:
        return text
    start = matches[-1].start()
    tail = text[start:]
    appendix = _APPENDIX_HEADING_RE.search(tail)
    if appendix and appendix.start() > 0:
        return _collapse_blank_lines(text[:start] + tail[appendix.start():])
    return _collapse_blank_lines(text[:start])


def _heading_values(metadata: dict[str, Any]) -> list[str]:
    values = []
    for key in _HEADER_KEYS:
        value = metadata.get(key)
        if isinstance(value, str) and value.strip():
            values.append(_normalize_section_title(value))
    return values


def _section_path(metadata: dict[str, Any]) -> str:
    return " > ".join(_heading_values(metadata))


def _matches_heading(metadata: dict[str, Any], pattern: re.Pattern[str]) -> bool:
    return any(pattern.search(value) for value in _heading_values(metadata))


def _prefix_section(text: str, path: str) -> str:
    if not path:
        return text
    marker = f"[{path}]"
    if text.startswith(marker):
        return text
    return f"{marker}\n{text}"


def _is_keepable_chunk(text: str) -> bool:
    if _is_atomic_block(text) or "```" in text or "$$" in text or "<table" in text.lower():
        return True
    body = re.sub(r"^\[.*?\]\n", "", text, count=1).strip()
    return len(body) >= _MIN_CHUNK_CHARS


def _is_atomic_block(text: str) -> bool:
    stripped = text.lstrip()
    return (
        stripped.startswith("```")
        or stripped.startswith("$$")
        or stripped.lower().startswith("<table")
        or stripped.startswith("|")
    )


def _split_preserving_atomic_blocks(text: str, splitter: RecursiveCharacterTextSplitter) -> list[str]:
    if not text.strip():
        return []
    parts = _ATOMIC_BLOCK_RE.split(text)
    chunks: list[str] = []
    prose_parts: list[str] = []

    def flush_prose() -> None:
        joined = "".join(prose_parts).strip()
        prose_parts.clear()
        if joined:
            chunks.extend(splitter.split_text(joined))

    for part in parts:
        if not part:
            continue
        if _is_atomic_block(part):
            flush_prose()
            block = part.strip()
            if chunks and len(chunks[-1]) + len(block) + 2 <= _CHUNK_SIZE:
                chunks[-1] = f"{chunks[-1]}\n\n{block}"
            else:
                chunks.append(block)
        else:
            prose_parts.append(part)
    flush_prose()
    return [chunk for chunk in chunks if chunk.strip()]


def split_markdown_documents(documents):
    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "h1"),
            ("##", "h2"),
            ("###", "h3"),
        ],
        strip_headers=True,
    )
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=_CHUNK_SIZE,
        chunk_overlap=_CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""],
        keep_separator=True,
    )

    chunks: list[Document] = []
    for document in documents:
        cleaned = _clean_llamaparse_artifacts(document.page_content)
        special_sections, remaining = _extract_labeled_sections(cleaned)
        remaining = _drop_reference_sections(remaining)

        for title, body in special_sections:
            if not body:
                continue
            special_metadata = {**document.metadata, "h1": title}
            content = _prefix_section(body, title)
            if _is_keepable_chunk(content):
                chunks.append(Document(page_content=content, metadata=special_metadata))

        if remaining:
            header_documents = header_splitter.split_text(remaining)
        else:
            header_documents = []

        for section in header_documents:
            section.metadata.update(document.metadata)
            if _matches_heading(section.metadata, _SKIP_SECTION_TITLES):
                continue
            path = _section_path(section.metadata)
            if _matches_heading(section.metadata, _KEEP_WHOLE_TITLES):
                pieces = [section.page_content]
            else:
                pieces = _split_preserving_atomic_blocks(section.page_content, text_splitter)
            for piece in pieces:
                content = _prefix_section(piece.strip(), path)
                if _is_keepable_chunk(content):
                    chunks.append(
                        Document(page_content=content, metadata=dict(section.metadata))
                    )
    return chunks

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
    chunks = split_markdown_documents(documents)
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
    for document in split_markdown_documents(_documents()):
        entities = _entities(document.page_content)
        for name, label in entities:
            # Adiciona o nó ao grafo com o rótulo como atributo
            graph.add_node(name, type=label)
        for index, (first, _) in enumerate(entities):
            # Adiciona arestas para os próximos 5 nomes diferentes encontrados
            for second, _ in entities[index + 1:index + 6]:
                # Adiciona uma aresta direcionada do primeiro para o segundo nó, incrementando o peso se a aresta já existir
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
        # Adiciona as relações do nó correspondente à consulta
        for node in [node for node in graph.nodes if name.lower() in node.lower()][:2]:
            # Adiciona as relações do nó encontrado
            for neighbor in list(graph.successors(node))[:5]:
                # Adiciona a relação do nó para o vizinho, incluindo o contexto da aresta
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
    for query_index, current_query in enumerate(queries[:4]):
        origem = "hyde" if options.use_hyde and query_index == 0 else (
            "multi_query" if query_index > 0 else "faiss"
        )
        for position, document in enumerate(similarity_search_with_retry(vectors, current_query, k=4), 1):
            key = document.page_content[:100]
            if key not in seen:
                seen.add(key)
                document.metadata = dict(document.metadata)
                document.metadata["origem"] = origem
                document.metadata["posicao_busca"] = position
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
    ranked_retrieval = [
        {
            "rank": index,
            "posicao": index,
            "origem": doc.metadata.get("origem", "faiss"),
            "posicao_busca": doc.metadata.get("posicao_busca"),
            "filename": doc.metadata.get("filename", "?"),
            "text": doc.page_content,
            "preview": doc.page_content[:200],
        }
        for index, doc in enumerate(ranked, 1)
    ]
    return {
        "answer": answer,
        "sources": [{"filename": doc.metadata.get("filename", "?"), "preview": doc.page_content[:200]} for doc in final_documents],
        "ranked_retrieval": ranked_retrieval,
        "metrics": metrics,
    }


def rebuild_index() -> dict:
    global vectors_cache, graph_cache
    vectors_cache = None
    graph_cache = None
    vectors = build_or_load_vectors(force=True)
    graph = build_graph(force=True)
    return {"loaded_documents": len(_documents()), "faiss_index_exists": vectors is not None, "graph_nodes": graph.number_of_nodes()}