"""Converte PDFs de docs/ para Markdown em docs/parse/ via LlamaParse.

Execute antes do eval_rag.py na primeira vez (ou quando adicionar PDFs):
    python preparse_docs.py
"""
import os
from pathlib import Path

from dotenv import load_dotenv
from llama_cloud import LlamaCloud

load_dotenv()

DOCS_DIR = Path("docs")
PARSE_DIR = DOCS_DIR / "parse"


def parse_folder(source_dir: Path, output_dir: Path) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    if not source_dir.exists():
        print(f"Pasta nao encontrada: {source_dir}")
        return 0

    api_key = os.environ.get("LLAMA_CLOUD_API_KEY")
    if not api_key:
        raise RuntimeError("Configure LLAMA_CLOUD_API_KEY no .env")

    client = LlamaCloud(api_key=api_key)
    parsed = 0
    pdfs = sorted(p for p in source_dir.iterdir() if p.is_file() and p.suffix.lower() == ".pdf")
    if not pdfs:
        print(f"Nenhum PDF em {source_dir}")
        return 0

    for i, pdf in enumerate(pdfs, start=1):
        md_path = output_dir / f"{pdf.stem}.md"
        if md_path.exists() and md_path.stat().st_mtime >= pdf.stat().st_mtime:
            print(f"[{i}/{len(pdfs)}] OK (cache): {pdf.name}")
            continue
        print(f"[{i}/{len(pdfs)}] Parseando: {pdf.name} ...")
        try:
            arquivo = client.files.create(file=pdf, purpose="parse")
            result = client.parsing.parse(
                file_id=arquivo.id,
                tier="agentic",
                version="latest",
                expand=["markdown_full"],
            )
            md_path.write_text(result.markdown_full or "", encoding="utf-8")
            parsed += 1
            print(f"         -> {md_path.name}")
        except Exception as exc:
            print(f"         ERRO: {exc}")
    return parsed


if __name__ == "__main__":
    n = parse_folder(DOCS_DIR, PARSE_DIR)
    total_md = len(list(PARSE_DIR.glob("*.md")))
    print(f"\nConcluido: {n} PDF(s) convertido(s) agora; {total_md} Markdown(s) em {PARSE_DIR}/")
