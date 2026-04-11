"""Data models for the Skill system."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class SkillCategory(str, Enum):
    """Skill categories mapping to business domains."""

    CONTENT = "content"  # 内容系：文案、创作
    DATA = "data"  # 数据系：查询、报表、分析
    OPERATION = "operation"  # 运营系：活动、客诉、竞品
    PRODUCT = "product"  # 产品系：新品、配方、包装
    PATROL = "patrol"  # 巡逻系：定时扫描、主动告警


class ModelPreference(str, Enum):
    """Which model tier a skill prefers."""

    LOCAL = "local"  # 本地模型（Qwen），低成本
    OVERSEAS = "overseas"  # 海外模型（Claude/GPT），高质量
    SPECIALIZED = "specialized"  # 微调模型（合规专用）
    AUTO = "auto"  # 由路由策略决定


class SkillMeta(BaseModel):
    """Metadata describing a skill's identity and capabilities."""

    id: str  # e.g. "compliant-copy"
    name: str  # e.g. "合规文案生成"
    description: str  # 用于意图路由匹配的描述
    category: SkillCategory
    version: str = "1.0.0"
    author: str = "system"
    triggers: list[str] = Field(default_factory=list)  # 触发词
    parameters: dict[str, Any] = Field(default_factory=dict)  # JSON Schema
    permissions: list[str] = Field(default_factory=list)
    model_preference: ModelPreference = ModelPreference.AUTO


class SkillInput(BaseModel):
    """Standard input for skill execution."""

    user_message: str
    parameters: dict[str, Any] = Field(default_factory=dict)
    user_id: str = ""
    session_id: str = ""
    context: dict[str, Any] = Field(default_factory=dict)


class SkillOutput(BaseModel):
    """Standard output from skill execution."""

    success: bool = True
    content: str = ""
    data: dict[str, Any] = Field(default_factory=dict)
    error: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class SkillExecutionRecord(BaseModel):
    """Record of a single skill execution, used by the Experience Engine."""

    id: str = ""
    skill_id: str
    input: SkillInput
    output: SkillOutput
    human_edited_output: str | None = None
    execution_time_ms: int = 0
    model_used: str = ""
    created_at: datetime = Field(default_factory=datetime.now)
