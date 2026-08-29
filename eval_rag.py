"""Ponto de entrada legado para o benchmark RAG local.

Uso:
    python eval_rag.py --limit 1
    python eval_rag.py --rebuild
"""

from eval_local import main


if __name__ == "__main__":
    raise SystemExit(main())
