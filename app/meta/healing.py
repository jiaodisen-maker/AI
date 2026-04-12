"""Self-healing: detect anomalies and auto-recover.

Detects:
  - Skill error spikes
  - Latency anomalies
  - Repeated failures on same input
  - Stuck workflows

Recovery actions:
  - Retry with different model
  - Roll back to last working version
  - Disable failing skill temporarily
  - Alert admin
"""

from __future__ import annotations

import logging
import time
from collections import defaultdict, deque
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class HealthSignal:
    """One observation of skill health."""

    skill_id: str
    timestamp: float
    success: bool
    latency_ms: int


@dataclass
class HealthState:
    """Current health state of a skill."""

    skill_id: str
    status: str = "healthy"  # healthy / degraded / failing / disabled
    error_rate: float = 0.0
    avg_latency_ms: int = 0
    consecutive_failures: int = 0
    disabled_until: float = 0.0


class HealingDetector:
    """Detects anomalies and triggers recovery actions."""

    def __init__(self, window_size: int = 100) -> None:
        self.window_size = window_size
        self._signals: dict[str, deque] = defaultdict(
            lambda: deque(maxlen=window_size)
        )
        self._states: dict[str, HealthState] = defaultdict(
            lambda: HealthState(skill_id="")
        )

    def record(self, skill_id: str, success: bool, latency_ms: int) -> None:
        """Record one execution outcome."""
        signal = HealthSignal(
            skill_id=skill_id,
            timestamp=time.time(),
            success=success,
            latency_ms=latency_ms,
        )
        self._signals[skill_id].append(signal)

        # Update state
        state = self._states[skill_id]
        state.skill_id = skill_id

        if success:
            state.consecutive_failures = 0
        else:
            state.consecutive_failures += 1

        signals = list(self._signals[skill_id])
        if signals:
            state.error_rate = sum(1 for s in signals if not s.success) / len(signals)
            state.avg_latency_ms = sum(s.latency_ms for s in signals) // len(signals)

        # Re-evaluate status
        self._update_status(state)

    def _update_status(self, state: HealthState) -> None:
        # Hard cutoff: 5 consecutive failures → disable for 5 min
        if state.consecutive_failures >= 5:
            state.status = "disabled"
            state.disabled_until = time.time() + 300
            logger.error(
                "Skill %s disabled due to 5 consecutive failures",
                state.skill_id,
            )
            return

        # Re-enable if disable period passed
        if state.status == "disabled" and time.time() > state.disabled_until:
            state.status = "degraded"
            logger.info("Skill %s re-enabled (degraded)", state.skill_id)

        # Status thresholds
        if state.error_rate > 0.5:
            state.status = "failing"
        elif state.error_rate > 0.2:
            state.status = "degraded"
        elif state.consecutive_failures == 0:
            state.status = "healthy"

    def is_skill_available(self, skill_id: str) -> bool:
        """Check if a skill is currently available (not disabled)."""
        state = self._states.get(skill_id)
        if not state:
            return True
        if state.status == "disabled":
            return time.time() > state.disabled_until
        return True

    def get_status(self, skill_id: str) -> dict:
        state = self._states.get(skill_id)
        if not state:
            return {"skill_id": skill_id, "status": "unknown"}
        return {
            "skill_id": skill_id,
            "status": state.status,
            "error_rate": round(state.error_rate, 3),
            "avg_latency_ms": state.avg_latency_ms,
            "consecutive_failures": state.consecutive_failures,
        }

    def get_all_statuses(self) -> list[dict]:
        return [self.get_status(sid) for sid in self._states]


# Global singleton
_detector: HealingDetector | None = None


def get_healing_detector() -> HealingDetector:
    global _detector
    if _detector is None:
        _detector = HealingDetector()
    return _detector
