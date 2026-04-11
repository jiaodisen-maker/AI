"""Skill registry: registration, discovery, and lookup."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.skills.base import BaseSkill
    from app.skills.models import SkillMeta

logger = logging.getLogger(__name__)


class SkillRegistry:
    """Central registry for all available skills.

    Supports lookup by skill ID or by trigger keyword matching.
    """

    def __init__(self) -> None:
        self._skills: dict[str, BaseSkill] = {}
        self._trigger_index: dict[str, str] = {}  # trigger_word → skill_id

    def register(self, skill: BaseSkill) -> None:
        """Register a skill instance."""
        meta = skill.meta()
        if meta.id in self._skills:
            logger.warning("Skill %s already registered, overwriting", meta.id)

        self._skills[meta.id] = skill

        for trigger in meta.triggers:
            self._trigger_index[trigger.lower()] = meta.id

        logger.info("Registered skill: %s (%s)", meta.id, meta.name)

    def get(self, skill_id: str) -> BaseSkill | None:
        """Get a skill by its ID."""
        return self._skills.get(skill_id)

    def find_by_trigger(self, text: str) -> BaseSkill | None:
        """Find a skill whose trigger word appears in the given text."""
        text_lower = text.lower()
        for trigger, skill_id in self._trigger_index.items():
            if trigger in text_lower:
                return self._skills.get(skill_id)
        return None

    def list_all(self) -> list[SkillMeta]:
        """List metadata of all registered skills."""
        return [skill.meta() for skill in self._skills.values()]

    def list_by_category(self, category: str) -> list[SkillMeta]:
        """List skills filtered by category."""
        return [
            skill.meta()
            for skill in self._skills.values()
            if skill.meta().category == category
        ]

    @property
    def count(self) -> int:
        return len(self._skills)
