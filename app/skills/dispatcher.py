"""Skill Dispatcher — the central routing hub.

ALL requests end up here. Routing modes:

  Fast track:   Trigger word → direct Skill (0 tokens)
  Agent loop:   AgentScope coordinator decides which Skills to call
  /deep:        LangChain Deep Agent for open-ended research
  /workflow:    Execute a named SOP from ontology
  /discuss:     Multi-agent group discussion via MsgHub
"""

from __future__ import annotations

import logging
import uuid
from typing import TYPE_CHECKING, Any

from app.skills.models import SkillInput
from app.skills.registry import SkillRegistry

if TYPE_CHECKING:
    from app.brain.agent import BrainAgent
    from app.brain.workflow import WorkflowEngine
    from app.memory.session import SessionMemory

logger = logging.getLogger(__name__)


class SkillDispatcher:
    """Routes messages to Skills. Skill is always the value center."""

    def __init__(
        self,
        registry: SkillRegistry,
        brain: BrainAgent | None = None,
        session_memory: SessionMemory | None = None,
        workflow_engine: WorkflowEngine | None = None,
    ) -> None:
        self.registry = registry
        self.brain = brain
        self.session_memory = session_memory
        self.workflow_engine = workflow_engine

    async def dispatch(
        self,
        message: str,
        user_id: str = "",
        session_id: str = "",
        source: str = "api",
    ) -> dict[str, Any]:
        """Dispatch a message. Returns content + metadata."""
        session_id = session_id or uuid.uuid4().hex

        # Store user message
        if self.session_memory:
            await self.session_memory.add_message(session_id, "user", message)

        # Route by command prefix
        msg = message.strip()

        if msg.startswith("/deep "):
            result = await self._deep_agent(msg[6:], user_id, session_id)
        elif msg.startswith("/workflow "):
            result = await self._run_workflow(msg[10:], user_id)
        elif msg.startswith("/discuss "):
            result = await self._multi_discuss(msg[9:], user_id)
        else:
            # Fast track: trigger word match
            skill = self.registry.find_by_trigger(message)
            if skill:
                logger.info("Fast track: %s", skill.meta().id)
                result = await self._execute_skill(
                    skill, message, user_id, session_id, source, mode="fast"
                )
            # Main path: Agent loop
            elif self.brain:
                logger.info("Main path: Agent loop")
                result = await self._agent_loop(
                    message, user_id, session_id, source
                )
            else:
                result = {
                    "content": "抱歉，我暂时无法处理您的请求。",
                    "skill_id": None,
                    "mode": "no_match",
                    "metadata": {},
                }

        # Store response
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
        """Execute a Skill through full BaseSkill.run() lifecycle."""
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
            "content": record.output.content
            if record.output.success
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
        """Main path: AgentScope coordinator decides what to do."""
        try:
            response = await self.brain.chat(
                message=message,
                user_id=user_id,
                session_id=session_id,
            )
            return {
                "content": response,
                "skill_id": None,
                "mode": "agent",
                "metadata": {},
            }
        except Exception as e:
            logger.error("Agent loop failed: %s", e)
            # Fallback to trigger match
            skill = self.registry.find_by_trigger(message)
            if skill:
                return await self._execute_skill(
                    skill, message, user_id, session_id, source, mode="fallback"
                )
            return {
                "content": f"处理请求时出错: {e}",
                "skill_id": None,
                "mode": "error",
                "metadata": {},
            }

    async def _deep_agent(
        self, query: str, user_id: str, session_id: str
    ) -> dict[str, Any]:
        """Deep Agent: /deep command → LangChain Deep Agent."""
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
            logger.warning("Deep Agent deps not installed, fallback")
            return await self._agent_loop(
                f"请深入分析：{query}", user_id, session_id, "api"
            )
        except Exception as e:
            logger.error("Deep Agent failed: %s", e)
            return {
                "content": f"深度分析出错: {e}",
                "skill_id": None,
                "mode": "deep_error",
                "metadata": {},
            }

    async def _run_workflow(
        self, workflow_name: str, user_id: str
    ) -> dict[str, Any]:
        """Execute a named SOP workflow: /workflow 新品上市文案流程."""
        if not self.workflow_engine:
            return {
                "content": "工作流引擎未初始化",
                "skill_id": None,
                "mode": "workflow_error",
                "metadata": {},
            }

        try:
            result = await self.workflow_engine.execute_workflow(
                workflow_name=workflow_name.strip(),
                initial_context={"user_id": user_id},
            )

            if "error" in result:
                return {
                    "content": f"工作流错误: {result['error']}",
                    "skill_id": None,
                    "mode": "workflow_error",
                    "metadata": {},
                }

            # Format workflow result
            lines = [f"工作流「{result['workflow']}」执行完成"]
            lines.append(
                f"步骤: {result['steps_completed']}/{result['steps_total']}"
            )
            for step in result.get("results", []):
                status = step.get("status", "unknown")
                icon = {"completed": "✓", "skipped": "⊘", "blocked": "✗",
                        "pending_approval": "⏳", "error": "✗"}.get(status, "?")
                lines.append(
                    f"  {icon} 步骤{step.get('step_id', '?')}: {status}"
                )
                if step.get("output"):
                    lines.append(f"    {str(step['output'])[:200]}")

            return {
                "content": "\n".join(lines),
                "skill_id": None,
                "mode": "workflow",
                "metadata": result,
            }
        except Exception as e:
            logger.error("Workflow failed: %s", e)
            return {
                "content": f"工作流执行出错: {e}",
                "skill_id": None,
                "mode": "workflow_error",
                "metadata": {},
            }

    async def _multi_discuss(
        self, topic: str, user_id: str
    ) -> dict[str, Any]:
        """Multi-agent discussion: /discuss 竞品降价应对策略."""
        if not self.brain:
            return {
                "content": "Agent 系统未初始化",
                "skill_id": None,
                "mode": "discuss_error",
                "metadata": {},
            }

        role_names = self.brain.role_agent_names
        if not role_names:
            return {
                "content": "没有可用的角色 Agent。请先通过本体创建角色。",
                "skill_id": None,
                "mode": "discuss_error",
                "metadata": {},
            }

        try:
            result = await self.brain.multi_agent_discuss(
                topic=topic.strip(),
                role_names=role_names,
            )
            return {
                "content": result,
                "skill_id": None,
                "mode": "discuss",
                "metadata": {"topic": topic, "participants": role_names},
            }
        except Exception as e:
            logger.error("Discussion failed: %s", e)
            return {
                "content": f"讨论出错: {e}",
                "skill_id": None,
                "mode": "discuss_error",
                "metadata": {},
            }
