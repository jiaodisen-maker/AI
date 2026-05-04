"""GBrain 适配器。通过 GBrain MCP 或本地 CLI 调用。

需要的能力:
  - hybrid_search(query, k)           pgvector + tsvector + RRF
  - write_markdown(content, hints)    生成路径并写入 brain repo
  - read(path)                        读 markdown 内容
  - upsert_markdown(path, content)
  - append_section(path, header, body)
  - append_frontmatter(path, key, value)
  - changed_since(ts)                 git log 取增量
"""
from __future__ import annotations

# 留 stub。实际实现替换为 gbrain CLI 子进程或 MCP client。
async def hybrid_search(query: str, k: int = 10) -> list[dict]:
    raise NotImplementedError

async def write_markdown(content: str, hints: dict) -> str:
    raise NotImplementedError

async def read(path: str) -> str | None:
    raise NotImplementedError

async def upsert_markdown(path: str, content: str) -> None:
    raise NotImplementedError

async def append_section(path: str, header: str, body: str) -> None:
    raise NotImplementedError

async def append_frontmatter(path: str, key: str, value) -> None:
    raise NotImplementedError

async def changed_since(ts) -> list:
    raise NotImplementedError
