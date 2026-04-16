"""Base class for patrol tasks."""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.patrol.models import PatrolResult, PatrolTaskConfig


class BasePatrolTask(ABC):
    """Abstract base for patrol (proactive monitoring) tasks.

    Patrol tasks run on a schedule, scan data, detect anomalies,
    and return results that may trigger notifications.
    """

    @abstractmethod
    def config(self) -> PatrolTaskConfig:
        """Return the patrol task configuration including schedule."""

    @abstractmethod
    async def execute(self) -> PatrolResult:
        """Run the patrol check and return results.

        Should:
        1. Fetch relevant data
        2. Analyze for anomalies / opportunities
        3. Return PatrolResult with appropriate alert level
        """
