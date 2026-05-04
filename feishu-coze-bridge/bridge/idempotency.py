"""event_id 去重 —— Redis SETNX。

飞书事件订阅是 at-least-once，必须去重，否则会重复处理。
"""
from __future__ import annotations

import redis.asyncio as redis

from .config import QUEUE


_r = redis.from_url(QUEUE.redis_url, db=1)   # 用单独 db 避免跟队列互相影响


async def seen_before(event_id: str) -> bool:
    """已见过返回 True；首次返回 False 并 mark."""
    ok = await _r.set(f"feishu:eid:{event_id}", "1",
                       nx=True, ex=QUEUE.idempotency_ttl_s)
    return not ok
