"""Skill Factory: programmatically create Skills.

Three creation paths:
  1. From YAML definition (no Python required) — for operators
  2. From template + parameters — for common patterns
  3. From example pairs — Skill learned from input/output examples
"""

from __future__ import annotations

import logging
from typing import Any

from app.skills.yaml_skill import YAMLSkill

logger = logging.getLogger(__name__)


# Common templates that operators can fill in
SKILL_TEMPLATES = {
    "content_writer": {
        "category": "content",
        "model_preference": "overseas",
        "prompt_template": (
            "你是{role}。{instructions}\n"
            "用户输入: {{user_message}}\n"
            "请用中文输出{output_format}"
        ),
    },
    "data_analyst": {
        "category": "data",
        "model_preference": "local",
        "prompt_template": (
            "你是数据分析助手。任务: {task}\n"
            "可用指标: {{ontology_context}}\n"
            "用户问题: {{user_message}}"
        ),
    },
    "compliance_checker": {
        "category": "operation",
        "model_preference": "local",
        "prompt_template": (
            "你是合规审核员。审核标准: {standards}\n"
            "待审核内容: {{user_message}}\n"
            "输出: 通过/不通过 + 理由"
        ),
    },
}


class SkillFactory:
    """Factory for creating Skills programmatically."""

    def __init__(self, model_router: Any = None) -> None:
        self.model_router = model_router

    def from_template(
        self,
        skill_id: str,
        name: str,
        description: str,
        template: str,
        params: dict[str, str],
        triggers: list[str] | None = None,
    ) -> YAMLSkill:
        """Create a skill from a template + filled-in params."""
        if template not in SKILL_TEMPLATES:
            raise ValueError(f"Unknown template: {template}")

        tpl = SKILL_TEMPLATES[template]
        prompt = tpl["prompt_template"].format(**params)

        skill_def = {
            "id": skill_id,
            "name": name,
            "description": description,
            "category": tpl["category"],
            "model_preference": tpl["model_preference"],
            "triggers": triggers or [],
            "prompt_template": prompt,
        }
        return YAMLSkill(skill_def, self.model_router)

    def from_yaml(self, yaml_content: str) -> YAMLSkill:
        """Create a skill from a YAML string."""
        import yaml as yaml_lib
        skill_def = yaml_lib.safe_load(yaml_content)
        return YAMLSkill(skill_def, self.model_router)

    def from_examples(
        self,
        skill_id: str,
        name: str,
        description: str,
        examples: list[dict[str, str]],
        triggers: list[str] | None = None,
    ) -> YAMLSkill:
        """Create a few-shot skill from input/output examples.

        Args:
            examples: list of {"input": "...", "output": "..."}
        """
        prompt = "你需要按以下示例的风格回答用户问题:\n\n"
        for i, ex in enumerate(examples, 1):
            prompt += f"示例 {i}:\n输入: {ex['input']}\n输出: {ex['output']}\n\n"
        prompt += "用户输入: {user_message}\n输出:"

        skill_def = {
            "id": skill_id,
            "name": name,
            "description": description,
            "category": "content",
            "model_preference": "local",
            "triggers": triggers or [],
            "prompt_template": prompt,
        }
        return YAMLSkill(skill_def, self.model_router)

    @staticmethod
    def list_templates() -> list[str]:
        return list(SKILL_TEMPLATES.keys())
