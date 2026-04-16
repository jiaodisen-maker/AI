"""Data models for the Patrol system."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class AlertLevel(str, Enum):
    """Alert severity levels.

    P0 - 立即通知（飞书 + 电话）：超过阈值 50%
    P1 - 紧急通知（飞书消息）：超过阈值 20%
    P2 - 日常通知（飞书卡片）：日常巡逻报告
    P3 - 静默记录（仅日志）：微小波动
    """

    P0_CRITICAL = "P0"
    P1_URGENT = "P1"
    P2_NORMAL = "P2"
    P3_SILENT = "P3"


class PatrolResult(BaseModel):
    """Result of a single patrol task execution."""

    task_id: str
    task_name: str
    alert_level: AlertLevel = AlertLevel.P3_SILENT
    title: str = ""
    summary: str = ""
    details: dict[str, Any] = Field(default_factory=dict)
    suggested_actions: list[str] = Field(default_factory=list)
    related_skill_ids: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)

    @property
    def needs_notification(self) -> bool:
        notify_levels = (
            AlertLevel.P0_CRITICAL, AlertLevel.P1_URGENT, AlertLevel.P2_NORMAL,
        )
        return self.alert_level in notify_levels


class PatrolTaskConfig(BaseModel):
    """Configuration for a scheduled patrol task."""

    task_id: str
    name: str
    description: str = ""
    cron: str  # cron expression, e.g. "0 8 * * *" for daily 8am
    enabled: bool = True
    notify_channels: list[str] = Field(default_factory=lambda: ["feishu"])
    parameters: dict[str, Any] = Field(default_factory=dict)
