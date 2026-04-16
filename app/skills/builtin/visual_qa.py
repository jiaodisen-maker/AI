"""Visual QA Skill — answer questions about an image.

E.g. "这张产品包装上的成分表是否合规？"
"""

from __future__ import annotations

from app.llm.router import ModelRouter
from app.multimodal.processors import ImageProcessor
from app.skills.base import BaseSkill
from app.skills.models import (
    SkillCategory,
    SkillInput,
    SkillMeta,
    SkillOutput,
)


class VisualQASkill(BaseSkill):
    """Visual question answering for images (product photos, packaging)."""

    def __init__(self, model_router: ModelRouter) -> None:
        self.model_router = model_router
        self.image = ImageProcessor(model_router)

    def meta(self) -> SkillMeta:
        return SkillMeta(
            id="visual-qa",
            name="图像理解",
            description="分析产品图、包装照片、截图等，回答相关问题",
            category=SkillCategory.OPERATION,
            triggers=["看图", "图像", "图片", "包装照", "截图分析"],
        )

    async def execute(self, skill_input: SkillInput) -> SkillOutput:
        image_path = skill_input.parameters.get("image_path", "")
        if not image_path:
            return SkillOutput(
                success=False,
                error="缺少 image_path 参数",
            )

        description = await self.image.describe(image_path)
        return SkillOutput(
            success=True,
            content=f"图像分析结果:\n{description}\n\n用户问题: {skill_input.user_message}",
            metadata={"image_path": image_path},
        )
