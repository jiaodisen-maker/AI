"""Skill auto-optimization based on execution history.

Analyzes which prompt patterns lead to fewer human corrections,
and proposes refinements to skill prompts.
"""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


class SkillOptimizer:
    """Auto-optimize Skills based on usage patterns."""

    def __init__(self, experience_store: Any = None) -> None:
        self.store = experience_store

    def analyze_skill_health(self, skill_id: str) -> dict[str, Any]:
        """Compute health metrics for a skill.

        Health score factors:
          - Correction rate (lower is better)
          - Execution time stability
          - Pattern confidence trend
        """
        if not self.store:
            return {"error": "no store"}

        records = [
            r for r in getattr(self.store, "_records", [])
            if r.skill_id == skill_id
        ]

        if not records:
            return {
                "skill_id": skill_id,
                "health_score": None,
                "samples": 0,
            }

        total = len(records)
        corrections = sum(1 for r in records if r.was_edited)
        correction_rate = corrections / total if total else 0

        patterns = self.store.get_all_patterns(skill_id)
        avg_confidence = (
            sum(p.confidence for p in patterns) / len(patterns)
            if patterns else 0
        )

        # Health score: 0-100, higher is better
        health = max(
            0, 100 - correction_rate * 100 + avg_confidence * 20
        )
        health = min(100, int(health))

        return {
            "skill_id": skill_id,
            "samples": total,
            "correction_rate": round(correction_rate, 3),
            "avg_pattern_confidence": round(avg_confidence, 3),
            "health_score": health,
            "recommendation": self._recommend(health, correction_rate),
        }

    def propose_prompt_refinement(self, skill_id: str) -> str:
        """Generate a prompt refinement suggestion based on top patterns."""
        if not self.store:
            return ""

        reliable = self.store.get_reliable_patterns(skill_id)
        if not reliable:
            return "暂无可靠经验，建议继续累积"

        lines = ["建议在 system_prompt 中加入以下高置信度规则:\n"]
        for p in reliable[:5]:
            lines.append(f"- {p.pattern} (置信度: {p.confidence:.2f})")
        return "\n".join(lines)

    @staticmethod
    def _recommend(health: int, correction_rate: float) -> str:
        if health >= 80:
            return "技能表现良好，无需调整"
        if correction_rate > 0.5:
            return "修正率过高，建议人工审查 prompt"
        if health < 50:
            return "技能质量偏低，建议加入更多经验或调整 prompt"
        return "技能表现一般，可继续累积经验自动改善"
