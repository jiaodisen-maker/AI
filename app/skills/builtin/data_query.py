"""数据查询 Skill — 自然语言查数据.

用户用自然语言提问，Skill 将问题转化为结构化查询，
从本体获取指标定义和数据源信息。
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

QUERY_PROMPT = """\
你是数据分析助手。用户用自然语言提出数据查询需求。

请分析用户问题，输出：
1. 涉及的指标（如 GMV、ROI、转化率）
2. 涉及的维度（如 渠道、产品、时间）
3. 建议的 SQL 查询（基于常见数据表结构）
4. 数据解读建议

{ontology_context}

用中文回答，结构清晰。"""


class DataQuerySkill(BaseSkill):
    """自然语言数据查询技能。"""

    def __init__(self, model_router: ModelRouter) -> None:
        self.model_router = model_router

    def meta(self) -> SkillMeta:
        return SkillMeta(
            id="data-query",
            name="数据查询",
            description="用自然语言查询业务数据，支持销售、ROI、转化率等指标分析",
            category=SkillCategory.DATA,
            version="1.0.0",
            triggers=[
                "查数据", "查一下", "查询", "多少", "销量",
                "GMV", "ROI", "转化率", "数据分析",
            ],
            model_preference=ModelPreference.LOCAL,
        )

    def ontology_needs(self) -> list[str]:
        return ["data_definitions", "health_supplements"]

    async def execute(self, skill_input: SkillInput) -> SkillOutput:
        ontology_info = ""
        ontology = skill_input.context.get("ontology", {})
        if "data_definitions" in ontology:
            metrics = ontology["data_definitions"].get("metrics", {})
            ontology_info = "可用指标：\n" + "\n".join(
                f"- {name}: {info.get('chinese_name', '')} = {info.get('definition', '')}"
                for name, info in metrics.items()
            )

        request = ChatRequest(
            messages=[
                ChatMessage(
                    role=Role.SYSTEM,
                    content=QUERY_PROMPT.format(
                        ontology_context=ontology_info,
                    ),
                ),
                ChatMessage(role=Role.USER, content=skill_input.user_message),
            ],
            model_preference="local",
            temperature=0.3,
            max_tokens=2048,
        )

        response = await self.model_router.chat(request)
        return SkillOutput(success=True, content=response.content)
