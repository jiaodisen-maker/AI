"""集中加载环境变量 + 默认值。所有模块只从这里取配置。"""
from __future__ import annotations

import os
from dataclasses import dataclass


def _env(name: str, default: str | None = None, *, required: bool = False) -> str:
    v = os.environ.get(name, default)
    if required and not v:
        raise RuntimeError(f"missing required env: {name}")
    return v or ""


@dataclass(frozen=True)
class FeishuCfg:
    app_id: str
    app_secret: str
    verification_token: str
    encrypt_key: str
    delivery_mode: str   # webhook | long_connection


@dataclass(frozen=True)
class CozeCfg:
    api_base: str
    pat: str
    enterprise_id: str
    # 资源 ID
    bot_personal_assistant: str
    bot_meeting_digest: str
    bot_approval_handler: str
    kb_product: str
    kb_sop: str
    kb_meeting_transcripts: str
    workflow_meeting_digest: str


@dataclass(frozen=True)
class QueueCfg:
    redis_url: str
    stream: str
    dlq: str
    group: str
    idempotency_ttl_s: int
    max_retries: int
    backoff_base_ms: int


@dataclass(frozen=True)
class ServerCfg:
    bind_host: str
    bind_port: int
    prometheus_port: int
    feishu_alert_webhook: str
    audit_log_dir: str
    database_url: str


def load() -> tuple[FeishuCfg, CozeCfg, QueueCfg, ServerCfg]:
    feishu = FeishuCfg(
        app_id=_env("FEISHU_APP_ID", required=True),
        app_secret=_env("FEISHU_APP_SECRET", required=True),
        verification_token=_env("FEISHU_VERIFICATION_TOKEN", required=True),
        encrypt_key=_env("FEISHU_ENCRYPT_KEY", required=True),
        delivery_mode=_env("FEISHU_DELIVERY_MODE", "webhook"),
    )
    coze = CozeCfg(
        api_base=_env("COZE_API_BASE", "https://api.coze.cn"),
        pat=_env("COZE_PAT", required=True),
        enterprise_id=_env("COZE_ENTERPRISE_ID", required=True),
        bot_personal_assistant=_env("COZE_PERSONAL_ASSISTANT_BOT_ID"),
        bot_meeting_digest=_env("COZE_MEETING_DIGEST_BOT_ID"),
        bot_approval_handler=_env("COZE_APPROVAL_HANDLER_BOT_ID"),
        kb_product=_env("COZE_PRODUCT_KB_DATASET_ID"),
        kb_sop=_env("COZE_SOP_KB_DATASET_ID"),
        kb_meeting_transcripts=_env("COZE_MEETING_TRANSCRIPTS_KB_DATASET_ID"),
        workflow_meeting_digest=_env("COZE_MEETING_DIGEST_WORKFLOW_ID"),
    )
    queue = QueueCfg(
        redis_url=_env("REDIS_URL", "redis://redis:6379/0"),
        stream=_env("QUEUE_STREAM", "feishu:events"),
        dlq=_env("QUEUE_DLQ", "feishu:events:dlq"),
        group=_env("QUEUE_GROUP", "bridge-workers"),
        idempotency_ttl_s=int(_env("IDEMPOTENCY_TTL_SECONDS", "3600")),
        max_retries=int(_env("MAX_RETRIES", "5")),
        backoff_base_ms=int(_env("BACKOFF_BASE_MS", "1000")),
    )
    server = ServerCfg(
        bind_host=_env("BIND_HOST", "0.0.0.0"),
        bind_port=int(_env("BIND_PORT", "8810")),
        prometheus_port=int(_env("PROMETHEUS_PORT", "9100")),
        feishu_alert_webhook=_env("FEISHU_ALERT_WEBHOOK"),
        audit_log_dir=_env("AUDIT_LOG_DIR", "/var/log/feishu-coze-bridge"),
        database_url=_env("DATABASE_URL", ""),
    )
    return feishu, coze, queue, server


# 模块级单例（worker / server 启动时 load 一次）
FEISHU, COZE, QUEUE, SERVER = load()
