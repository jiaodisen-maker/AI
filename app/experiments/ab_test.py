"""A/B testing framework for Skills.

Allows running two variants of a skill (different prompts, models, params)
against real users, then comparing outcomes.

Variant assignment is sticky per user (same user always sees same variant).
"""

from __future__ import annotations

import hashlib
import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class Variant:
    """One arm of an A/B test."""

    id: str  # "A" or "B" or "control"
    name: str
    skill_overrides: dict[str, Any] = field(default_factory=dict)
    weight: float = 0.5  # traffic share


@dataclass
class ABTestResult:
    """Outcome record for one execution."""

    variant_id: str
    user_id: str
    success: bool
    user_corrected: bool = False
    timestamp: datetime = field(default_factory=datetime.now)


class ABTest:
    """A/B test for a skill."""

    def __init__(
        self,
        test_id: str,
        skill_id: str,
        variants: list[Variant],
    ) -> None:
        self.test_id = test_id
        self.skill_id = skill_id
        self.variants = variants
        self._results: list[ABTestResult] = []
        self.started_at = datetime.now()

    def get_variant_for_user(self, user_id: str) -> Variant:
        """Sticky assignment: same user always gets same variant.

        Uses hash of user_id for deterministic distribution.
        """
        if not self.variants:
            raise ValueError("No variants defined")

        if not user_id:
            return self.variants[0]

        # Hash to [0, 1)
        hash_val = int(hashlib.md5(user_id.encode()).hexdigest(), 16)
        bucket = (hash_val % 10000) / 10000.0

        cumulative = 0.0
        for variant in self.variants:
            cumulative += variant.weight
            if bucket < cumulative:
                return variant
        return self.variants[-1]

    def record_result(
        self,
        variant_id: str,
        user_id: str,
        success: bool,
        user_corrected: bool = False,
    ) -> None:
        """Record an outcome."""
        self._results.append(ABTestResult(
            variant_id=variant_id,
            user_id=user_id,
            success=success,
            user_corrected=user_corrected,
        ))

    def get_metrics(self) -> dict[str, Any]:
        """Compute metrics per variant."""
        metrics = {}
        for variant in self.variants:
            variant_results = [r for r in self._results if r.variant_id == variant.id]
            total = len(variant_results)
            if total == 0:
                metrics[variant.id] = {
                    "name": variant.name,
                    "total": 0,
                    "success_rate": 0,
                    "correction_rate": 0,
                }
                continue

            success = sum(1 for r in variant_results if r.success)
            corrected = sum(1 for r in variant_results if r.user_corrected)

            metrics[variant.id] = {
                "name": variant.name,
                "total": total,
                "success_rate": success / total,
                "correction_rate": corrected / total,
                "human_quality_score": (success - corrected * 0.5) / total,
            }
        return {
            "test_id": self.test_id,
            "skill_id": self.skill_id,
            "started_at": self.started_at.isoformat(),
            "variants": metrics,
        }

    def get_winner(self) -> str | None:
        """Return the variant ID with the highest quality score."""
        metrics = self.get_metrics()["variants"]
        if not metrics:
            return None
        best = max(
            metrics.items(),
            key=lambda kv: kv[1].get("human_quality_score", 0),
        )
        return best[0] if best[1]["total"] > 10 else None  # need data
