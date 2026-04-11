"""Message router: the central pipeline connecting channels to the brain."""

from __future__ import annotations

import logging
import uuid
from typing import TYPE_CHECKING

from app.channels.models import IncomingMessage, OutgoingMessage
from app.skills.models import SkillInput

if TYPE_CHECKING:
    from app.brain.intent import IntentRecognizer
    from app.brain.router import SkillRouter
    from app.experience.engine import ExperienceEngine
    from app.llm.router import ModelRouter

logger = logging.getLogger(__name__)


class MessageRouter:
    """Routes incoming messages through the full pipeline:

    Message → Intent Recognition → Skill Routing → Skill Execution → Response

    This is the central orchestrator connecting all layers.
    """

    def __init__(
        self,
        intent_recognizer: IntentRecognizer,
        skill_router: SkillRouter,
        experience_engine: ExperienceEngine,
        model_router: ModelRouter,
    ) -> None:
        self.intent_recognizer = intent_recognizer
        self.skill_router = skill_router
        self.experience_engine = experience_engine
        self.model_router = model_router

    async def handle(self, message: IncomingMessage) -> OutgoingMessage:
        """Process an incoming message through the full pipeline.

        Returns an outgoing message ready to be sent back.
        """
        session_id = message.session_id or uuid.uuid4().hex

        logger.info(
            "Processing message from %s [%s]: %s",
            message.user_id,
            message.source,
            message.content[:100],
        )

        # Step 1: Recognize intent
        available_skills = self._get_skills_for_intent()
        intent = await self.intent_recognizer.recognize(message.content, available_skills)

        logger.info(
            "Intent: skill=%s confidence=%.2f summary=%s",
            intent.skill_id,
            intent.confidence,
            intent.summary,
        )

        # Step 2: Route to skill
        skill = self.skill_router.route(intent, raw_message=message.content)

        if not skill:
            # No matching skill — generic AI response
            return await self._generic_response(message)

        # Step 3: Build skill input with experience injection
        experience_prompt = self.experience_engine.get_experience_prompt(skill.meta().id)
        skill_input = SkillInput(
            user_message=message.content,
            parameters=intent.parameters,
            user_id=message.user_id,
            session_id=session_id,
            context={
                "experience_prompt": experience_prompt,
                "source": message.source,
                "chat_id": message.chat_id,
            },
        )

        # Step 4: Execute skill
        record = await skill.run(skill_input)

        # Step 5: Record execution for experience learning
        await self.experience_engine.record_execution(
            skill_id=skill.meta().id,
            input_context={"user_message": message.content, **intent.parameters},
            ai_output=record.output.content,
            model_used=record.model_used,
        )

        # Step 6: Build response
        if record.output.success:
            content = record.output.content
        else:
            content = f"执行失败：{record.output.error}"

        return OutgoingMessage(
            content=content,
            target_user_id=message.user_id,
            target_chat_id=message.chat_id,
            source=message.source,
            metadata={
                "skill_id": skill.meta().id,
                "execution_time_ms": record.execution_time_ms,
            },
        )

    async def _generic_response(self, message: IncomingMessage) -> OutgoingMessage:
        """Handle messages that don't match any skill with a generic AI response."""
        from app.llm.models import ChatMessage, ChatRequest, Role

        request = ChatRequest(
            messages=[
                ChatMessage(
                    role=Role.SYSTEM,
                    content="你是企业 AI 助手。如果用户的问题可以用某个技能解决，引导他们使用。"
                    "否则，尽力回答他们的问题。保持专业、简洁。",
                ),
                ChatMessage(role=Role.USER, content=message.content),
            ],
            model_preference="local",
            temperature=0.7,
        )

        try:
            response = await self.model_router.chat(request)
            content = response.content
        except Exception as e:
            logger.error("Generic response failed: %s", e)
            content = "抱歉，我暂时无法处理您的请求。请稍后重试。"

        return OutgoingMessage(
            content=content,
            target_user_id=message.user_id,
            target_chat_id=message.chat_id,
            source=message.source,
        )

    def _get_skills_for_intent(self) -> list[dict]:
        """Get skill metadata formatted for intent recognition."""
        return [
            {
                "id": meta.id,
                "name": meta.name,
                "description": meta.description,
                "triggers": meta.triggers,
            }
            for meta in self.skill_router.registry.list_all()
        ]
