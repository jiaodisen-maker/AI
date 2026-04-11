"""Skill routing: match intent to the best skill."""

from __future__ import annotations

import logging

from app.brain.intent import Intent
from app.skills.base import BaseSkill
from app.skills.registry import SkillRegistry

logger = logging.getLogger(__name__)


class SkillRouter:
    """Routes a recognized intent to the appropriate skill.

    Routing priority:
    1. Exact skill_id match from intent recognition
    2. Trigger keyword match from user message
    3. No match → return None (brain should handle gracefully)
    """

    def __init__(self, registry: SkillRegistry) -> None:
        self.registry = registry

    def route(self, intent: Intent, raw_message: str = "") -> BaseSkill | None:
        """Find the best matching skill for the given intent.

        Args:
            intent: Recognized intent from IntentRecognizer.
            raw_message: Original user message for fallback trigger matching.

        Returns:
            Matching skill instance or None.
        """
        # Priority 1: Exact skill_id from intent
        if intent.skill_id:
            skill = self.registry.get(intent.skill_id)
            if skill:
                logger.info(
                    "Routed to skill %s via intent (confidence=%.2f)",
                    intent.skill_id,
                    intent.confidence,
                )
                return skill
            logger.warning("Intent suggested skill %s but not found in registry", intent.skill_id)

        # Priority 2: Trigger keyword match
        if raw_message:
            skill = self.registry.find_by_trigger(raw_message)
            if skill:
                logger.info("Routed to skill %s via trigger match", skill.meta().id)
                return skill

        logger.info("No skill matched for intent: %s", intent.summary)
        return None
