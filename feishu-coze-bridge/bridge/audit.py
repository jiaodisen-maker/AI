"""审计日志 —— 4 类落库。

参考 docs/coze-knowledge-base/DATA-SECURITY.md §11.
"""
from __future__ import annotations

import hashlib
import json
import logging
import time
from pathlib import Path

from .config import SERVER


LOG = logging.getLogger("bridge.audit")


def _log_dir() -> Path:
    p = Path(SERVER.audit_log_dir)
    p.mkdir(parents=True, exist_ok=True)
    return p


def _write(stream: str, record: dict) -> None:
    f = _log_dir() / f"{stream}.log"
    f.open("a", encoding="utf-8").write(json.dumps(record, ensure_ascii=False) + "\n")


def log_sync(event_type: str, target: str, ok: bool,
              event_id: str, latency_ms: float, error: str = "") -> None:
    _write("sync", {
        "ts": time.time(),
        "event_type": event_type,
        "target": target,
        "ok": ok,
        "event_id": event_id,
        "latency_ms": round(latency_ms, 1),
        "error": error[:500],
    })


def log_pii_block(event_id: str, event_type: str, reason: str,
                   payload_hash: str) -> None:
    """**永久保留**——合规事件。"""
    _write("pii_block", {
        "ts": time.time(),
        "event_id": event_id,
        "event_type": event_type,
        "reason": reason,
        "payload_hash": payload_hash,
    })
    LOG.warning("PII block: event=%s reason=%s", event_id, reason)


def hash_payload(payload: dict) -> str:
    s = json.dumps(payload, sort_keys=True, default=str).encode()
    return hashlib.sha256(s).hexdigest()[:16]
