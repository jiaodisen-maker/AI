"""Intent recognition: parse user message into structured intent."""

from __future__ import annotations

import json
import logging
from typing import Any

from pydantic import BaseModel

from app.llm.models import ChatMessage, ChatRequest, Role
from app.llm.router import ModelRouter

logger = logging.getLogger(__name__)

INTENT_SYSTEM_PROMPT = """你是一个意图识别引擎。分析用户消息，提取以下信息：

1. skill_id: 最匹配的技能ID（从可用技能列表中选择，如果没有匹配返回空字符串）
2. parameters: 提取的参数（JSON 对象）
3. confidence: 置信度 0-1
4. summary: 一句话概括用户意图

可用技能列表：
{skills_description}

请以 JSON 格式返回，不要包含其他内容：
{{"skill_id": "...", "parameters": {{}}, "confidence": 0.0, "summary": "..."}}"""


class Intent(BaseModel):
    """Parsed user intent."""

    skill_id: str = ""
    parameters: dict[str, Any] = {}
    confidence: float = 0.0
    summary: str = ""


class IntentRecognizer:
    """Uses LLM to recognize user intent and map to skills."""

    def __init__(self, model_router: ModelRouter) -> None:
        self.model_router = model_router

    async def recognize(self, message: str, available_skills: list[dict]) -> Intent:
        """Recognize intent from a user message.

        Args:
            message: Raw user message text.
            available_skills: List of skill metadata dicts for context.

        Returns:
            Parsed Intent object.
        """
        skills_desc = "\n".join(
            f"- {s['id']}: {s['name']} — {s['description']}"
            f" (触发词: {', '.join(s.get('triggers', []))})"
            for s in available_skills
        )

        system_prompt = INTENT_SYSTEM_PROMPT.format(skills_description=skills_desc)

        request = ChatRequest(
            messages=[
                ChatMessage(role=Role.SYSTEM, content=system_prompt),
                ChatMessage(role=Role.USER, content=message),
            ],
            model_preference="local",  # Intent recognition uses local model for speed
            temperature=0.1,
            max_tokens=512,
        )

        try:
            response = await self.model_router.chat(request)
            return self._parse_response(response.content)
        except Exception as e:
            logger.error("Intent recognition failed: %s", e)
            return Intent(summary=f"识别失败: {e}")

    def _parse_response(self, content: str) -> Intent:
        """Parse LLM response into Intent object."""
        # Strip markdown code fences if present
        content = content.strip()
        if content.startswith("```"):
            content = content.split("\n", 1)[-1]
        if content.endswith("```"):
            content = content.rsplit("```", 1)[0]
        content = content.strip()

        try:
            data = json.loads(content)
            return Intent(**data)
        except (json.JSONDecodeError, TypeError) as e:
            logger.warning("Failed to parse intent response: %s — raw: %s", e, content[:200])
            return Intent(summary=content[:200])
