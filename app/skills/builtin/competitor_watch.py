"""竞品监控 Skill — 分析竞品动态.

分析竞品的价格、活动、新品、文案变化，
提供差异化建议。
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

COMPETITOR_PROMPT = """\
你是保健品行业竞品分析专家。

用户询问竞品相关问题时，请分析：
1. 竞品基本信息（品牌、产品线、定位）
2. 竞品策略分析（价格、渠道、营销）
3. 与我司产品的对比
4. 差异化建议和应对策略

{ontology_context}

用中文回答，数据驱动，给出可执行的建议。"""


class CompetitorWatchSkill(BaseSkill):
    """竞品监控分析技能。"""

    def __init__(self, model_router: ModelRouter) -> None:
        self.model_router = model_router

    def meta(self) -> SkillMeta:
        return SkillMeta(
            id="competitor-watch",
            name="竞品分析",
            description="分析竞品动态：价格变化、营销策略、新品上市，提供差异化建议",
            category=SkillCategory.OPERATION,
            version="1.0.0",
            triggers=[
                "竞品", "竞争对手", "对手", "竞品分析",
                "Swisse", "汤臣倍健", "FANCL",
            ],
            model_preference=ModelPreference.LOCAL,
        )

    def ontology_needs(self) -> list[str]:
        return ["health_supplements"]

    async def execute(self, skill_input: SkillInput) -> SkillOutput:
        ontology_info = ""
        ontology = skill_input.context.get("ontology", {})
        if "health_supplements" in ontology:
            products = ontology["health_supplements"].get("product_categories", {})
            competitors = []
            for cat, info in products.items():
                for comp in info.get("competitors", []):
                    competitors.append(f"{comp['brand']}: {', '.join(comp.get('products', []))}")
            if competitors:
                ontology_info = "已知竞品：\n" + "\n".join(f"- {c}" for c in competitors)

        request = ChatRequest(
            messages=[
                ChatMessage(
                    role=Role.SYSTEM,
                    content=COMPETITOR_PROMPT.format(ontology_context=ontology_info),
                ),
                ChatMessage(role=Role.USER, content=skill_input.user_message),
            ],
            model_preference="local",
            temperature=0.5,
            max_tokens=4096,
        )

        response = await self.model_router.chat(request)
        return SkillOutput(success=True, content=response.content)
