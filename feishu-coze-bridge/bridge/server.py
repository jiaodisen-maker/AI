"""飞书 Webhook 接收（FastAPI）。

职责（**仅这些**）：
  1. URL 验证（飞书首次配置时发 challenge）
  2. encrypt_key AES-256-CBC 解密
  3. verification_token 校验
  4. event_id 幂等去重
  5. 立即入队 + 200 ACK（必须 < 200ms，否则飞书重投）

业务在 worker.py 里做。
"""
from __future__ import annotations

import base64
import hashlib
import json
import logging
import time
from typing import Any

import uvicorn
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from fastapi import FastAPI, Header, HTTPException, Request
from prometheus_client import Counter, Histogram, start_http_server

from .config import FEISHU, SERVER
from .idempotency import seen_before
from .queue import enqueue


LOG = logging.getLogger("bridge.server")
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s %(message)s")

WEBHOOK_TOTAL = Counter("bridge_webhook_total", "webhook events", ["event_type", "result"])
WEBHOOK_LATENCY = Histogram("bridge_webhook_seconds", "webhook handling time")


def _aes_decrypt(encrypt_b64: str) -> dict:
    """飞书 encrypt_key AES-256-CBC，IV 是密文前 16 字节，PKCS7 padding."""
    key = hashlib.sha256(FEISHU.encrypt_key.encode()).digest()
    cipher_bytes = base64.b64decode(encrypt_b64)
    iv, ct = cipher_bytes[:16], cipher_bytes[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    plain = cipher.decryptor().update(ct) + cipher.decryptor().finalize()
    pad = plain[-1]
    return json.loads(plain[:-pad].decode())


def _verify_signature(ts: str | None, nonce: str | None,
                       body: bytes, signature: str | None) -> bool:
    """飞书签名 = sha256(ts + nonce + encrypt_key + body)."""
    if not (ts and nonce and signature):
        return False
    s = (ts + nonce + FEISHU.encrypt_key).encode() + body
    return hashlib.sha256(s).hexdigest() == signature


app = FastAPI(title="feishu-coze-bridge")


@app.get("/healthz")
async def healthz():
    return {"ok": True, "ts": time.time()}


@app.post("/webhook/feishu")
@WEBHOOK_LATENCY.time()
async def webhook(
    req: Request,
    x_lark_signature: str | None = Header(default=None),
    x_lark_request_timestamp: str | None = Header(default=None),
    x_lark_request_nonce: str | None = Header(default=None),
):
    raw = await req.body()
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        WEBHOOK_TOTAL.labels("?", "bad_json").inc()
        raise HTTPException(400, "invalid json")

    # 加密模式
    if "encrypt" in payload:
        if x_lark_signature and not _verify_signature(
            x_lark_request_timestamp, x_lark_request_nonce, raw, x_lark_signature
        ):
            WEBHOOK_TOTAL.labels("?", "bad_signature").inc()
            raise HTTPException(401, "bad signature")
        try:
            payload = _aes_decrypt(payload["encrypt"])
        except Exception as e:
            WEBHOOK_TOTAL.labels("?", "decrypt_fail").inc()
            raise HTTPException(400, f"decrypt failed: {e}") from None

    # 1) URL 验证
    if payload.get("type") == "url_verification":
        return {"challenge": payload["challenge"]}

    # 2) verification_token 校验（兼容 v1 / v2 事件结构）
    token = payload.get("token") or payload.get("header", {}).get("token")
    if token != FEISHU.verification_token:
        WEBHOOK_TOTAL.labels("?", "bad_token").inc()
        raise HTTPException(401, "bad token")

    # 3) event_id 幂等
    event_id = (payload.get("header", {}).get("event_id")
                or payload.get("uuid"))
    if not event_id:
        WEBHOOK_TOTAL.labels("?", "no_event_id").inc()
        raise HTTPException(400, "missing event_id")

    if await seen_before(event_id):
        et = payload.get("header", {}).get("event_type", "?")
        WEBHOOK_TOTAL.labels(et, "dedup").inc()
        return {"ok": True, "dedup": True}

    # 4) 入队（立即返回）
    await enqueue(payload)

    et = payload.get("header", {}).get("event_type", "?")
    WEBHOOK_TOTAL.labels(et, "enqueued").inc()
    LOG.info("event %s enqueued event_id=%s", et, event_id)

    return {"ok": True}


def main() -> None:
    start_http_server(SERVER.prometheus_port)
    LOG.info("Prometheus on :%d", SERVER.prometheus_port)
    uvicorn.run(app, host=SERVER.bind_host, port=SERVER.bind_port,
                log_level="info")


if __name__ == "__main__":
    main()
