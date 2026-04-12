"""Feishu webhook endpoint: receives events from Feishu bot."""

from __future__ import annotations

import logging
from typing import Any

from fastapi import APIRouter, Request

router = APIRouter(prefix="/feishu", tags=["feishu"])

logger = logging.getLogger(__name__)

# Dedup TTL in seconds (5 minutes)
_DEDUP_TTL = 300


@router.post("/webhook")
async def feishu_webhook(request: Request) -> dict[str, Any]:
    """Handle Feishu webhook events.

    Supports:
    - URL verification challenge
    - Message events (text messages)
    """
    from app.main import get_app_state

    body = await request.json()
    state = get_app_state()
    feishu_bot = state.feishu_bot

    # Step 1: Event verification
    challenge_response = feishu_bot.verify_event(body)
    if challenge_response:
        return challenge_response

    # Step 2: Parse message event
    event_type = body.get("header", {}).get("event_type", "")
    if event_type != "im.message.receive_v1":
        logger.debug("Ignoring event type: %s", event_type)
        return {"status": "ignored"}

    message = feishu_bot.parse_message_event(body)
    if not message:
        return {"status": "no_content"}

    # Step 3: Dedup (Redis SETNX with TTL, fallback to in-memory)
    redis_client = None
    if hasattr(state, "redis") and state.redis and state.redis.is_connected:
        redis_client = state.redis.client

    if redis_client:
        dedup_key = f"feishu:dedup:{message.message_id}"
        was_set = await redis_client.set(dedup_key, "1", ex=_DEDUP_TTL, nx=True)
        if not was_set:
            logger.debug("Duplicate message (Redis): %s", message.message_id)
            return {"status": "duplicate"}
    else:
        # Fallback: in-memory set (single worker only)
        if not hasattr(feishu_webhook, "_seen"):
            feishu_webhook._seen = set()
        if message.message_id in feishu_webhook._seen:
            return {"status": "duplicate"}
        feishu_webhook._seen.add(message.message_id)
        if len(feishu_webhook._seen) > 1000:
            feishu_webhook._seen = set(list(feishu_webhook._seen)[-500:])

    # Step 4: Process through message router
    logger.info("Feishu message from %s: %s", message.user_id, message.content[:100])

    outgoing = await state.message_router.handle(message)

    # Step 5: Reply
    if message.message_id:
        await feishu_bot.reply_text(message.message_id, outgoing.content)

    return {"status": "ok"}
