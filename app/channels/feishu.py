"""Feishu (飞书) bot integration: webhook handler, message send/receive."""

from __future__ import annotations

import logging
from typing import Any

import httpx

from app.channels.models import IncomingMessage, MessageSource
from app.config import settings

logger = logging.getLogger(__name__)

# Feishu API endpoints
FEISHU_TOKEN_URL = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
FEISHU_SEND_MSG_URL = "https://open.feishu.cn/open-apis/im/v1/messages"
FEISHU_REPLY_MSG_URL = "https://open.feishu.cn/open-apis/im/v1/messages/{message_id}/reply"


class FeishuBot:
    """Feishu bot for receiving and sending messages.

    Handles:
    - Webhook event verification
    - Parsing incoming messages
    - Sending text/card replies
    - Tenant access token management
    """

    def __init__(self) -> None:
        self._tenant_token: str = ""
        self._token_expires_at: float = 0.0
        self._http = httpx.AsyncClient(timeout=10)

    async def get_tenant_token(self) -> str:
        """Obtain or refresh the tenant access token (expires every 2 hours)."""
        import time

        # Return cached token if still valid (with 5 min buffer)
        if self._tenant_token and time.time() < self._token_expires_at - 300:
            return self._tenant_token

        if not settings.feishu_app_id:
            logger.warning("Feishu app_id not configured")
            return ""

        resp = await self._http.post(
            FEISHU_TOKEN_URL,
            json={
                "app_id": settings.feishu_app_id,
                "app_secret": settings.feishu_app_secret,
            },
        )
        import time

        data = resp.json()
        self._tenant_token = data.get("tenant_access_token", "")
        # Token expires in ~2 hours (7200s), cache with expiry tracking
        expire_in = data.get("expire", 7200)
        self._token_expires_at = time.time() + expire_in
        return self._tenant_token

    def verify_event(self, body: dict[str, Any]) -> dict[str, Any] | None:
        """Verify and handle Feishu webhook event.

        Returns challenge response for URL verification,
        or None if this is a regular event.
        """
        # URL verification challenge
        if "challenge" in body:
            return {"challenge": body["challenge"]}

        # Token verification
        token = body.get("header", {}).get("token", "")
        if settings.feishu_verification_token and token != settings.feishu_verification_token:
            logger.warning("Feishu event token mismatch")
            return {"error": "token mismatch"}

        return None

    def parse_message_event(self, body: dict[str, Any]) -> IncomingMessage | None:
        """Parse a Feishu message event into IncomingMessage."""
        event = body.get("event", {})
        message = event.get("message", {})
        sender = event.get("sender", {})

        # Only handle text messages for now
        msg_type = message.get("message_type", "")
        if msg_type != "text":
            logger.debug("Ignoring non-text message type: %s", msg_type)
            return None

        # Extract text content
        import json

        try:
            content_json = json.loads(message.get("content", "{}"))
            text = content_json.get("text", "")
        except json.JSONDecodeError:
            text = ""

        if not text:
            return None

        # Strip @bot mention prefix
        if text.startswith("@_user"):
            text = text.split(" ", 1)[-1] if " " in text else text

        return IncomingMessage(
            message_id=message.get("message_id", ""),
            source=MessageSource.FEISHU,
            user_id=sender.get("sender_id", {}).get("user_id", ""),
            user_name=sender.get("sender_id", {}).get("name", ""),
            content=text.strip(),
            chat_id=message.get("chat_id", ""),
            raw_event=body,
        )

    async def reply_text(self, message_id: str, text: str) -> bool:
        """Reply to a specific message with text."""
        token = await self.get_tenant_token()
        if not token:
            logger.error("Cannot reply: no tenant token")
            return False

        import json

        resp = await self._http.post(
            FEISHU_REPLY_MSG_URL.format(message_id=message_id),
            headers={"Authorization": f"Bearer {token}"},
            json={
                "msg_type": "text",
                "content": json.dumps({"text": text}),
            },
        )

        if resp.status_code == 200:
            return True

        logger.error("Feishu reply failed: %s", resp.text)
        return False

    async def send_text_message(
        self,
        text: str,
        chat_id: str = "",
        user_id: str = "",
    ) -> bool:
        """Send a text message to a chat or user."""
        token = await self.get_tenant_token()
        if not token:
            logger.error("Cannot send: no tenant token")
            return False

        import json

        receive_id_type = "chat_id" if chat_id else "user_id"
        receive_id = chat_id or user_id

        if not receive_id:
            logger.error("No target specified for message")
            return False

        resp = await self._http.post(
            FEISHU_SEND_MSG_URL,
            headers={"Authorization": f"Bearer {token}"},
            params={"receive_id_type": receive_id_type},
            json={
                "receive_id": receive_id,
                "msg_type": "text",
                "content": json.dumps({"text": text}),
            },
        )

        if resp.status_code == 200:
            return True

        logger.error("Feishu send failed: %s", resp.text)
        return False

    async def send_card_message(
        self,
        card: dict[str, Any],
        chat_id: str = "",
        user_id: str = "",
    ) -> bool:
        """Send an interactive card message."""
        token = await self.get_tenant_token()
        if not token:
            return False

        import json

        receive_id_type = "chat_id" if chat_id else "user_id"
        receive_id = chat_id or user_id

        resp = await self._http.post(
            FEISHU_SEND_MSG_URL,
            headers={"Authorization": f"Bearer {token}"},
            params={"receive_id_type": receive_id_type},
            json={
                "receive_id": receive_id,
                "msg_type": "interactive",
                "content": json.dumps(card),
            },
        )

        return resp.status_code == 200

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._http.aclose()
