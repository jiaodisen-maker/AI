"""文本嵌入 — 用 DashScope text-embedding-v3（1024 dim, 与 pgvector schema 对齐）。

替代方案：bge-large-zh-v1.5（本地，sentence-transformers），但占内存。MVP 默认走 API。
"""
import os

from openai import OpenAI

DASHSCOPE_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
EMBED_MODEL = "text-embedding-v3"
EMBED_DIM = 1024


def embed_text(text: str) -> list[float]:
    if not text or not text.strip():
        return [0.0] * EMBED_DIM
    client = OpenAI(api_key=os.environ["QWEN_API_KEY"], base_url=DASHSCOPE_BASE_URL)
    resp = client.embeddings.create(model=EMBED_MODEL, input=text, dimensions=EMBED_DIM)
    return resp.data[0].embedding


def embed_batch(texts: list[str]) -> list[list[float]]:
    if not texts:
        return []
    cleaned = [t if (t and t.strip()) else " " for t in texts]
    client = OpenAI(api_key=os.environ["QWEN_API_KEY"], base_url=DASHSCOPE_BASE_URL)
    resp = client.embeddings.create(model=EMBED_MODEL, input=cleaned, dimensions=EMBED_DIM)
    return [d.embedding for d in resp.data]
