"""
Agent Router 服务入口

这是治理层的核心服务，对外暴露 REST API：
- POST /agents              注册新 Agent
- GET  /agents              列出 Agent
- GET  /agents/{name}        获取 Agent
- DELETE /agents/{name}      注销 Agent
- POST /agents/discover      语义检索 Agent
- POST /agents/invoke        统一调用（核心）
- POST /agents/stream        流式调用
- GET  /agents/{name}/stats  使用统计
- GET  /healthz              健康检查
"""
from __future__ import annotations

import logging
import os
from contextlib import asynccontextmanager
from dataclasses import asdict

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from .adapters.factory import AdapterFactory
from .adapters.ports import AgentRegistryPort
from .adapters.types import (
    AgentFramework,
    AgentInvokeRequest,
    AgentMaturity,
    AgentSpec,
    Skill,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================
# 应用状态（依赖注入）
# ============================================================
class AppState:
    registry: AgentRegistryPort | None = None


state = AppState()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """启动时初始化 Registry"""
    factory = AdapterFactory()
    state.registry = factory.create_agent_registry()
    logger.info("Agent Router started, registry initialized")
    yield
    # 关闭
    if hasattr(state.registry, "close"):
        await state.registry.close()


app = FastAPI(
    title="AI Platform - Agent Router",
    version="0.1.0",
    description="20+ Agent 治理层（注册/发现/路由）",
    lifespan=lifespan,
)


# ============================================================
# Pydantic schemas (HTTP 接口的入参类型)
# ============================================================
class SkillModel(BaseModel):
    name: str
    description: str
    instructions: str = ""
    triggers: list[str] = []
    parameters: dict = {}


class RegisterAgentRequest(BaseModel):
    name: str
    display_name: str
    description: str
    framework: str  # "coze" / "dify" / "langgraph" / ...
    endpoint: str
    skill: SkillModel
    owner_team: str = ""
    maturity: str = "poc"
    cost_per_call: float = 0.0
    allowed_users: list[str] = []
    allowed_teams: list[str] = []
    auth_type: str = "api_key"
    auth_config: dict = {}
    timeout_seconds: int = 60
    metadata: dict = {}


class DiscoverRequest(BaseModel):
    query: str
    top_k: int = 5
    user_id: str | None = None


class InvokeRequest(BaseModel):
    agent_name: str
    input: str
    session_id: str
    user_id: str
    metadata: dict = {}


# ============================================================
# 工具函数：转换 Pydantic → dataclass
# ============================================================
def _to_agent_spec(req: RegisterAgentRequest) -> AgentSpec:
    return AgentSpec(
        name=req.name,
        display_name=req.display_name,
        description=req.description,
        framework=AgentFramework(req.framework),
        endpoint=req.endpoint,
        skill=Skill(
            name=req.skill.name,
            description=req.skill.description,
            instructions=req.skill.instructions,
            triggers=req.skill.triggers,
            parameters=req.skill.parameters,
        ),
        owner_team=req.owner_team,
        maturity=AgentMaturity(req.maturity),
        cost_per_call=req.cost_per_call,
        allowed_users=req.allowed_users,
        allowed_teams=req.allowed_teams,
        auth_type=req.auth_type,
        auth_config=req.auth_config,
        timeout_seconds=req.timeout_seconds,
        metadata=req.metadata,
    )


def _spec_to_dict(spec: AgentSpec) -> dict:
    """安全序列化 spec（不暴露 auth_config 等敏感字段）"""
    d = asdict(spec)
    d["framework"] = spec.framework.value
    d["maturity"] = spec.maturity.value
    # 脱敏
    d["auth_config"] = {"_redacted": True} if spec.auth_config else {}
    return d


# ============================================================
# 路由
# ============================================================
@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


# === 注册管理 ===
@app.post("/agents", status_code=201)
async def register_agent(req: RegisterAgentRequest):
    """注册新 Agent"""
    spec = _to_agent_spec(req)
    await state.registry.register(spec)
    return {"name": spec.name, "status": "registered"}


@app.put("/agents/{name}")
async def update_agent(name: str, req: RegisterAgentRequest):
    """更新 Agent"""
    spec = _to_agent_spec(req)
    await state.registry.update(name, spec)
    return {"name": name, "status": "updated"}


@app.delete("/agents/{name}")
async def deregister_agent(name: str):
    """注销 Agent"""
    await state.registry.deregister(name)
    return {"name": name, "status": "deregistered"}


# === 查询发现 ===
@app.get("/agents")
async def list_agents(
    framework: str | None = None,
    owner_team: str | None = None,
    maturity: str | None = None,
):
    """列出 Agent（带过滤）"""
    agents = await state.registry.list_all(
        framework=AgentFramework(framework) if framework else None,
        owner_team=owner_team,
        maturity=AgentMaturity(maturity) if maturity else None,
    )
    return {"count": len(agents), "agents": [_spec_to_dict(a) for a in agents]}


@app.get("/agents/{name}")
async def get_agent(name: str):
    """获取 Agent 详情"""
    spec = await state.registry.get(name)
    if not spec:
        raise HTTPException(404, f"Agent '{name}' not found")
    return _spec_to_dict(spec)


@app.post("/agents/discover")
async def discover(req: DiscoverRequest):
    """语义检索 Agent"""
    agents = await state.registry.discover(
        query=req.query,
        top_k=req.top_k,
        user_id=req.user_id,
    )
    return {"count": len(agents), "agents": [_spec_to_dict(a) for a in agents]}


# === 统一调用 ===
@app.post("/agents/invoke")
async def invoke(req: InvokeRequest):
    """统一调用 Agent（屏蔽底层框架）"""
    invoke_req = AgentInvokeRequest(
        agent_name=req.agent_name,
        input=req.input,
        session_id=req.session_id,
        user_id=req.user_id,
        metadata=req.metadata,
    )
    response = await state.registry.invoke(invoke_req)
    return asdict(response)


@app.post("/agents/stream")
async def stream(req: InvokeRequest):
    """流式调用"""
    invoke_req = AgentInvokeRequest(
        agent_name=req.agent_name,
        input=req.input,
        session_id=req.session_id,
        user_id=req.user_id,
        metadata=req.metadata,
    )

    async def event_stream():
        async for chunk in state.registry.stream_invoke(invoke_req):
            import json
            yield f"data: {json.dumps(asdict(chunk))}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


# === 统计 ===
@app.get("/agents/{name}/stats")
async def get_stats(name: str):
    """获取使用统计"""
    return await state.registry.get_usage_stats(name)


@app.get("/stats")
async def get_all_stats():
    """全局统计"""
    return await state.registry.get_usage_stats()


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
