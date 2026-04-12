"""YAML-defined Skill: define new skills without writing Python.

Operators can create new skills by writing a YAML file like:

  id: weekly-summary
  name: 周报摘要
  description: 总结本周亮点
  category: content
  triggers: [周报摘要, 总结亮点]
  model_preference: local
  ontology_needs: [data_definitions]
  prompt_template: |
    你是周报摘要专家。基于以下指标，写一段简短的周报摘要。
    {ontology_context}
    用户输入: {user_message}
"""

from __future__ import annotations

from typing import Any

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


class YAMLSkill(BaseSkill):
    """A Skill defined entirely by a YAML configuration."""

    def __init__(
        self,
        skill_def: dict[str, Any],
        model_router: ModelRouter | None = None,
    ) -> None:
        self._def = skill_def
        self.model_router = model_router

    def meta(self) -> SkillMeta:
        return SkillMeta(
            id=self._def.get("id", "unknown-yaml"),
            name=self._def.get("name", "未命名 YAML 技能"),
            description=self._def.get("description", ""),
            category=SkillCategory(self._def.get("category", "content")),
            version=self._def.get("version", "1.0.0"),
            triggers=self._def.get("triggers", []),
            parameters=self._def.get("parameters", {}),
            model_preference=ModelPreference(
                self._def.get("model_preference", "local")
            ),
        )

    def ontology_needs(self) -> list[str]:
        return self._def.get("ontology_needs", [])

    async def execute(self, skill_input: SkillInput) -> SkillOutput:
        if not self.model_router:
            return SkillOutput(success=False, error="model_router 未配置")

        prompt_template = self._def.get(
            "prompt_template", "{user_message}"
        )

        # Build ontology context from injected data
        ontology = skill_input.context.get("ontology", {})
        ontology_context = ""
        for dim, data in ontology.items():
            ontology_context += f"\n[{dim}]\n{str(data)[:500]}\n"

        experience = skill_input.context.get("experience_prompt", "")

        try:
            system_prompt = prompt_template.format(
                user_message=skill_input.user_message,
                ontology_context=ontology_context,
                experience_prompt=experience,
                **skill_input.parameters,
            )
        except KeyError as e:
            return SkillOutput(
                success=False,
                error=f"prompt_template 缺少参数: {e}",
            )

        request = ChatRequest(
            messages=[
                ChatMessage(role=Role.SYSTEM, content=system_prompt),
                ChatMessage(role=Role.USER, content=skill_input.user_message),
            ],
            model_preference=self._def.get("model_preference", "local"),
            temperature=self._def.get("temperature", 0.7),
            max_tokens=self._def.get("max_tokens", 2048),
        )

        try:
            response = await self.model_router.chat(request)
            return SkillOutput(
                success=True,
                content=response.content,
                metadata={"yaml_skill": True},
            )
        except Exception as e:
            return SkillOutput(success=False, error=str(e))
