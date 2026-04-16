"""Patrol notifier: sends alerts through configured channels."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.channels.feishu import FeishuBot
    from app.patrol.models import PatrolResult

logger = logging.getLogger(__name__)


class PatrolNotifier:
    """Formats patrol results and pushes notifications to channels.

    Notification routing based on alert level:
    - P0: Feishu urgent message + phone (future)
    - P1: Feishu message
    - P2: Feishu interactive card
    - P3: Log only, no notification
    """

    def __init__(self, feishu_bot: FeishuBot | None = None) -> None:
        self.feishu_bot = feishu_bot

    async def notify(self, result: PatrolResult) -> None:
        """Send notification for a patrol result."""
        if not result.needs_notification:
            logger.debug("Patrol %s: P3 silent, skipping notification", result.task_id)
            return

        message = self._format_message(result)

        if self.feishu_bot:
            try:
                await self.feishu_bot.send_text_message(message)
                logger.info(
                    "Patrol notification sent: %s [%s]",
                    result.task_name, result.alert_level,
                )
            except Exception as e:
                logger.error("Failed to send patrol notification: %s", e)
        else:
            logger.warning("No notification channel available, logging only: %s", message)

    def _format_message(self, result: PatrolResult) -> str:
        """Format a patrol result into a readable message."""
        level_emoji = {
            "P0": "[P0 紧急]",
            "P1": "[P1 告警]",
            "P2": "[P2 通知]",
            "P3": "[P3 记录]",
        }

        lines = [
            f"{level_emoji.get(result.alert_level, '')} {result.title}",
            "",
            result.summary,
        ]

        if result.suggested_actions:
            lines.append("")
            lines.append("建议动作：")
            for i, action in enumerate(result.suggested_actions, 1):
                lines.append(f"  {i}. {action}")

        if result.related_skill_ids:
            lines.append("")
            lines.append(f"相关技能：{', '.join(result.related_skill_ids)}")

        return "\n".join(lines)
