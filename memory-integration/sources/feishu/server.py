"""飞书 Webhook 接收端。

职责（且仅做这些）：
  1. URL 验证（首次配置时飞书会发 challenge）
  2. encrypt_key AES 解密
  3. verification_token 校验
  4. event_id 幂等
  5. 立即入队
  6. 200 OK 立即返回（不超过 200ms，否则飞书会重投）

不做：业务处理 → 都在 worker.py 里。
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
from typing import Any

import yaml
from fastapi import FastAPI, Header, HTTPException, Request
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from .idempotency import seen_before
from .queue import enqueue

CFG = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), "config.yaml")))
ENCRYPT_KEY = os.path.expandvars(CFG["feishu"]["encrypt_key"])
VERIFICATION_TOKEN = os.path.expandvars(CFG["feishu"]["verification_token"])

app = FastAPI(title="memory-integration · feishu webhook")


def _aes_decrypt(encrypt: str) -> dict:
    """飞书 encrypt_key 用 AES-256-CBC，IV 是密文前 16 字节。"""
    key = hashlib.sha256(ENCRYPT_KEY.encode()).digest()
    cipher_bytes = base64.b64decode(encrypt)
    iv, ct = cipher_bytes[:16], cipher_bytes[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plain = decryptor.update(ct) + decryptor.finalize()
    pad = plain[-1]
    return json.loads(plain[:-pad].decode())


@app.post(CFG["feishu"]["webhook"]["path"])
async def webhook(req: Request,
                  x_lark_signature: str | None = Header(default=None),
                  x_lark_request_timestamp: str | None = Header(default=None),
                  x_lark_request_nonce: str | None = Header(default=None)):
    raw = await req.body()
    try:
        payload = json.loads(raw)
    except Exception:
        raise HTTPException(400, "invalid json")

    # 加密模式：飞书把整个 payload 塞在 encrypt 字段里
    if "encrypt" in payload:
        # 签名校验（可选但强烈建议开）
        if x_lark_signature and not _verify_signature(
            x_lark_request_timestamp, x_lark_request_nonce, raw, x_lark_signature
        ):
            raise HTTPException(401, "bad signature")
        payload = _aes_decrypt(payload["encrypt"])

    # 1) URL 验证（首次配置）
    if payload.get("type") == "url_verification":
        return {"challenge": payload["challenge"]}

    # 2) verification_token 校验
    token = payload.get("token") or payload.get("header", {}).get("token")
    if token != VERIFICATION_TOKEN:
        raise HTTPException(401, "bad token")

    # 3) 幂等
    event_id = (payload.get("header", {}).get("event_id")
                or payload.get("uuid"))
    if not event_id:
        raise HTTPException(400, "missing event_id")
    if await seen_before(event_id):
        return {"ok": True, "dedup": True}

    # 4) 入队（立即返回，处理在 worker）
    await enqueue(payload)
    return {"ok": True}


def _verify_signature(ts: str | None, nonce: str | None,
                      body: bytes, sig: str) -> bool:
    if not (ts and nonce):
        return False
    s = (ts + nonce + ENCRYPT_KEY).encode() + body
    return hashlib.sha256(s).hexdigest() == sig


def main():
    import uvicorn
    bind = CFG["feishu"]["webhook"]["bind"]
    host, port = bind.split(":")
    uvicorn.run(app, host=host, port=int(port))


if __name__ == "__main__":
    main()
