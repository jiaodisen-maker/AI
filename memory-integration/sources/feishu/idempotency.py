"""event_id 幂等去重。Redis SETNX。"""
from __future__ import annotations

import os
import yaml
import redis.asyncio as redis

CFG = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), "config.yaml")))
_r = redis.from_url(CFG["idempotency"]["url"])
_TTL = CFG["idempotency"]["ttl_seconds"]


async def seen_before(event_id: str) -> bool:
    """已见过返回 True；首次返回 False 并打标。"""
    ok = await _r.set(f"feishu:eid:{event_id}", "1", nx=True, ex=_TTL)
    return not ok
