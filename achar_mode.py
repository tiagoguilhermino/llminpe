from rag_engine import _models

_, embeddings = _models()

for model in embeddings.available_models:
    print(model.id, getattr(model, "deprecated", False))