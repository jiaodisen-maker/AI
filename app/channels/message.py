"""Message router: connects channels to the Skill Dispatcher.

Every message from any channel ends up going through SkillDispatcher,
which routes to the appropriate Skill. Skill is always the center.
"""

from __future__ import annotations

import logging
import uuid
from typing import TYPE_CHECKING

from app.channels.models import IncomingMessage, OutgoingMessage

if TYPE_CHECKING:
    from app.skills.dispatcher import SkillDispatcher

logger = logging.getLogger(__name__)


class MessageRouter:
    """Thin adapter: channel message → SkillDispatcher → channel response."""

    def __init__(self, dispatcher: SkillDispatcher) -> None:
        self.dispatcher = dispatcher

    async def handle(self, message: IncomingMessage) -> OutgoingMessage:
        """Process an incoming message through the Skill Dispatcher."""
        session_id = message.session_id or uuid.uuid4().hex

        logger.info(
            "Message from %s [%s]: %s",
            message.user_id,
            message.source,
            message.content[:100],
        )

        result = await self.dispatcher.dispatch(
            message=message.content,
            user_id=message.user_id,
            session_id=session_id,
            source=message.source.value,
        )

        return OutgoingMessage(
            content=result["content"],
            target_user_id=message.user_id,
            target_chat_id=message.chat_id,
            source=message.source,
            metadata={
                "skill_id": result.get("skill_id"),
                "tier": result.get("tier"),
                **result.get("metadata", {}),
            },
        )
