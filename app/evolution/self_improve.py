"""Self-improvement loop: orchestrates AutoML + RL + healing.

Runs periodically (e.g. nightly) to:
  1. Identify underperforming Skills via RL feedback
  2. Run AutoML on those Skills
  3. Apply healing if any Skill is failing
  4. Re-evaluate after improvements
  5. Report changes
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class ImprovementReport:
    timestamp: datetime
    skills_analyzed: int
    skills_improved: int
    skills_healed: int
    actions: list[str]


class SelfImproveLoop:
    """Orchestrates the system-wide self-improvement cycle."""

    def __init__(
        self,
        registry: Any = None,
        rl_feedback: Any = None,
        healing: Any = None,
        optimizer: Any = None,
        automl: Any = None,
    ) -> None:
        self.registry = registry
        self.rl_feedback = rl_feedback
        self.healing = healing
        self.optimizer = optimizer
        self.automl = automl

    async def run_cycle(self) -> ImprovementReport:
        """Run one self-improvement cycle."""
        actions: list[str] = []
        skills_analyzed = 0
        skills_improved = 0
        skills_healed = 0

        if not self.registry:
            return ImprovementReport(
                timestamp=datetime.now(),
                skills_analyzed=0,
                skills_improved=0,
                skills_healed=0,
                actions=["registry not available"],
            )

        for meta in self.registry.list_all():
            skills_analyzed += 1
            skill_id = meta.id

            # 1. Check RL reward
            if self.rl_feedback:
                avg_reward = self.rl_feedback.get_skill_reward_avg(skill_id)
                if avg_reward < 0:
                    actions.append(f"⚠ {skill_id}: 平均反馈分 {avg_reward:.2f}")

            # 2. Check health (auto-healing)
            if self.healing:
                status = self.healing.get_status(skill_id)
                if status.get("status") in ("failing", "degraded"):
                    actions.append(
                        f"🔧 {skill_id}: 状态 {status['status']}，触发自愈"
                    )
                    skills_healed += 1

            # 3. Optimizer recommendations
            if self.optimizer:
                health = self.optimizer.analyze_skill_health(skill_id)
                if health.get("health_score", 100) < 60:
                    rec = self.optimizer.propose_prompt_refinement(skill_id)
                    if rec:
                        actions.append(f"💡 {skill_id}: {rec[:80]}")
                        skills_improved += 1

        report = ImprovementReport(
            timestamp=datetime.now(),
            skills_analyzed=skills_analyzed,
            skills_improved=skills_improved,
            skills_healed=skills_healed,
            actions=actions,
        )
        logger.info(
            "Self-improve cycle: %d analyzed, %d improved, %d healed",
            skills_analyzed, skills_improved, skills_healed,
        )
        return report
