"""Skill Dispatcher — the central routing hub.

ALL requests end up here. Three modes:

  Fast track:  Trigger word match → direct Skill execution (0 tokens)
  Main path:   AgentScope Agent loop → model decides which Skills to call
  /deep:       User-triggered deep research → LangChain Deep Agent

The model decides complexity. We don't classify for it.
"""

from __future__ import annotations

import logging
import uuid
from typing import TYPE_CHECKING, Any

from app.skills.models import SkillInput
from app.skills.registry import SkillRegistry

if TYPE_CHECKING:
    from app.brain.agent import BrainAgent
    from app.memory.session import SessionMemory

logger = logging.getLogger(__name__)


class SkillDispatcher:
    """Routes messages to Skills. Skill is always the value center.

    Agent decides what to do. Skill decides how to do it.
    """

    def __init__(
        self,
        registry: SkillRegistry,
        brain: BrainAgent | None = None,
        session_memory: SessionMemory | None = None,
    ) -> None:
        self.registry = registry
        self.brain = brain
        self.session_memory = session_memory

    async def dispatch(
        self,
        message: str,
        user_id: str = "",
        session_id: str = "",
        source: str = "api",
    ) -> dict[str, Any]:
        """Dispatch a message. Returns content + metadata."""
        session_id = session_id or uuid.uuid4().hex

        # Store user message in session memory
        if self.session_memory:
            await self.session_memory.add_message(session_id, "user", message)

        # Check for /deep command
        if message.strip().startswith("/deep "):
            deep_query = message.strip()[6:]
            result = await self._deep_agent(deep_query, user_id, session_id)
        else:
            # Fast track: trigger word match (0 tokens, optional optimization)
            skill = self.registry.find_by_trigger(message)
            if skill:
                logger.info("Fast track: %s", skill.meta().id)
                result = await self._execute_skill(
                    skill, message, user_id, session_id, source, mode="fast"
                )
            # Main path: Agent loop (model decides everything)
            elif self.brain:
                logger.info("Main path: Agent loop")
                result = await self._agent_loop(
                    message, user_id, session_id, source
                )
            else:
                # No agent available, try trigger match only
                result = {
                    "content": "抱歉，我暂时无法处理您的请求。请尝试更具体的描述。",
                    "skill_id": None,
                    "mode": "no_match",
                    "metadata": {},
                }

        # Store assistant response in session memory
        if self.session_memory:
            await self.session_memory.add_message(
                session_id, "assistant", result["content"]
            )

        return result

    async def _execute_skill(
        self,
        skill: Any,
        message: str,
        user_id: str,
        session_id: str,
        source: str,
        mode: str = "fast",
    ) -> dict[str, Any]:
        """Execute a Skill through the full BaseSkill.run() lifecycle."""
        skill_input = SkillInput(
            user_message=message,
            user_id=user_id,
            session_id=session_id,
            context={"source": source},
        )

        try:
            record = await skill.run(skill_input)
        except Exception as e:
            logger.error("Skill %s error: %s", skill.meta().id, e)
            return {
                "content": f"技能执行出错: {e}",
                "skill_id": skill.meta().id,
                "mode": mode,
                "metadata": {"error": str(e)},
            }

        return {
            "content": record.output.content if record.output.success
            else f"执行失败：{record.output.error}",
            "skill_id": skill.meta().id,
            "mode": mode,
            "metadata": {
                "execution_time_ms": record.execution_time_ms,
                **record.output.metadata,
            },
        }

    async def _agent_loop(
        self,
        message: str,
        user_id: str,
        session_id: str,
        source: str,
    ) -> dict[str, Any]:
        """Main path: AgentScope Agent loop decides which Skills to call."""
        experience_prompt = ""

        try:
            response = await self.brain.chat(
                message=message,
                user_id=user_id,
                session_id=session_id,
                experience_prompt=experience_prompt,
            )
            return {
                "content": response,
                "skill_id": None,
                "mode": "agent",
                "metadata": {},
            }
        except Exception as e:
            logger.error("Agent loop failed: %s", e)
            # Fallback: try trigger match
            skill = self.registry.find_by_trigger(message)
            if skill:
                return await self._execute_skill(
                    skill, message, user_id, session_id, source, mode="fallback"
                )
            return {
                "content": f"处理请求时出错: {e}",
                "skill_id": None,
                "mode": "error",
                "metadata": {"error": str(e)},
            }

    async def _deep_agent(
        self,
        query: str,
        user_id: str,
        session_id: str,
    ) -> dict[str, Any]:
        """Deep Agent: user-triggered deep research via /deep command.

        Uses LangChain Deep Agents for open-ended reasoning with:
        - File system backend (offload large results)
        - Context compression (long reasoning chains)
        - write_todos planning tool
        - Skills registered as tools

        Falls back to AgentScope if Deep Agent deps not available.
        """
        try:
            from app.brain.deep import run_deep_agent

            result = await run_deep_agent(
                query=query,
                skill_registry=self.registry,
                user_id=user_id,
                session_id=session_id,
            )
            return {
                "content": result,
                "skill_id": None,
                "mode": "deep",
                "metadata": {"query": query},
            }
        except ImportError:
            logger.warning("Deep Agent deps not installed, falling back to Agent loop")
            return await self._agent_loop(
                f"请深入分析：{query}", user_id, session_id, "api"
            )
        except Exception as e:
            logger.error("Deep Agent failed: %s", e)
            return {
                "content": f"深度分析出错: {e}",
                "skill_id": None,
                "mode": "deep_error",
                "metadata": {"error": str(e)},
            }
