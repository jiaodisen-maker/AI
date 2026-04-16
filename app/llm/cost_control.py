"""LLM cost control: per-task budget + loop detection.

Prevents runaway agent loops from burning the budget.
A misconfigured loop can produce thousands of LLM calls per minute,
costing $2000+/hour. This module enforces hard limits.
"""

from __future__ import annotations

import logging
import time
from collections import defaultdict
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class BudgetConfig:
    """Budget limits per task / user / time window."""

    per_task_max_tokens: int = 50000
    per_task_max_calls: int = 20
    per_user_daily_tokens: int = 500000
    loop_detect_window_seconds: int = 60
    loop_detect_max_calls: int = 30


@dataclass
class TaskBudget:
    """Tracks budget for a single task."""

    task_id: str
    started_at: float = field(default_factory=time.time)
    tokens_used: int = 0
    calls_made: int = 0
    blocked: bool = False
    block_reason: str = ""


class CostController:
    """Enforces LLM cost limits with hard cutoffs.

    Three-layer protection:
      1. Per-task token + call cap
      2. Per-user daily token cap
      3. Loop detection (too many calls in short window)
    """

    def __init__(self, config: BudgetConfig | None = None) -> None:
        self.config = config or BudgetConfig()
        self._tasks: dict[str, TaskBudget] = {}
        self._user_daily: dict[str, dict] = defaultdict(
            lambda: {"date": "", "tokens": 0}
        )
        self._call_history: dict[str, list[float]] = defaultdict(list)

    def start_task(self, task_id: str) -> TaskBudget:
        """Start tracking a new task."""
        budget = TaskBudget(task_id=task_id)
        self._tasks[task_id] = budget
        return budget

    def check_and_record(
        self,
        task_id: str,
        user_id: str,
        tokens: int = 0,
    ) -> tuple[bool, str]:
        """Check if a call is allowed and record it.

        Returns: (allowed, reason_if_blocked)
        """
        # Get or create task budget
        budget = self._tasks.get(task_id)
        if not budget:
            budget = self.start_task(task_id)

        # If task already blocked, stay blocked
        if budget.blocked:
            return False, budget.block_reason

        # 1. Check per-task call cap
        if budget.calls_made >= self.config.per_task_max_calls:
            budget.blocked = True
            budget.block_reason = f"任务调用次数超限 ({self.config.per_task_max_calls})"
            logger.warning(
                "Task %s blocked: too many calls", task_id
            )
            return False, budget.block_reason

        # 2. Check per-task token cap
        if budget.tokens_used + tokens > self.config.per_task_max_tokens:
            budget.blocked = True
            budget.block_reason = (
                f"任务 token 超限 ({self.config.per_task_max_tokens})"
            )
            logger.warning(
                "Task %s blocked: token budget exceeded", task_id
            )
            return False, budget.block_reason

        # 3. Check loop detection (too many calls in window)
        now = time.time()
        window_start = now - self.config.loop_detect_window_seconds
        history = self._call_history[task_id]
        history.append(now)
        # Keep only calls within the window
        self._call_history[task_id] = [t for t in history if t >= window_start]

        if len(self._call_history[task_id]) > self.config.loop_detect_max_calls:
            budget.blocked = True
            budget.block_reason = "检测到调用循环（短时间内大量调用）"
            logger.error(
                "Task %s blocked: loop detected (%d calls in %ds)",
                task_id,
                len(self._call_history[task_id]),
                self.config.loop_detect_window_seconds,
            )
            return False, budget.block_reason

        # 4. Check per-user daily cap
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        user_data = self._user_daily[user_id]
        if user_data["date"] != today:
            user_data["date"] = today
            user_data["tokens"] = 0

        if user_data["tokens"] + tokens > self.config.per_user_daily_tokens:
            return False, f"用户 {user_id} 今日 token 超限"

        # All checks passed: record usage
        budget.calls_made += 1
        budget.tokens_used += tokens
        user_data["tokens"] += tokens
        return True, ""

    def get_task_status(self, task_id: str) -> dict:
        """Get current task budget status."""
        budget = self._tasks.get(task_id)
        if not budget:
            return {"task_id": task_id, "status": "not_found"}
        return {
            "task_id": task_id,
            "tokens_used": budget.tokens_used,
            "calls_made": budget.calls_made,
            "blocked": budget.blocked,
            "block_reason": budget.block_reason,
            "elapsed_seconds": int(time.time() - budget.started_at),
        }

    def get_user_usage(self, user_id: str) -> dict:
        """Get user's daily usage."""
        return dict(self._user_daily.get(user_id, {"date": "", "tokens": 0}))

    def reset_task(self, task_id: str) -> None:
        """Reset a task (e.g. for retry after fix)."""
        self._tasks.pop(task_id, None)
        self._call_history.pop(task_id, None)


# Global singleton
_controller: CostController | None = None


def get_cost_controller() -> CostController:
    global _controller
    if _controller is None:
        _controller = CostController()
    return _controller
