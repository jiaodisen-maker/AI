"""Meta-learning analyzer.

Analyzes execution history across all Skills to find:
  - Cross-skill patterns ("修改文案后总会查合规")
  - User behavior patterns
  - Skill performance trends
  - Knowledge transfer opportunities (pattern from Skill A useful for Skill B)
"""

from __future__ import annotations

import logging
from collections import Counter, defaultdict
from typing import Any

logger = logging.getLogger(__name__)


class MetaAnalyzer:
    """Analyzes patterns across Skills to find meta-knowledge."""

    def __init__(self, experience_store: Any = None) -> None:
        self.store = experience_store

    def analyze_skill_sequences(self, limit: int = 1000) -> list[dict]:
        """Find common skill execution sequences across users.

        E.g. "用户调用 compliant-copy 后 80% 概率会调用 compliance-check"
        """
        if not self.store:
            return []

        # Group records by user/session, sorted by time
        sessions: dict[str, list[str]] = defaultdict(list)
        for record in self._get_recent_records(limit):
            session_id = record.input_context.get("session_id", "default")
            sessions[session_id].append(record.skill_id)

        # Count consecutive skill pairs
        pair_counter: Counter = Counter()
        for skills in sessions.values():
            for i in range(len(skills) - 1):
                pair_counter[(skills[i], skills[i + 1])] += 1

        return [
            {"sequence": [a, b], "count": count}
            for (a, b), count in pair_counter.most_common(20)
        ]

    def analyze_user_patterns(self) -> dict[str, Any]:
        """Find patterns in how users interact with the system."""
        if not self.store:
            return {}

        records = self._get_recent_records(1000)
        skill_usage: Counter = Counter()
        correction_count: Counter = Counter()

        for r in records:
            skill_usage[r.skill_id] += 1
            if r.was_edited:
                correction_count[r.skill_id] += 1

        return {
            "top_skills": skill_usage.most_common(10),
            "correction_rates": {
                skill: corrections / skill_usage[skill]
                for skill, corrections in correction_count.items()
                if skill_usage[skill] > 0
            },
            "total_executions": len(records),
        }

    def find_knowledge_transfer_candidates(
        self, source_skill: str, target_skill: str
    ) -> list[str]:
        """Find experience patterns from source_skill that might apply to target_skill.

        E.g. "小红书文案要口语化" learned from compliant-copy
        might apply to content-adapt as well.
        """
        if not self.store:
            return []

        source_patterns = self.store.get_all_patterns(source_skill)

        # Simple heuristic: pattern is generic if it doesn't mention specifics
        generic_patterns = []
        for p in source_patterns:
            text = p.pattern.lower()
            # Generic if mentions general concepts, not specific products
            if not any(specific in text for specific in [
                "胶原蛋白", "辅酶", "益生菌", source_skill,
            ]):
                generic_patterns.append(p.pattern)

        return generic_patterns

    def _get_recent_records(self, limit: int) -> list:
        """Get recent records, fall back gracefully if store API differs."""
        try:
            if hasattr(self.store, "_records"):
                return self.store._records[-limit:]
            return []
        except Exception:
            return []
