"""文本嵌入 — 默认 DashScope text-embedding-v3（1024 dim, 与 pgvector schema 对齐）。

支持聚合端点：LLM_BASE_URL + LLM_API_KEY 设置时优先用。
"""
import os

from openai import OpenAI

DASHSCOPE_DEFAULT = "https://dashscope.aliyuncs.com/compatible-mode/v1"
EMBED_MODEL_DEFAULT = "text-embedding-v3"
EMBED_DIM = 1024


def _client_and_model() -> tuple[OpenAI, str]:
    if os.getenv("LLM_BASE_URL") and os.getenv("LLM_API_KEY"):
        base = os.environ["LLM_BASE_URL"]
        key = os.environ["LLM_API_KEY"]
    else:
        base = os.getenv("EMBEDDING_BASE_URL") or DASHSCOPE_DEFAULT
        key = os.environ["QWEN_API_KEY"]
    model = os.getenv("EMBEDDING_MODEL") or EMBED_MODEL_DEFAULT
    return OpenAI(api_key=key, base_url=base), model


def embed_text(text: str) -> list[float]:
    if not text or not text.strip():
        return [0.0] * EMBED_DIM
    client, model = _client_and_model()
    resp = client.embeddings.create(model=model, input=text, dimensions=EMBED_DIM)
    return resp.data[0].embedding


def embed_batch(texts: list[str]) -> list[list[float]]:
    if not texts:
        return []
    cleaned = [t if (t and t.strip()) else " " for t in texts]
    client, model = _client_and_model()
    resp = client.embeddings.create(model=model, input=cleaned, dimensions=EMBED_DIM)
    return [d.embedding for d in resp.data]
