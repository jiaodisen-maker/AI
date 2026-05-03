"""
Agent Router 服务入口

治理层核心服务，集成：
- AgentRegistry：跨框架 Agent 注册/发现/调用
- Session：用户级会话隔离 + 历史
- Memory：经验引擎
- Middleware Chain：审计/PII/合规/限流/经验注入
- Skill Loader：SKILL.md 文件系统加载

REST API:
  Agent 管理：
    POST /agents               注册
    GET  /agents               列表（带过滤）
    GET  /agents/{name}         详情
    PUT  /agents/{name}         更新
    DELETE /agents/{name}      注销
    POST /agents/discover      语义检索

  调用：
    POST /agents/invoke        统一调用（含中间件链）
    POST /agents/stream        流式调用

  Session：
    GET  /sessions/{id}        获取会话状态
    GET  /sessions/{id}/history 获取消息历史
    DELETE /sessions/{id}      清空会话

  Memory：
    POST /memory/patterns     存储 pattern
    POST /memory/search       检索 pattern

  统计：
    GET /agents/{name}/stats   单 agent 统计
    GET /stats                  全局统计

  健康：
    GET /healthz / /readyz / /livez
"""
from __future__ import annotations

import logging
import os
from contextlib import asynccontextmanager
from dataclasses import asdict
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from .adapters.factory import AdapterFactory
from .adapters.middleware import (
    InvokeContext,
    MiddlewareChain,
    audit_middleware,
    make_compliance_middleware,
    make_experience_middleware,
    make_rate_limit_middleware,
    pii_middleware,
)
from .adapters.ports import (
    AgentRegistryPort,
    MemoryPort,
    SessionPort,
    SkillPort,
)
from .adapters.types import (
    AgentFramework,
    AgentInvokeRequest,
    AgentInvokeResponse,
    AgentMaturity,
    AgentSpec,
    Message,
    Role,
    Skill,
)

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)
logger = logging.getLogger(__name__)


# ============================================================
# 应用状态（依赖注入）
# ============================================================
class AppState:
    registry: AgentRegistryPort | None = None
    session: SessionPort | None = None
    memory: MemoryPort | None = None
    skill_loader: SkillPort | None = None
    middleware_chain: MiddlewareChain | None = None
    ready: bool = False


state = AppState()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """启动时初始化所有 adapter + middleware"""
    factory = AdapterFactory()

    state.registry = factory.create_agent_registry()
    state.session = factory.create_session()
    state.memory = factory.create_memory()
    state.skill_loader = factory.create_skill_loader()

    # 加载本地 SKILL.md
    skills_dir = os.getenv("SKILLS_DIR", "/data/skills")
    try:
        loaded = await state.skill_loader.load_skills(skills_dir)
        logger.info(f"Loaded {loaded} SKILL.md files from {skills_dir}")
    except Exception as e:
        logger.warning(f"Skill load failed: {e}")

    # 中间件链组装
    chain = MiddlewareChain()
    chain.use(audit_middleware)

    # PII（开关）
    if os.getenv("ENABLE_PII", "true").lower() == "true":
        chain.use(pii_middleware)

    # 合规（开关）
    if os.getenv("ENABLE_COMPLIANCE", "true").lower() == "true":
        chain.use(make_compliance_middleware(
            block_input=os.getenv("COMPLIANCE_BLOCK_INPUT", "false").lower() == "true",
            sanitize_output=True,
        ))

    # 限流（如果有 redis）
    if hasattr(state.session, "redis"):
        chain.use(make_rate_limit_middleware(
            redis_client=state.session.redis,
            max_per_minute=int(os.getenv("RATE_LIMIT_PER_MIN", "60")),
            max_per_day=int(os.getenv("RATE_LIMIT_PER_DAY", "1000")),
        ))

    # 经验注入
    if os.getenv("ENABLE_EXPERIENCE", "true").lower() == "true":
        chain.use(make_experience_middleware(state.memory))

    state.middleware_chain = chain
    state.ready = True
    logger.info("Agent Router started, all adapters initialized")
    yield

    state.ready = False
    for adapter in [state.registry, state.session, state.memory]:
        if hasattr(adapter, "close"):
            try:
                await adapter.close()
            except Exception:
                logger.exception("Adapter close failed")


app = FastAPI(
    title="AI Platform - Agent Router",
    version="0.2.0",
    description="20+ Agent 治理层（注册/发现/路由/会话/经验/中间件）",
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# Pydantic schemas
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
    framework: str
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
    agent_name: str | None = None  # 不传则自动 discover
    input: str
    session_id: str
    user_id: str
    metadata: dict = Field(default_factory=dict)


class StorePatternRequest(BaseModel):
    skill_name: str
    input: str
    output: str
    feedback: dict = {}


class SearchPatternRequest(BaseModel):
    skill_name: str
    query: str
    top_k: int = 3


# ============================================================
# 工具函数
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
    """安全序列化 spec（脱敏 auth_config）"""
    d = asdict(spec)
    d["framework"] = spec.framework.value
    d["maturity"] = spec.maturity.value
    d["auth_config"] = {"_redacted": True} if spec.auth_config else {}
    return d


# ============================================================
# 健康探针
# ============================================================
@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.get("/livez")
async def livez():
    return {"status": "alive"}


@app.get("/readyz")
async def readyz():
    if not state.ready:
        raise HTTPException(503, "not ready")
    return {"status": "ready"}


# ============================================================
# Agent 管理
# ============================================================
@app.post("/agents", status_code=201)
async def register_agent(req: RegisterAgentRequest):
    spec = _to_agent_spec(req)
    await state.registry.register(spec)
    return {"name": spec.name, "status": "registered"}


@app.put("/agents/{name}")
async def update_agent(name: str, req: RegisterAgentRequest):
    spec = _to_agent_spec(req)
    await state.registry.update(name, spec)
    return {"name": name, "status": "updated"}


@app.delete("/agents/{name}")
async def deregister_agent(name: str):
    await state.registry.deregister(name)
    return {"name": name, "status": "deregistered"}


@app.get("/agents")
async def list_agents(
    framework: str | None = None,
    owner_team: str | None = None,
    maturity: str | None = None,
):
    agents = await state.registry.list_all(
        framework=AgentFramework(framework) if framework else None,
        owner_team=owner_team,
        maturity=AgentMaturity(maturity) if maturity else None,
    )
    return {"count": len(agents), "agents": [_spec_to_dict(a) for a in agents]}


@app.get("/agents/{name}")
async def get_agent(name: str):
    spec = await state.registry.get(name)
    if not spec:
        raise HTTPException(404, f"Agent '{name}' not found")
    return _spec_to_dict(spec)


@app.post("/agents/discover")
async def discover(req: DiscoverRequest):
    agents = await state.registry.discover(
        query=req.query,
        top_k=req.top_k,
        user_id=req.user_id,
    )
    return {"count": len(agents), "agents": [_spec_to_dict(a) for a in agents]}


# ============================================================
# 调用（含中间件链 + Session 历史）
# ============================================================
@app.post("/agents/invoke")
async def invoke(req: InvokeRequest):
    """统一调用 Agent（屏蔽底层框架，含完整中间件链）"""
    # 1. 自动 discover（如果未指定 agent_name）
    agent_name = req.agent_name
    if not agent_name:
        agents = await state.registry.discover(
            query=req.input, top_k=1, user_id=req.user_id
        )
        if not agents:
            raise HTTPException(404, "No matching agent found")
        agent_name = agents[0].name

    # 2. 拉历史（用户级隔离）
    history = await state.session.get_history(req.session_id, limit=10)

    invoke_req = AgentInvokeRequest(
        agent_name=agent_name,
        input=req.input,
        session_id=req.session_id,
        user_id=req.user_id,
        metadata={**req.metadata, "history_len": len(history)},
    )

    # 3. 通过中间件链调用
    ctx = InvokeContext(request=invoke_req)

    async def base_handler(c: InvokeContext) -> AgentInvokeResponse:
        return await state.registry.invoke(c.request)

    response = await state.middleware_chain.execute(ctx, base_handler)

    # 4. 记录到 Session（用户输入 + AI 响应）
    await state.session.get_or_create(req.session_id, req.user_id)
    await state.session.append_message(
        req.session_id,
        Message(role=Role.USER, content=req.input),
    )
    if response.output and not response.error:
        await state.session.append_message(
            req.session_id,
            Message(role=Role.ASSISTANT, content=response.output),
        )

    result = asdict(response)
    result["middleware_metadata"] = ctx.metadata
    return result


@app.post("/agents/stream")
async def stream(req: InvokeRequest):
    """流式调用（暂不走中间件链）"""
    if not req.agent_name:
        agents = await state.registry.discover(
            query=req.input, top_k=1, user_id=req.user_id
        )
        if not agents:
            raise HTTPException(404, "No matching agent found")
        req.agent_name = agents[0].name

    invoke_req = AgentInvokeRequest(
        agent_name=req.agent_name,
        input=req.input,
        session_id=req.session_id,
        user_id=req.user_id,
        metadata=req.metadata,
    )

    async def event_stream():
        import json
        async for chunk in state.registry.stream_invoke(invoke_req):
            yield f"data: {json.dumps(asdict(chunk))}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


# ============================================================
# Session 管理
# ============================================================
@app.get("/sessions/{session_id}")
async def get_session(session_id: str, user_id: str = ""):
    session = await state.session.get_or_create(session_id, user_id or session_id)
    return {
        "session_id": session.session_id,
        "user_id": session.user_id,
        "message_count": len(session.messages),
        "metadata": session.metadata,
        "created_at": session.created_at,
        "updated_at": session.updated_at,
    }


@app.get("/sessions/{session_id}/history")
async def get_session_history(session_id: str, limit: int = 20):
    messages = await state.session.get_history(session_id, limit=limit)
    return {
        "session_id": session_id,
        "count": len(messages),
        "messages": [
            {
                "role": m.role.value,
                "content": m.content,
                "metadata": m.metadata,
            }
            for m in messages
        ],
    }


@app.delete("/sessions/{session_id}")
async def clear_session(session_id: str):
    await state.session.clear(session_id)
    return {"session_id": session_id, "status": "cleared"}


# ============================================================
# Memory（经验引擎）
# ============================================================
@app.post("/memory/patterns", status_code=201)
async def store_pattern(req: StorePatternRequest):
    pid = await state.memory.store_pattern(
        skill_name=req.skill_name,
        input_text=req.input,
        output_text=req.output,
        feedback=req.feedback,
    )
    return {"pattern_id": pid}


@app.post("/memory/search")
async def search_patterns(req: SearchPatternRequest):
    patterns = await state.memory.retrieve_patterns(
        skill_name=req.skill_name,
        query=req.query,
        top_k=req.top_k,
    )
    return {"count": len(patterns), "patterns": patterns}


# ============================================================
# Skill 管理
# ============================================================
@app.get("/skills")
async def list_skills():
    skills = await state.skill_loader.list_skills()
    return {
        "count": len(skills),
        "skills": [
            {
                "name": s.name,
                "description": s.description,
                "triggers": s.triggers,
                "source_path": s.source_path,
            }
            for s in skills
        ],
    }


@app.get("/skills/{name}")
async def get_skill(name: str):
    skill = await state.skill_loader.get_skill(name)
    if not skill:
        raise HTTPException(404, f"Skill '{name}' not found")
    return {
        "name": skill.name,
        "description": skill.description,
        "instructions": skill.instructions,
        "triggers": skill.triggers,
        "parameters": skill.parameters,
        "source_path": skill.source_path,
    }


# ============================================================
# 统计
# ============================================================
@app.get("/agents/{name}/stats")
async def get_stats(name: str):
    return await state.registry.get_usage_stats(name)


@app.get("/stats")
async def get_all_stats():
    return await state.registry.get_usage_stats()


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
