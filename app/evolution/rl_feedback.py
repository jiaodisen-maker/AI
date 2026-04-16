"""Reinforcement learning from user corrections (RLHF-lite).

Treats user corrections as the reward signal:
  - Output accepted as-is        → reward = +1.0
  - Output minor edits            → reward = +0.5
  - Output major edits            → reward = -0.5
  - Output rejected outright      → reward = -1.0
"""

from __future__ import annotations

import logging
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime

logger = logging.getLogger(__name__)


@dataclass
class FeedbackRecord:
    skill_id: str
    user_id: str
    output: str
    edited_output: str | None
    reward: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)


class RLFeedback:
    """Collects and learns from user feedback signals."""

    def __init__(self) -> None:
        self._records: list[FeedbackRecord] = []
        self._skill_rewards: dict[str, list[float]] = defaultdict(list)

    def record_feedback(
        self,
        skill_id: str,
        user_id: str,
        output: str,
        edited_output: str | None = None,
        rejected: bool = False,
    ) -> float:
        """Record user feedback and compute reward."""
        reward = self._compute_reward(output, edited_output, rejected)
        record = FeedbackRecord(
            skill_id=skill_id,
            user_id=user_id,
            output=output,
            edited_output=edited_output,
            reward=reward,
        )
        self._records.append(record)
        self._skill_rewards[skill_id].append(reward)
        # Cap to last 5000 records
        if len(self._records) > 5000:
            self._records = self._records[-2500:]
        return reward

    def _compute_reward(
        self,
        output: str,
        edited: str | None,
        rejected: bool,
    ) -> float:
        if rejected:
            return -1.0
        if edited is None or edited == output:
            return 1.0
        # Compute edit distance ratio
        if not output:
            return 0.0
        common = sum(1 for a, b in zip(output, edited) if a == b)
        ratio = common / max(len(output), len(edited))
        if ratio > 0.9:
            return 0.5  # minor edits
        return -0.5  # major edits

    def get_skill_reward_avg(self, skill_id: str) -> float:
        """Average reward for a skill (recent)."""
        rewards = self._skill_rewards.get(skill_id, [])
        if not rewards:
            return 0.0
        recent = rewards[-100:]
        return sum(recent) / len(recent)

    def get_top_skills(self, n: int = 5) -> list[tuple[str, float]]:
        """Skills with highest average reward."""
        scores = [
            (skill, self.get_skill_reward_avg(skill))
            for skill in self._skill_rewards
        ]
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:n]

    def get_failing_skills(self, threshold: float = 0.0) -> list[tuple[str, float]]:
        """Skills with reward below threshold (need attention)."""
        scores = [
            (skill, self.get_skill_reward_avg(skill))
            for skill in self._skill_rewards
        ]
        return [s for s in scores if s[1] < threshold]


# Global singleton
_rl: RLFeedback | None = None


def get_rl_feedback() -> RLFeedback:
    global _rl
    if _rl is None:
        _rl = RLFeedback()
    return _rl
