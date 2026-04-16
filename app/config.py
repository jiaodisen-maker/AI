"""Application configuration loaded from environment variables."""

from __future__ import annotations

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Central configuration for the AI middleware platform."""

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

    # --- App ---
    app_name: str = "ai-zhongtai"
    app_env: str = "development"
    debug: bool = True
    secret_key: str = "change-me-to-a-random-string"

    # --- LLM: Local model (vLLM) ---
    local_model_base_url: str = "http://localhost:8000/v1"
    local_model_name: str = "qwen2.5-72b-instruct"
    local_model_api_key: str = "not-needed"

    # --- LLM: Overseas models ---
    anthropic_api_key: str = ""
    openai_api_key: str = ""

    # --- LLM: Routing strategy ---
    # local_first | overseas_first | cost_optimized
    model_routing_strategy: str = "local_first"

    # --- Database ---
    database_url: str = "sqlite+aiosqlite:///./ai_zhongtai.db"
    redis_url: str = "redis://localhost:6379/0"

    # --- Vector DB ---
    milvus_host: str = "localhost"
    milvus_port: int = 19530

    # --- ClickHouse ---
    clickhouse_host: str = "localhost"
    clickhouse_port: int = 8123
    clickhouse_database: str = "analytics"

    # --- Feishu ---
    feishu_app_id: str = ""
    feishu_app_secret: str = ""
    feishu_verification_token: str = ""
    feishu_encrypt_key: str = ""

    # --- File storage ---
    oss_endpoint: str = ""
    oss_access_key_id: str = ""
    oss_access_key_secret: str = ""
    oss_bucket: str = "ai-zhongtai"

    # --- Patrol ---
    patrol_enabled: bool = True
    patrol_timezone: str = "Asia/Shanghai"
    use_celery: bool = False  # If true, use Celery instead of APScheduler

    # --- Langfuse Observability ---
    langfuse_public_key: str = ""
    langfuse_secret_key: str = ""
    langfuse_host: str = "https://cloud.langfuse.com"

    # --- Cost Control (Phase 4) ---
    per_task_max_tokens: int = 50000
    per_task_max_calls: int = 20
    per_user_daily_tokens: int = 500000

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"


# Singleton — import this everywhere
settings = Settings()
