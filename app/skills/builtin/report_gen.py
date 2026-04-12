"""报表生成 Skill — 自动生成日报/周报/月报.

根据用户要求的报表类型和时间范围，
生成结构化的运营报表。
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

REPORT_PROMPT = """\
你是运营报表专家。根据用户要求生成结构化的运营报表。

报表要求：
1. 标题和时间范围
2. 核心指标概览（表格形式）
3. 重点数据分析（趋势、异常、对比）
4. 问题和风险提示
5. 建议动作

{ontology_context}
{experience_prompt}

用中文输出，格式清晰专业。"""


class ReportGenSkill(BaseSkill):
    """运营报表自动生成技能。"""

    def __init__(self, model_router: ModelRouter) -> None:
        self.model_router = model_router

    def meta(self) -> SkillMeta:
        return SkillMeta(
            id="report-gen",
            name="报表生成",
            description="自动生成日报/周报/月报，含核心指标、趋势分析、建议动作",
            category=SkillCategory.DATA,
            version="1.0.0",
            triggers=[
                "写报告", "生成报告", "报表", "日报", "周报", "月报",
                "运营报告", "数据报告", "经营分析",
            ],
            model_preference=ModelPreference.LOCAL,
        )

    def ontology_needs(self) -> list[str]:
        return ["data_definitions", "goals"]

    async def execute(self, skill_input: SkillInput) -> SkillOutput:
        ontology_info = ""
        ontology = skill_input.context.get("ontology", {})
        if "data_definitions" in ontology:
            metrics = ontology["data_definitions"].get("metrics", {})
            ontology_info = "报表可用指标：\n" + "\n".join(
                f"- {name}: {info.get('chinese_name', '')}"
                for name, info in metrics.items()
            )
        if "goals" in ontology:
            goals = ontology["goals"].get("company_goals", {})
            ontology_info += "\n\n公司目标：\n" + str(goals)[:500]

        experience = skill_input.context.get("experience_prompt", "")

        request = ChatRequest(
            messages=[
                ChatMessage(
                    role=Role.SYSTEM,
                    content=REPORT_PROMPT.format(
                        ontology_context=ontology_info,
                        experience_prompt=experience,
                    ),
                ),
                ChatMessage(role=Role.USER, content=skill_input.user_message),
            ],
            model_preference="local",
            temperature=0.5,
            max_tokens=4096,
        )

        response = await self.model_router.chat(request)
        return SkillOutput(success=True, content=response.content)
