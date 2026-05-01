"""Structured logging with correlation IDs (workflow_id)。

每条 log 自动带 workflow_id 和 agent name 字段，便于 Grafana Loki / ELK 聚合。
"""
from __future__ import annotations

import contextvars
import json
import logging
import sys
import time

# correlation context (workflow_id, run_id, agent)
_workflow_id: contextvars.ContextVar[str | None] = contextvars.ContextVar("workflow_id", default=None)
_agent: contextvars.ContextVar[str | None] = contextvars.ContextVar("agent", default=None)


def set_correlation(workflow_id: str | None, agent: str | None = None) -> None:
    if workflow_id is not None:
        _workflow_id.set(workflow_id)
    if agent is not None:
        _agent.set(agent)


class StructuredFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(record.created)),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        wf = _workflow_id.get()
        ag = _agent.get()
        if wf:
            payload["workflow_id"] = wf
        if ag:
            payload["agent"] = ag
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False, default=str)


def setup_structured_logging(level: int = logging.INFO) -> None:
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(StructuredFormatter())
    root = logging.getLogger()
    root.handlers = [h]
    root.setLevel(level)
