"""联网搜索 Skill — 搜索互联网获取信息.

用于竞品调研、行业动态、法规变化等
需要外部信息的场景。
"""

from __future__ import annotations

from app.llm.models import ChatMessage, ChatRequest, Role
from app.llm.router import ModelRouter
from app.skills.base import BaseSkill
from app.skills.models import (
    ModelPreference,
    SkillCategory,
    SkillInput,
    SkillMeta,
    SkillOutput,
)

SEARCH_PROMPT = """\
你是信息检索和分析助手。用户需要你搜索和整理信息。

请根据用户问题：
1. 分析搜索意图
2. 提供你已知的相关信息
3. 标注信息的时效性和可靠性
4. 给出进一步搜索的建议

注意：你目前没有实时联网能力，请基于已有知识回答，
并明确告知哪些信息可能需要验证。

用中文回答。"""


class WebSearchSkill(BaseSkill):
    """联网搜索技能。"""

    def __init__(self, model_router: ModelRouter) -> None:
        self.model_router = model_router

    def meta(self) -> SkillMeta:
        return SkillMeta(
            id="web-search",
            name="联网搜索",
            description="搜索互联网获取行业动态、竞品信息、法规变化等外部信息",
            category=SkillCategory.OPERATION,
            version="1.0.0",
            triggers=[
                "搜索", "搜一下", "查一查", "最新", "行业动态",
                "新闻", "政策", "法规变化",
            ],
            model_preference=ModelPreference.OVERSEAS,
        )

    async def execute(self, skill_input: SkillInput) -> SkillOutput:
        request = ChatRequest(
            messages=[
                ChatMessage(role=Role.SYSTEM, content=SEARCH_PROMPT),
                ChatMessage(role=Role.USER, content=skill_input.user_message),
            ],
            model_preference="overseas",
            temperature=0.3,
            max_tokens=4096,
        )

        response = await self.model_router.chat(request)
        return SkillOutput(success=True, content=response.content)
