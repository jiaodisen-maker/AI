"""
飞书 Bot 服务

职责：
1. 接收飞书事件（含加密事件解密 + 签名验证）
2. Slash 命令处理（/clear /history /agents /help）
3. 路由到 Agent Router
4. 用户级隔离 + 私聊回复
"""
from __future__ import annotations

import json
import logging
import os
import time

import httpx
from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel

from .lark_security import LarkSecurityError, parse_event_body, verify_signature

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)
logger = logging.getLogger(__name__)


# ============================================================
# 配置
# ============================================================
LARK_APP_ID = os.getenv("LARK_APP_ID", "")
LARK_APP_SECRET = os.getenv("LARK_APP_SECRET", "")
LARK_VERIFICATION_TOKEN = os.getenv("LARK_VERIFICATION_TOKEN", "")
LARK_ENCRYPT_KEY = os.getenv("LARK_ENCRYPT_KEY", "")
AGENT_ROUTER_URL = os.getenv("AGENT_ROUTER_URL", "http://agent-router:8000")
LARK_API_BASE = "https://open.feishu.cn/open-apis"
DEBUG = os.getenv("DEBUG", "false").lower() == "true"


app = FastAPI(title="Lark Bot", version="0.2.0")


# ============================================================
# 飞书 Token 缓存
# ============================================================
class TokenCache:
    def __init__(self):
        self.access_token: str = ""
        self.expires_at: float = 0

    async def get(self) -> str:
        if self.access_token and self.expires_at > time.time() + 60:
            return self.access_token

        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(
                f"{LARK_API_BASE}/auth/v3/tenant_access_token/internal",
                json={"app_id": LARK_APP_ID, "app_secret": LARK_APP_SECRET},
            )
            data = response.json()
            self.access_token = data.get("tenant_access_token", "")
            self.expires_at = time.time() + data.get("expire", 7200)
        return self.access_token


token_cache = TokenCache()


# ============================================================
# 健康探针
# ============================================================
@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.get("/readyz")
async def readyz():
    # 探针 router 是否可达
    try:
        async with httpx.AsyncClient(timeout=2) as client:
            r = await client.get(f"{AGENT_ROUTER_URL}/healthz")
            r.raise_for_status()
        return {"status": "ready"}
    except Exception as e:
        raise HTTPException(503, f"router not ready: {e}")


# ============================================================
# 飞书事件订阅入口
# ============================================================
@app.post("/lark/event")
async def handle_lark_event(
    request: Request,
    x_lark_signature: str | None = Header(None, alias="X-Lark-Signature"),
    x_lark_request_timestamp: str | None = Header(None, alias="X-Lark-Request-Timestamp"),
    x_lark_request_nonce: str | None = Header(None, alias="X-Lark-Request-Nonce"),
):
    """飞书事件回调"""
    raw_body = await request.body()

    # 签名验证（如果配置了 encrypt_key）
    if LARK_ENCRYPT_KEY and x_lark_signature:
        if not verify_signature(
            timestamp=x_lark_request_timestamp or "",
            nonce=x_lark_request_nonce or "",
            body_raw=raw_body,
            signature=x_lark_signature,
            encrypt_key=LARK_ENCRYPT_KEY,
        ):
            raise HTTPException(401, "Invalid signature")

    try:
        body = json.loads(raw_body.decode("utf-8"))
    except json.JSONDecodeError:
        raise HTTPException(400, "Invalid JSON")

    # 解密（如果是加密事件）
    try:
        body = parse_event_body(body, LARK_ENCRYPT_KEY)
    except LarkSecurityError as e:
        raise HTTPException(400, f"Decrypt failed: {e}")

    # URL 验证（首次配置）
    if body.get("type") == "url_verification":
        if LARK_VERIFICATION_TOKEN and body.get("token") != LARK_VERIFICATION_TOKEN:
            raise HTTPException(401, "Invalid verification token")
        return {"challenge": body.get("challenge")}

    # 事件分发
    header = body.get("header", {})
    event = body.get("event", {})
    event_type = header.get("event_type", "")

    if event_type == "im.message.receive_v1":
        return await _handle_message(event)

    return {"code": 0}


# ============================================================
# 消息处理 + Slash 命令
# ============================================================
async def _handle_message(event: dict):
    """处理收到的消息"""
    try:
        sender = event.get("sender", {})
        message = event.get("message", {})

        sender_id = sender.get("sender_id", {})
        user_id = sender_id.get("open_id") or sender_id.get("user_id", "")
        if not user_id:
            return {"code": 0}

        msg_type = message.get("message_type", "")
        if msg_type != "text":
            return {"code": 0}

        content = json.loads(message.get("content", "{}"))
        text = content.get("text", "").strip()
        # 群聊里 @bot 飞书会自动加 @_user_xxx，去掉
        text = _strip_at_mentions(text).strip()
        if not text:
            return {"code": 0}

        message_id = message.get("message_id", "")
        chat_type = message.get("chat_type", "p2p")

        logger.info(f"Received from user={user_id} chat={chat_type}: {text[:80]}")

        # === Slash 命令分支 ===
        if text.startswith("/"):
            reply = await _handle_slash_command(user_id, text)
        else:
            reply = await _route_and_invoke(user_id=user_id, text=text)

        await _reply_message(user_id=user_id, message_id=message_id, content=reply)

    except Exception:
        logger.exception("Failed to handle message")

    return {"code": 0}


def _strip_at_mentions(text: str) -> str:
    """去掉 @_user_x 的飞书 mention 标记"""
    import re
    return re.sub(r"@_user_\d+", "", text)


async def _handle_slash_command(user_id: str, text: str) -> str:
    """处理 / 开头的命令"""
    parts = text.split(maxsplit=1)
    cmd = parts[0].lower()

    if cmd == "/help":
        return (
            "支持的命令：\n"
            "/help        显示本帮助\n"
            "/agents      列出可用的 AI 助手\n"
            "/history     查看你的对话历史\n"
            "/clear       清空你的对话历史\n"
            "其他消息     自动路由到合适的 AI 助手"
        )

    if cmd == "/clear":
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                r = await client.delete(f"{AGENT_ROUTER_URL}/sessions/{user_id}")
                r.raise_for_status()
            return "✓ 已清空你的对话历史"
        except Exception as e:
            return f"清空失败：{e}"

    if cmd == "/history":
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                r = await client.get(
                    f"{AGENT_ROUTER_URL}/sessions/{user_id}/history?limit=10"
                )
                r.raise_for_status()
                data = r.json()
            messages = data.get("messages", [])
            if not messages:
                return "对话历史为空"
            lines = [f"最近 {len(messages)} 条消息："]
            for m in messages:
                role_icon = "🙋" if m["role"] == "user" else "🤖"
                content = m["content"][:80]
                lines.append(f"{role_icon} {content}")
            return "\n".join(lines)
        except Exception as e:
            return f"获取历史失败：{e}"

    if cmd == "/agents":
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                r = await client.get(f"{AGENT_ROUTER_URL}/agents")
                r.raise_for_status()
                data = r.json()
            agents = data.get("agents", [])
            if not agents:
                return "暂无可用的 AI 助手"
            lines = [f"共 {len(agents)} 个可用 AI 助手："]
            for a in agents[:20]:
                name = a["name"]
                display = a.get("display_name", name)
                desc = a.get("description", "")[:40]
                maturity = a.get("maturity", "")
                lines.append(f"• {display} ({name}) [{maturity}]\n  {desc}")
            return "\n".join(lines)
        except Exception as e:
            return f"获取列表失败：{e}"

    return f"未知命令：{cmd}\n输入 /help 查看支持的命令"


async def _route_and_invoke(user_id: str, text: str) -> str:
    """通过 Agent Router 完整调用"""
    async with httpx.AsyncClient(timeout=70) as client:
        try:
            # 直接 invoke（router 会自动 discover）
            invoke_resp = await client.post(
                f"{AGENT_ROUTER_URL}/agents/invoke",
                json={
                    "input": text,
                    "session_id": user_id,
                    "user_id": user_id,
                    "metadata": {"channel": "lark"},
                },
            )
            invoke_resp.raise_for_status()
            data = invoke_resp.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return "没找到匹配的 AI 助手，请换个说法或 /help 查看可用助手"
            logger.error(f"Invoke failed: {e}")
            return f"AI 服务出错：HTTP {e.response.status_code}"
        except httpx.HTTPError as e:
            logger.error(f"Invoke failed: {e}")
            return "AI 服务暂时不可用，请稍后再试"

        if data.get("error"):
            return f"出错了：{data['error']}"
        return data.get("output", "（无回复）")


# ============================================================
# 飞书消息发送（私聊优先）
# ============================================================
async def _reply_message(user_id: str, message_id: str, content: str):
    if not content:
        return

    if not LARK_APP_ID or not LARK_APP_SECRET:
        logger.warning(f"LARK creds missing, would reply to {user_id}: {content[:80]}")
        return

    token = await token_cache.get()
    if not token:
        return

    async with httpx.AsyncClient(timeout=10) as client:
        try:
            if message_id:
                response = await client.post(
                    f"{LARK_API_BASE}/im/v1/messages/{message_id}/reply",
                    headers={"Authorization": f"Bearer {token}"},
                    json={
                        "msg_type": "text",
                        "content": json.dumps({"text": content}),
                    },
                )
            else:
                response = await client.post(
                    f"{LARK_API_BASE}/im/v1/messages?receive_id_type=open_id",
                    headers={"Authorization": f"Bearer {token}"},
                    json={
                        "receive_id": user_id,
                        "msg_type": "text",
                        "content": json.dumps({"text": content}),
                    },
                )
            if response.status_code != 200:
                logger.error(f"Lark reply failed: {response.text}")
        except httpx.HTTPError as e:
            logger.error(f"Lark API error: {e}")


# ============================================================
# 调试接口
# ============================================================
class MockMessageRequest(BaseModel):
    user_id: str = "test_user_001"
    text: str


@app.post("/debug/message")
async def debug_message(req: MockMessageRequest):
    """开发用：模拟飞书消息（不调真飞书 API）"""
    if not DEBUG:
        raise HTTPException(403, "Debug endpoint disabled (set DEBUG=true)")

    if req.text.startswith("/"):
        reply = await _handle_slash_command(req.user_id, req.text)
    else:
        reply = await _route_and_invoke(user_id=req.user_id, text=req.text)
    return {"user_id": req.user_id, "input": req.text, "output": reply}


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8001"))
    uvicorn.run(app, host="0.0.0.0", port=port)
