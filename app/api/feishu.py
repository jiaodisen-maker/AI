"""Feishu webhook endpoint: receives events from Feishu bot."""

from __future__ import annotations

import logging
from typing import Any

from fastapi import APIRouter, Request

router = APIRouter(prefix="/feishu", tags=["feishu"])

logger = logging.getLogger(__name__)

# Dedup: track recently processed message IDs to avoid duplicate processing
_processed_messages: set[str] = set()
_MAX_PROCESSED_CACHE = 1000


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

    # Step 3: Dedup
    if message.message_id in _processed_messages:
        logger.debug("Duplicate message: %s", message.message_id)
        return {"status": "duplicate"}

    _processed_messages.add(message.message_id)
    if len(_processed_messages) > _MAX_PROCESSED_CACHE:
        # Simple cache eviction: clear half
        to_remove = list(_processed_messages)[: _MAX_PROCESSED_CACHE // 2]
        for mid in to_remove:
            _processed_messages.discard(mid)

    # Step 4: Process through message router
    logger.info("Feishu message from %s: %s", message.user_id, message.content[:100])

    outgoing = await state.message_router.handle(message)

    # Step 5: Reply
    if message.message_id:
        await feishu_bot.reply_text(message.message_id, outgoing.content)

    return {"status": "ok"}
