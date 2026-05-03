"""
框架无关的数据传输类型。
绝对不允许 import agentscope/langgraph/claude 等任何框架。

业务层只看这里定义的类型。
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Literal


# ============================================================
# 消息和角色
# ============================================================
class Role(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    TOOL = "tool"


@dataclass
class Message:
    """通用消息（不绑定任何框架）"""
    role: Role
    content: str
    tool_calls: list[ToolCall] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)


# ============================================================
# 工具调用
# ============================================================
@dataclass
class ToolSchema:
    """工具的 JSON Schema 描述"""
    name: str
    description: str
    parameters: dict  # JSON Schema


@dataclass
class ToolCall:
    """LLM 发起的工具调用请求"""
    id: str
    name: str
    arguments: dict


@dataclass
class ToolResult:
    """工具执行结果"""
    call_id: str
    content: str
    finished: bool = True
    error: str | None = None


@dataclass
class ToolChunk:
    """流式工具结果片段（对齐 AgentScope 2.0 ToolChunk）"""
    call_id: str
    delta: str
    is_last: bool


# ============================================================
# LLM 生成请求/响应
# ============================================================
@dataclass
class GenerateRequest:
    messages: list[Message]
    tools: list[ToolSchema] = field(default_factory=list)
    model: str | None = None
    temperature: float = 0.7
    max_tokens: int | None = None
    extra: dict = field(default_factory=dict)


@dataclass
class GenerateResponse:
    content: str
    tool_calls: list[ToolCall] = field(default_factory=list)
    is_complete: bool = True
    usage: dict = field(default_factory=dict)


@dataclass
class StreamChunk:
    """流式响应片段（对齐 2.0 ChatResponse.is_last 范式）"""
    delta: str = ""
    tool_call_delta: ToolCall | None = None
    is_last: bool = False
    usage: dict = field(default_factory=dict)


# ============================================================
# 会话状态（用户级隔离）
# ============================================================
@dataclass
class SessionState:
    """用户会话状态"""
    session_id: str
    user_id: str
    messages: list[Message] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)


# ============================================================
# Skill（对齐 Anthropic SKILL.md 标准）
# ============================================================
@dataclass
class Skill:
    """框架无关的 Skill 描述"""
    name: str
    description: str
    instructions: str = ""  # markdown 内容
    triggers: list[str] = field(default_factory=list)
    parameters: dict = field(default_factory=dict)
    source_path: str | None = None
    updated_at: float = field(default_factory=time.time)


# ============================================================
# 中间件上下文
# ============================================================
@dataclass
class HookContext:
    """中间件传递的上下文"""
    request: GenerateRequest
    session: SessionState
    skill_name: str | None = None
    metadata: dict = field(default_factory=dict)


# ============================================================
# Agent Registry（治理层核心）
# ============================================================
class AgentFramework(str, Enum):
    """支持的 Agent 框架"""
    COZE = "coze"
    DIFY = "dify"
    LANGGRAPH = "langgraph"
    AGENTSCOPE_1X = "agentscope_1x"
    AGENTSCOPE_2X = "agentscope_2x"
    CLAUDE_SDK = "claude_sdk"
    HIAGENT = "hiagent"
    LARK_AILY = "lark_aily"
    CUSTOM_HTTP = "custom_http"
    MOCK = "mock"


class AgentMaturity(str, Enum):
    """Agent 成熟度"""
    POC = "poc"
    BETA = "beta"
    PRODUCTION = "production"
    DEPRECATED = "deprecated"


AuthType = Literal["none", "api_key", "oauth", "bearer"]


@dataclass
class AgentSpec:
    """跨框架 Agent 描述（核心数据类）"""
    name: str
    display_name: str
    description: str
    framework: AgentFramework
    endpoint: str
    skill: Skill

    # 治理元数据
    owner_team: str = ""
    maturity: AgentMaturity = AgentMaturity.POC
    cost_per_call: float = 0.0
    avg_latency_ms: int = 0
    success_rate: float = 0.0

    # 访问控制
    allowed_users: list[str] = field(default_factory=list)
    allowed_teams: list[str] = field(default_factory=list)

    # 调用配置
    auth_type: AuthType = "api_key"
    auth_config: dict = field(default_factory=dict)
    timeout_seconds: int = 60

    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)
    metadata: dict = field(default_factory=dict)


@dataclass
class AgentInvokeRequest:
    """统一调用请求"""
    agent_name: str
    input: str
    session_id: str
    user_id: str
    metadata: dict = field(default_factory=dict)


@dataclass
class AgentInvokeResponse:
    """统一调用响应"""
    agent_name: str
    output: str
    cost: float = 0.0
    latency_ms: int = 0
    error: str | None = None
    metadata: dict = field(default_factory=dict)
