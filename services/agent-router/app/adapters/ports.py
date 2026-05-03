"""
6 个稳定接口（Protocol）。一旦定型，未来 5 年不要改。
任何新框架要接入，都实现这些接口。

业务层只 import 这里和 types.py，永不 import 框架。
"""
from __future__ import annotations

from typing import AsyncIterator, Callable, Protocol, runtime_checkable

from .types import (
    AgentFramework,
    AgentInvokeRequest,
    AgentInvokeResponse,
    AgentMaturity,
    AgentSpec,
    GenerateRequest,
    GenerateResponse,
    Message,
    SessionState,
    Skill,
    StreamChunk,
    ToolCall,
    ToolChunk,
    ToolResult,
    ToolSchema,
)


# ============================================================
# Port 1: LLM 生成（最核心）
# ============================================================
@runtime_checkable
class LLMPort(Protocol):
    """大模型调用抽象"""

    async def generate(self, req: GenerateRequest) -> GenerateResponse:
        """同步生成（一次返回完整结果）"""
        ...

    async def stream(self, req: GenerateRequest) -> AsyncIterator[StreamChunk]:
        """流式生成（对齐 2.0 ChatResponse.is_last 范式）"""
        ...

    def get_supported_models(self) -> list[str]:
        """支持的模型列表"""
        ...


# ============================================================
# Port 2: Skill 注册和路由
# ============================================================
@runtime_checkable
class SkillPort(Protocol):
    """Skill 管理抽象（对齐 Anthropic SKILL.md 标准）"""

    async def load_skills(self, source: str) -> int:
        """从来源加载 Skill（路径/沙箱/远程仓库），返回加载数量"""
        ...

    async def list_skills(self) -> list[Skill]:
        """列出所有可用 Skill"""
        ...

    async def get_skill(self, name: str) -> Skill | None:
        """按名取 Skill"""
        ...

    async def get_skills_prompt(self, skill_names: list[str] | None = None) -> str:
        """生成 Skill 注入到 system prompt 的描述"""
        ...

    async def match_skill(self, msg: str) -> Skill | None:
        """根据消息匹配 Skill（触发词/语义/LLM 路由）"""
        ...


# ============================================================
# Port 3: 会话状态隔离（用户隐私关键）
# ============================================================
@runtime_checkable
class SessionPort(Protocol):
    """会话状态管理 - 解决用户隔离问题"""

    async def get_or_create(self, session_id: str, user_id: str) -> SessionState:
        """获取或创建会话"""
        ...

    async def append_message(self, session_id: str, msg: Message) -> None:
        """追加消息"""
        ...

    async def get_history(self, session_id: str, limit: int = 20) -> list[Message]:
        """获取历史"""
        ...

    async def save(self, session: SessionState) -> None:
        """持久化"""
        ...

    async def clear(self, session_id: str) -> None:
        """清空（用户主动清除时）"""
        ...


# ============================================================
# Port 4: 工具执行（支持流式）
# ============================================================
@runtime_checkable
class ToolPort(Protocol):
    """工具执行抽象"""

    def register(self, schema: ToolSchema, executor: Callable) -> None:
        """注册工具"""
        ...

    async def call(self, call: ToolCall, session: SessionState) -> ToolResult:
        """同步执行工具"""
        ...

    async def stream_call(
        self, call: ToolCall, session: SessionState
    ) -> AsyncIterator[ToolChunk]:
        """流式执行（对齐 2.0 ToolChunk）"""
        ...

    def list_schemas(self) -> list[ToolSchema]:
        """列出所有工具 schema"""
        ...


# ============================================================
# Port 5: 经验/知识检索（业务护城河）
# ============================================================
@runtime_checkable
class MemoryPort(Protocol):
    """经验引擎和长期记忆抽象"""

    async def store_pattern(
        self,
        skill_name: str,
        input_text: str,
        output_text: str,
        feedback: dict | None = None,
    ) -> str:
        """记录一次执行（id 返回）"""
        ...

    async def retrieve_patterns(
        self, skill_name: str, query: str, top_k: int = 3
    ) -> list[dict]:
        """检索相似 pattern"""
        ...

    async def store_knowledge(self, namespace: str, content: str, metadata: dict) -> str:
        """存储行业本体/知识"""
        ...

    async def retrieve_knowledge(
        self, namespace: str, query: str, top_k: int = 5
    ) -> list[dict]:
        """检索知识"""
        ...


# ============================================================
# Port 6: Agent Registry（治理层核心，新增）
# ============================================================
@runtime_checkable
class AgentRegistryPort(Protocol):
    """跨框架 Agent 注册、发现、调用"""

    # === 注册管理 ===
    async def register(self, spec: AgentSpec) -> None:
        """注册一个 Agent"""
        ...

    async def update(self, name: str, spec: AgentSpec) -> None:
        """更新 Agent 元数据"""
        ...

    async def deregister(self, name: str) -> None:
        """注销"""
        ...

    # === 发现 ===
    async def list_all(
        self,
        framework: AgentFramework | None = None,
        owner_team: str | None = None,
        maturity: AgentMaturity | None = None,
    ) -> list[AgentSpec]:
        """列出 Agent（带过滤）"""
        ...

    async def get(self, name: str) -> AgentSpec | None:
        """精确查询"""
        ...

    async def discover(
        self,
        query: str,
        top_k: int = 5,
        user_id: str | None = None,
    ) -> list[AgentSpec]:
        """语义检索 Agent"""
        ...

    # === 统一调用（核心）===
    async def invoke(self, req: AgentInvokeRequest) -> AgentInvokeResponse:
        """统一调用接口（屏蔽底层框架差异）"""
        ...

    async def stream_invoke(
        self, req: AgentInvokeRequest
    ) -> AsyncIterator[StreamChunk]:
        """流式调用"""
        ...

    # === 治理 ===
    async def check_permission(self, agent_name: str, user_id: str) -> bool:
        """权限检查"""
        ...

    async def get_usage_stats(
        self,
        agent_name: str | None = None,
    ) -> dict:
        """使用统计"""
        ...
