from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+psycopg://platform:platform@localhost:5432/platform"

    temporal_address: str = "localhost:7233"
    temporal_namespace: str = "default"
    temporal_task_queue: str = "agentic-insight"

    minio_endpoint: str = "localhost:9000"
    minio_root_user: str = "minio"
    minio_root_password: str = "minio12345"
    minio_bucket: str = "cases-media"

    redis_url: str = "redis://localhost:6379/0"

    deepseek_api_key: str = ""
    qwen_api_key: str = ""
    anthropic_api_key: str = ""

    douyin_oauth_client_id: str = ""
    douyin_oauth_client_secret: str = ""
    qianchuan_api_key: str = ""

    poc_crawled_enabled: bool = True
    poc_data_ttl_days: int = 30
    hitl_webhook_url: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()
