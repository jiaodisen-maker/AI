"""FastAPI application entry point.

Wires together all layers:
  Channel → AgentScope Brain → Skill (as tools) → LLM
  with Experience Engine recording every interaction.
"""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.brain.agent import BrainAgent
from app.brain.tools import register_skills_as_tools
from app.channels.feishu import FeishuBot
from app.channels.message import MessageRouter
from app.config import settings
from app.data.database import DatabaseManager
from app.data.redis import RedisManager
from app.experience.engine import ExperienceEngine
from app.experience.store import ExperienceStore
from app.llm.router import ModelRouter
from app.patrol.notifier import PatrolNotifier
from app.patrol.scheduler import PatrolScheduler
from app.skills.builtin import CompliantCopySkill
from app.skills.registry import SkillRegistry

logger = logging.getLogger(__name__)

# ============================================================
# Application State: holds all initialized components
# ============================================================


@dataclass
class AppState:
    """Global application state holding all initialized components."""

    # Core
    model_router: ModelRouter = field(default_factory=ModelRouter)
    skill_registry: SkillRegistry = field(default_factory=SkillRegistry)

    # Brain (AgentScope)
    brain: BrainAgent = field(default_factory=BrainAgent)

    # Experience
    experience_store: ExperienceStore = field(default_factory=ExperienceStore)
    experience_engine: ExperienceEngine | None = None

    # Channels
    feishu_bot: FeishuBot = field(default_factory=FeishuBot)
    message_router: MessageRouter | None = None

    # Patrol
    patrol_notifier: PatrolNotifier | None = None
    patrol_scheduler: PatrolScheduler | None = None

    # Data
    db: DatabaseManager | None = None
    redis: RedisManager | None = None


_app_state: AppState | None = None


def get_app_state() -> AppState:
    """Get the global application state. Raises if not initialized."""
    if _app_state is None:
        raise RuntimeError("Application state not initialized")
    return _app_state


# ============================================================
# Lifespan: startup and shutdown
# ============================================================


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan: initialize all components on startup, cleanup on shutdown."""
    global _app_state
    state = AppState()

    logger.info("Starting AI 中台 v%s [env=%s]", __version__, settings.app_env)

    # --- Data layer ---
    state.db = DatabaseManager()
    state.redis = RedisManager()
    await state.redis.connect()

    if settings.debug:
        await state.db.init_db()

    # --- Experience store ---
    if state.redis.is_connected:
        await state.experience_store.init_redis(settings.redis_url)

    # --- LLM router ---
    state.model_router = ModelRouter()

    # --- Experience engine ---
    state.experience_engine = ExperienceEngine(
        store=state.experience_store,
        model_router=state.model_router,
    )

    # --- Skills ---
    state.skill_registry = SkillRegistry()
    _register_builtin_skills(state)

    # --- Brain (AgentScope) ---
    state.brain = BrainAgent()
    register_skills_as_tools(
        brain=state.brain,
        registry=state.skill_registry,
        experience_engine=state.experience_engine,
    )
    state.brain.initialize()

    # --- Channels ---
    state.feishu_bot = FeishuBot()
    state.message_router = MessageRouter(
        brain=state.brain,
        experience_engine=state.experience_engine,
    )

    # --- Patrol ---
    state.patrol_notifier = PatrolNotifier(feishu_bot=state.feishu_bot)
    state.patrol_scheduler = PatrolScheduler(notifier=state.patrol_notifier)
    state.patrol_scheduler.start()

    _app_state = state

    logger.info(
        "AI 中台 ready: %d skills registered (AgentScope), patrol %s",
        state.skill_registry.count,
        "enabled" if settings.patrol_enabled else "disabled",
    )

    yield

    # --- Shutdown ---
    logger.info("Shutting down AI 中台...")
    state.patrol_scheduler.stop()
    await state.feishu_bot.close()
    if state.db:
        await state.db.close()
    if state.redis:
        await state.redis.close()

    _app_state = None
    logger.info("AI 中台 shutdown complete")


def _register_builtin_skills(state: AppState) -> None:
    """Register all built-in skills."""
    state.skill_registry.register(CompliantCopySkill(state.model_router))


# ============================================================
# FastAPI App Factory
# ============================================================


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="AI 中台",
        description="自进化企业 AI 操作系统 — AgentScope + Skills + Experience Engine",
        version=__version__,
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"] if settings.debug else [],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from app.api import chat, experience, feishu, health, patrol, skills

    app.include_router(health.router, prefix="/api")
    app.include_router(chat.router, prefix="/api")
    app.include_router(skills.router, prefix="/api")
    app.include_router(experience.router, prefix="/api")
    app.include_router(feishu.router, prefix="/api")
    app.include_router(patrol.router, prefix="/api")

    return app


# Default app instance for `uvicorn app.main:app`
app = create_app()
