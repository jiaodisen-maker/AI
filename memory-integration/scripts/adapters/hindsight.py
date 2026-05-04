"""Hindsight 适配器。Python embedded 模式。

需要的能力:
  - retain(content, meta)                      → memory_id
  - recall(query, k)                           → list[hit dict]
  - stable_entities(min_age_hours, ...)        → list[Entity]
  - stable_beliefs(min_confidence)             → list[Belief]
  - mark_archived(id, gbrain_path)
"""
from __future__ import annotations

# 留 stub。实际实现替换为 `from hindsight import Memory; m = Memory(...)`。
async def retain(content: str, meta: dict) -> str:
    raise NotImplementedError

async def recall(query: str, k: int = 10) -> list[dict]:
    raise NotImplementedError

async def stable_entities(min_age_hours: int, min_confidence: float,
                          min_observations: int, scope: str) -> list:
    raise NotImplementedError

async def stable_beliefs(min_confidence: float) -> list:
    raise NotImplementedError

async def mark_archived(id: str, gbrain_path: str) -> None:
    raise NotImplementedError
