"""Task planner: decompose complex requests into ordered skill calls."""

from __future__ import annotations

import json
import logging
from typing import Any

from pydantic import BaseModel

from app.llm.models import ChatMessage, ChatRequest, Role
from app.llm.router import ModelRouter

logger = logging.getLogger(__name__)

PLANNER_SYSTEM_PROMPT = """你是一个任务规划器。用户可能提出需要多个步骤的复杂请求。
将请求分解为有序的步骤，每个步骤对应一个技能调用。

可用技能：
{skills_description}

以 JSON 数组格式返回步骤列表：
[
  {{"step": 1, "skill_id": "...", "description": "...", "parameters": {{}}, "depends_on": []}},
  {{"step": 2, "skill_id": "...", "description": "...", "parameters": {{}}, "depends_on": [1]}}
]

如果只需要一个步骤，返回只有一个元素的数组。
如果请求无法分解为已有技能，返回空数组 []。"""


class PlanStep(BaseModel):
    """A single step in a task plan."""

    step: int
    skill_id: str
    description: str = ""
    parameters: dict[str, Any] = {}
    depends_on: list[int] = []


class TaskPlan(BaseModel):
    """An ordered sequence of skill invocations."""

    steps: list[PlanStep] = []
    raw_request: str = ""

    @property
    def is_single_step(self) -> bool:
        return len(self.steps) == 1

    @property
    def is_empty(self) -> bool:
        return len(self.steps) == 0


class TaskPlanner:
    """Decomposes complex user requests into multi-step skill execution plans."""

    def __init__(self, model_router: ModelRouter) -> None:
        self.model_router = model_router

    async def plan(self, message: str, available_skills: list[dict]) -> TaskPlan:
        """Create an execution plan for a user request.

        Args:
            message: User's request text.
            available_skills: List of skill metadata dicts.

        Returns:
            TaskPlan with ordered steps.
        """
        skills_desc = "\n".join(
            f"- {s['id']}: {s['name']} — {s['description']}"
            for s in available_skills
        )

        request = ChatRequest(
            messages=[
                ChatMessage(role=Role.SYSTEM, content=PLANNER_SYSTEM_PROMPT.format(
                    skills_description=skills_desc
                )),
                ChatMessage(role=Role.USER, content=message),
            ],
            model_preference="local",
            temperature=0.1,
            max_tokens=1024,
        )

        try:
            response = await self.model_router.chat(request)
            steps = self._parse_response(response.content)
            return TaskPlan(steps=steps, raw_request=message)
        except Exception as e:
            logger.error("Task planning failed: %s", e)
            return TaskPlan(raw_request=message)

    def _parse_response(self, content: str) -> list[PlanStep]:
        """Parse LLM response into plan steps."""
        content = content.strip()
        if content.startswith("```"):
            content = content.split("\n", 1)[-1]
        if content.endswith("```"):
            content = content.rsplit("```", 1)[0]
        content = content.strip()

        try:
            data = json.loads(content)
            if isinstance(data, list):
                return [PlanStep(**step) for step in data]
        except (json.JSONDecodeError, TypeError) as e:
            logger.warning("Failed to parse plan response: %s", e)

        return []
