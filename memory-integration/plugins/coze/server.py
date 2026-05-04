"""Coze 自定义插件服务。

暴露 4 个 HTTP 端点给 Coze bot 调，鉴权后委托给 MemoryRouter。
"""
from __future__ import annotations

import hashlib
import json
import logging
import os
import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

import httpx
import yaml
from fastapi import Depends, FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from .auth import rate_limit, verify_bearer

LOG = logging.getLogger("coze-plugin")
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s %(message)s")

BACKEND_MODE = os.environ.get("MEMORY_BACKEND", "stdio")
HTTP_URL = os.environ.get("MEMORY_HTTP_URL", "http://memory-backend:7900")
RL_RECALL  = int(os.environ.get("RATE_LIMIT_RECALL_PER_MIN", 120))
RL_WRITE   = int(os.environ.get("RATE_LIMIT_WRITE_PER_MIN", 30))
RL_REFLECT = int(os.environ.get("RATE_LIMIT_REFLECT_PER_MIN", 2))

AUDIT_LOG = Path(os.environ.get("AUDIT_LOG", "/var/log/coze-plugin/audit.log"))


# ---- backend 委托 ---------------------------------------------------

if BACKEND_MODE == "stdio":
    from ...scripts.router import MemoryRouter   # 进程内调
    _router = MemoryRouter()

    async def _write(content: str, hints: dict) -> dict:
        r = await _router.write(content, hints)
        return r.__dict__

    async def _recall(query: str, k: int) -> list[dict]:
        hits = await _router.recall(query, k)
        return [h.__dict__ for h in hits]

    async def _reflect(scope: str, dry_run: bool) -> dict:
        from ...reliability.state import State           # 复用其状态
        from ...scripts.auto_dream import consolidate
        rep = await consolidate(scope, dry_run)
        return rep
else:
    async def _write(content: str, hints: dict) -> dict:
        async with httpx.AsyncClient(timeout=8) as cli:
            r = await cli.post(f"{HTTP_URL}/memory_write",
                               json={"content": content, "hints": hints})
            r.raise_for_status()
            return r.json()

    async def _recall(query: str, k: int) -> list[dict]:
        async with httpx.AsyncClient(timeout=8) as cli:
            r = await cli.post(f"{HTTP_URL}/memory_recall",
                               json={"query": query, "k": k})
            r.raise_for_status()
            return r.json()

    async def _reflect(scope: str, dry_run: bool) -> dict:
        async with httpx.AsyncClient(timeout=30) as cli:
            r = await cli.post(f"{HTTP_URL}/memory_reflect",
                               json={"scope": scope, "dry_run": dry_run})
            r.raise_for_status()
            return r.json()


# ---- 审计 ----------------------------------------------------------

def _audit(bot_id: str, op: str, payload: Any, result_bytes: int):
    try:
        AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
        h = hashlib.sha256(
            json.dumps(payload, sort_keys=True, default=str).encode()
        ).hexdigest()[:16]
        AUDIT_LOG.open("a").write(json.dumps({
            "ts": time.time(),
            "bot_id": bot_id,
            "op": op,
            "in_hash": h,
            "out_bytes": result_bytes,
        }) + "\n")
    except Exception as e:
        LOG.warning("audit write failed: %s", e)


# ---- schemas -------------------------------------------------------

class WriteIn(BaseModel):
    content: str = Field(..., description="要写入的记忆原文")
    hints: dict = Field(default_factory=dict,
                        description="提示路由：{source, type, subject_ref, ...}")

class WriteOut(BaseModel):
    target: str
    gbrain_path: str | None = None
    hindsight_id: str | None = None

class RecallIn(BaseModel):
    query: str = Field(..., description="自然语言问题或关键词")
    k: int = Field(5, ge=1, le=50)

class RecallHit(BaseModel):
    id: str
    text: str
    score: float
    source: str
    ref: str
    ts: str

class ReflectIn(BaseModel):
    scope: str = Field("recent", pattern="^(recent|all)$")
    dry_run: bool = False


# ---- app -----------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    LOG.info("coze-plugin starting; backend=%s", BACKEND_MODE)
    yield
    LOG.info("coze-plugin shutdown")

app = FastAPI(title="memory-integration · coze plugin",
              version="1.0.0", lifespan=lifespan,
              dependencies=[Depends(verify_bearer)])


@app.get("/healthz", dependencies=[])
async def healthz():
    return {"ok": True}


@app.post("/memory/recall", response_model=list[RecallHit])
@rate_limit("recall", RL_RECALL)
async def recall(body: RecallIn, request: Request):
    bot = request.headers.get("x-coze-bot-id", "anonymous")
    hits = await _recall(body.query, body.k)
    _audit(bot, "recall", body.dict(), len(json.dumps(hits)))
    return hits


@app.post("/memory/write", response_model=WriteOut)
@rate_limit("write", RL_WRITE)
async def write(body: WriteIn, request: Request):
    bot = request.headers.get("x-coze-bot-id", "anonymous")
    res = await _write(body.content, body.hints)
    _audit(bot, "write", body.dict(), len(json.dumps(res)))
    return res


@app.post("/memory/reflect")
@rate_limit("reflect", RL_REFLECT)
async def reflect(body: ReflectIn, request: Request):
    bot = request.headers.get("x-coze-bot-id", "anonymous")
    rep = await _reflect(body.scope, body.dry_run)
    _audit(bot, "reflect", body.dict(), len(json.dumps(rep)))
    return rep


@app.get("/memory/person/{ref:path}")
@rate_limit("recall", RL_RECALL)
async def lookup_person(ref: str, request: Request):
    """ref 可以是 brain/people/xxx.md，也可以是 email / mobile / open_id 关键词"""
    bot = request.headers.get("x-coze-bot-id", "anonymous")
    hits = await _recall(f"person:{ref}", 8)
    _audit(bot, "person", {"ref": ref}, len(json.dumps(hits)))
    return {"ref": ref, "matches": hits}


def main():
    import uvicorn
    uvicorn.run(app,
                host=os.environ.get("BIND_HOST", "0.0.0.0"),
                port=int(os.environ.get("BIND_PORT", 8810)))


if __name__ == "__main__":
    main()
