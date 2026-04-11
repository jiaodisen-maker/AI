"""Message router: connects channels to the AgentScope-powered brain."""

from __future__ import annotations

import logging
import uuid
from typing import TYPE_CHECKING

from app.channels.models import IncomingMessage, OutgoingMessage

if TYPE_CHECKING:
    from app.brain.agent import BrainAgent
    from app.experience.engine import ExperienceEngine

logger = logging.getLogger(__name__)


class MessageRouter:
    """Routes incoming messages through the AgentScope ReActAgent.

    Message → BrainAgent (ReActAgent with tool calling) → Response

    The agent autonomously decides which skills to call.
    """

    def __init__(
        self,
        brain: BrainAgent,
        experience_engine: ExperienceEngine,
    ) -> None:
        self.brain = brain
        self.experience_engine = experience_engine

    async def handle(self, message: IncomingMessage) -> OutgoingMessage:
        """Process an incoming message through the AgentScope agent."""
        session_id = message.session_id or uuid.uuid4().hex

        logger.info(
            "Processing message from %s [%s]: %s",
            message.user_id,
            message.source,
            message.content[:100],
        )

        # Get experience prompt for injection
        experience_prompt = ""
        if self.experience_engine:
            # Inject experience from all skills (agent decides which to use)
            experience_prompt = self.experience_engine.get_experience_prompt(
                "compliant-copy"
            )

        # Send to AgentScope ReActAgent
        response_text = await self.brain.chat(
            message=message.content,
            user_id=message.user_id,
            session_id=session_id,
            experience_prompt=experience_prompt,
        )

        return OutgoingMessage(
            content=response_text,
            target_user_id=message.user_id,
            target_chat_id=message.chat_id,
            source=message.source,
            metadata={"session_id": session_id},
        )
