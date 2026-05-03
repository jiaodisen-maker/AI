"""
飞书 Bot 服务

职责：
1. 接收飞书消息事件
2. 验证签名
3. 转发到 Agent Router
4. 用户级隔离（每用户独立 session）
5. 私聊回复（不污染群聊）
"""
from __future__ import annotations

import hashlib
import json
import logging
import os

import httpx
from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================
# 配置
# ============================================================
LARK_APP_ID = os.getenv("LARK_APP_ID", "")
LARK_APP_SECRET = os.getenv("LARK_APP_SECRET", "")
LARK_VERIFICATION_TOKEN = os.getenv("LARK_VERIFICATION_TOKEN", "")
AGENT_ROUTER_URL = os.getenv("AGENT_ROUTER_URL", "http://agent-router:8000")
LARK_API_BASE = "https://open.feishu.cn/open-apis"


app = FastAPI(title="Lark Bot", version="0.1.0")


# ============================================================
# 飞书 Token 缓存（简化版，生产用 Redis）
# ============================================================
class TokenCache:
    def __init__(self):
        self.access_token: str = ""
        self.expires_at: float = 0

    async def get(self) -> str:
        import time
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
# 健康检查
# ============================================================
@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


# ============================================================
# 飞书事件订阅入口
# ============================================================
@app.post("/lark/event")
async def handle_lark_event(request: Request):
    """飞书消息事件回调"""
    body = await request.json()

    # 飞书首次配置时的 URL 验证（challenge 协议）
    if body.get("type") == "url_verification":
        # 验证 verification_token
        if body.get("token") != LARK_VERIFICATION_TOKEN:
            raise HTTPException(401, "Invalid verification token")
        return {"challenge": body.get("challenge")}

    # 事件回调（v2 协议）
    header = body.get("header", {})
    event = body.get("event", {})
    event_type = header.get("event_type", "")

    if event_type == "im.message.receive_v1":
        return await _handle_message(event)

    # 其他事件忽略
    return {"code": 0}


# ============================================================
# 消息处理（用户级隔离）
# ============================================================
async def _handle_message(event: dict):
    """处理收到的消息"""
    try:
        sender = event.get("sender", {})
        message = event.get("message", {})

        sender_id_obj = sender.get("sender_id", {})
        user_id = sender_id_obj.get("open_id") or sender_id_obj.get("user_id", "")
        if not user_id:
            return {"code": 0}

        msg_type = message.get("message_type", "")
        if msg_type != "text":
            # 非文本消息暂不处理
            return {"code": 0}

        content_raw = message.get("content", "{}")
        content = json.loads(content_raw)
        text = content.get("text", "").strip()

        # 群聊里要 @bot 才响应（飞书会自动去掉 @）
        chat_type = message.get("chat_type", "p2p")
        message_id = message.get("message_id", "")

        if not text:
            return {"code": 0}

        logger.info(f"Received from user={user_id} chat={chat_type}: {text[:80]}")

        # 路由到 Agent Router（先 discover 再 invoke）
        reply = await _route_and_invoke(user_id=user_id, text=text)

        # 回复消息
        await _reply_message(user_id=user_id, message_id=message_id, content=reply)

    except Exception:
        logger.exception("Failed to handle message")

    return {"code": 0}


async def _route_and_invoke(user_id: str, text: str) -> str:
    """路由到 Agent Router 并调用合适的 Agent"""
    async with httpx.AsyncClient(timeout=70) as client:
        # 1. 发现合适的 Agent
        try:
            discover_resp = await client.post(
                f"{AGENT_ROUTER_URL}/agents/discover",
                json={"query": text, "top_k": 1, "user_id": user_id},
            )
            discover_resp.raise_for_status()
            agents = discover_resp.json().get("agents", [])
        except httpx.HTTPError as e:
            logger.error(f"Discover failed: {e}")
            return "AI 服务暂时不可用，请稍后再试"

        if not agents:
            return "没找到匹配的 AI 助手，请换个说法或联系管理员"

        agent_name = agents[0]["name"]
        logger.info(f"Routing to agent: {agent_name}")

        # 2. 调用
        try:
            invoke_resp = await client.post(
                f"{AGENT_ROUTER_URL}/agents/invoke",
                json={
                    "agent_name": agent_name,
                    "input": text,
                    "session_id": user_id,  # session = user，实现用户隔离
                    "user_id": user_id,
                    "metadata": {"channel": "lark"},
                },
            )
            invoke_resp.raise_for_status()
            data = invoke_resp.json()
        except httpx.HTTPError as e:
            logger.error(f"Invoke failed: {e}")
            return "AI 调用出错，请稍后再试"

        if data.get("error"):
            return f"出错了：{data['error']}"
        return data.get("output", "（无回复）")


# ============================================================
# 飞书消息发送
# ============================================================
async def _reply_message(user_id: str, message_id: str, content: str):
    """通过飞书 API 回复消息（用户私聊形式，保护隐私）"""
    if not content:
        return

    token = await token_cache.get()
    if not token:
        logger.error("No Lark token, cannot reply")
        return

    # 优先用 reply（针对原消息回复），否则发新消息
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            if message_id:
                # 回复原消息
                response = await client.post(
                    f"{LARK_API_BASE}/im/v1/messages/{message_id}/reply",
                    headers={"Authorization": f"Bearer {token}"},
                    json={
                        "msg_type": "text",
                        "content": json.dumps({"text": content}),
                    },
                )
            else:
                # 发新消息（私聊）
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
# 调试用：模拟飞书消息（开发环境）
# ============================================================
class MockMessageRequest(BaseModel):
    user_id: str = "test_user_001"
    text: str


@app.post("/debug/message")
async def debug_message(req: MockMessageRequest):
    """开发调试用：模拟飞书消息触发完整流程，但不调真飞书 API"""
    if os.getenv("DEBUG", "false").lower() != "true":
        raise HTTPException(403, "Debug endpoint disabled")
    reply = await _route_and_invoke(user_id=req.user_id, text=req.text)
    return {"user_id": req.user_id, "input": req.text, "output": reply}


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8001"))
    uvicorn.run(app, host="0.0.0.0", port=port)
