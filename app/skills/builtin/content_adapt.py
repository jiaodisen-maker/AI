"""内容适配 Skill — 一篇内容适配多平台.

将一篇文案/文章自动改写为适配不同平台的版本：
小红书（种草风）、抖音（口播风）、公众号（深度风）、京东（卖点风）。
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

ADAPT_PROMPT = """\
你是多平台内容适配专家。

将用户提供的内容改写为适配以下平台的版本：

1. 小红书版：口语化、第一人称、分享体验、300-500字、带话题标签
2. 抖音版：短视频脚本、开头3秒抓注意力、150-300字、引导互动
3. 公众号版：深度文章、讲故事、分段清晰、800-1500字
4. 京东版：详情页、卖点前置、参数清晰、品质背书

每个版本前标注平台名。遵守保健品广告法。

{experience_prompt}"""


class ContentAdaptSkill(BaseSkill):
    """一篇内容多平台适配技能。"""

    def __init__(self, model_router: ModelRouter) -> None:
        self.model_router = model_router

    def meta(self) -> SkillMeta:
        return SkillMeta(
            id="content-adapt",
            name="多平台适配",
            description="将一篇内容自动改写为小红书/抖音/公众号/京东等多平台版本",
            category=SkillCategory.CONTENT,
            version="1.0.0",
            triggers=[
                "适配", "改写", "多平台", "转成",
                "各平台版本", "全平台",
            ],
            model_preference=ModelPreference.OVERSEAS,
        )

    def ontology_needs(self) -> list[str]:
        return ["health_supplements"]

    async def execute(self, skill_input: SkillInput) -> SkillOutput:
        experience = skill_input.context.get("experience_prompt", "")

        request = ChatRequest(
            messages=[
                ChatMessage(
                    role=Role.SYSTEM,
                    content=ADAPT_PROMPT.format(experience_prompt=experience),
                ),
                ChatMessage(role=Role.USER, content=skill_input.user_message),
            ],
            model_preference="overseas",
            temperature=0.8,
            max_tokens=4096,
        )

        response = await self.model_router.chat(request)
        return SkillOutput(success=True, content=response.content)
