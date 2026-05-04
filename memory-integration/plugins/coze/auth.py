"""API Key 鉴权 + 简单的 per-bot 速率限制。"""
from __future__ import annotations

import hmac
import os
import time
from collections import defaultdict, deque

from fastapi import HTTPException, Request

EXPECTED = os.environ.get("PLUGIN_API_KEY", "")
if not EXPECTED:
    raise RuntimeError("PLUGIN_API_KEY env var is required")


def verify_bearer(request: Request) -> None:
    auth = request.headers.get("authorization", "")
    if not auth.startswith("Bearer "):
        raise HTTPException(401, "missing bearer token")
    token = auth[7:].strip()
    if not hmac.compare_digest(token, EXPECTED):
        raise HTTPException(401, "invalid bearer token")


# ---- per-bot rate limit（进程内滑动窗口；多实例部署用 Redis） ----

_BUCKETS: dict[tuple[str, str], deque] = defaultdict(deque)


def rate_limit(bucket: str, per_min: int):
    """装饰用：每分钟最多 per_min 次，按 bot_id 分桶。"""
    def deco(fn):
        async def wrapper(*args, request: Request, **kw):
            bot_id = (request.headers.get("x-coze-bot-id")
                      or request.headers.get("x-bot-id")
                      or "anonymous")
            key = (bucket, bot_id)
            now = time.time()
            q = _BUCKETS[key]
            while q and q[0] < now - 60:
                q.popleft()
            if len(q) >= per_min:
                raise HTTPException(503, f"rate limit: {per_min}/min for bot {bot_id}")
            q.append(now)
            return await fn(*args, request=request, **kw)
        return wrapper
    return deco
