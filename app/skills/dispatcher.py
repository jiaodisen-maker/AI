"""Skill Dispatcher — the central routing hub.

ALL requests end up here. The dispatcher decides which Skill handles
the request, then runs it through the full Skill lifecycle.

Three-tier routing:
  Tier 1: Trigger word match (0 tokens, 0 latency)
  Tier 2: LLM intent classification (few tokens)
  Tier 3: Agent multi-skill orchestration (complex requests only)
"""

from __future__ import annotations

import logging
import uuid
from typing import TYPE_CHECKING, Any

from app.skills.models import SkillInput
from app.skills.registry import SkillRegistry

if TYPE_CHECKING:
    from app.brain.agent import BrainAgent
    from app.llm.router import ModelRouter

logger = logging.getLogger(__name__)


class SkillDispatcher:
    """Routes messages to Skills through three-tier intent matching.

    Skill is always the center. The dispatcher just answers:
    "Which Skill should handle this?"
    """

    def __init__(
        self,
        registry: SkillRegistry,
        model_router: ModelRouter | None = None,
        brain: BrainAgent | None = None,
    ) -> None:
        self.registry = registry
        self.model_router = model_router
        self.brain = brain  # Only used for Tier 3

    async def dispatch(
        self,
        message: str,
        user_id: str = "",
        session_id: str = "",
        source: str = "api",
    ) -> dict[str, Any]:
        """Dispatch a message to the appropriate Skill(s).

        Returns a dict with content, skill_id, tier, and metadata.
        """
        session_id = session_id or uuid.uuid4().hex

        # Tier 1: Trigger word match — fast, no LLM call
        skill = self.registry.find_by_trigger(message)
        if skill:
            logger.info("Tier 1 match: %s", skill.meta().id)
            return await self._execute_skill(
                skill, message, user_id, session_id, source, tier=1
            )

        # Tier 2: LLM intent classification — one LLM call
        if self.model_router:
            skill = await self._classify_intent(message)
            if skill:
                logger.info("Tier 2 match: %s", skill.meta().id)
                return await self._execute_skill(
                    skill, message, user_id, session_id, source, tier=2
                )

        # Tier 3: Agent orchestration — complex multi-step
        if self.brain:
            logger.info("Tier 3: Agent orchestration")
            try:
                response = await self.brain.chat(
                    message=message,
                    user_id=user_id,
                    session_id=session_id,
                )
                return {
                    "content": response,
                    "skill_id": None,
                    "tier": 3,
                    "metadata": {"mode": "agent_orchestration"},
                }
            except Exception as e:
                logger.error("Agent orchestration failed: %s", e)

        # No match at all — generic response
        return {
            "content": "抱歉，我暂时无法处理您的请求。请尝试更具体的描述。",
            "skill_id": None,
            "tier": 0,
            "metadata": {"mode": "no_match"},
        }

    async def _execute_skill(
        self,
        skill: Any,
        message: str,
        user_id: str,
        session_id: str,
        source: str,
        tier: int,
    ) -> dict[str, Any]:
        """Execute a Skill through the full lifecycle."""
        skill_input = SkillInput(
            user_message=message,
            user_id=user_id,
            session_id=session_id,
            context={"source": source},
        )

        try:
            # This goes through the FULL BaseSkill.run() lifecycle:
            # validate → guardrail → ontology → experience → execute
            # → guardrail → post_execute → record
            record = await skill.run(skill_input)
        except Exception as e:
            logger.error("Skill %s execution error: %s", skill.meta().id, e)
            return {
                "content": f"技能执行出错: {e}",
                "skill_id": skill.meta().id,
                "tier": tier,
                "metadata": {"error": str(e)},
            }

        return {
            "content": record.output.content if record.output.success
            else f"执行失败：{record.output.error}",
            "skill_id": skill.meta().id,
            "tier": tier,
            "metadata": {
                "execution_time_ms": record.execution_time_ms,
                **record.output.metadata,
            },
        }

    async def _classify_intent(self, message: str) -> Any:
        """Tier 2: Use LLM to classify which Skill matches."""
        if not self.model_router:
            return None

        from app.llm.models import ChatMessage, ChatRequest, Role

        skills_desc = "\n".join(
            f"- {m.id}: {m.name} ({m.description})"
            for m in self.registry.list_all()
        )

        request = ChatRequest(
            messages=[
                ChatMessage(
                    role=Role.SYSTEM,
                    content=f"你是意图分类器。根据用户消息，从以下技能中选择最匹配的。\n"
                    f"只返回技能 ID，如果没有匹配返回 none。\n\n{skills_desc}",
                ),
                ChatMessage(role=Role.USER, content=message),
            ],
            model_preference="local",
            temperature=0.1,
            max_tokens=50,
        )

        try:
            response = await self.model_router.chat(request)
            skill_id = response.content.strip().lower()
            return self.registry.get(skill_id)
        except Exception as e:
            logger.warning("Intent classification failed: %s", e)
            return None
