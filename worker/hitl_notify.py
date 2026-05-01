"""HITL Alert webhook 通知 — 当 hitl_alerts 写入时调钉钉/企业微信机器人 webhook。

设计要点：
- 数据不在 IM 持久化（IM 只通知，载体是 Postgres + Web UI）
- 失败 fail-soft（webhook 挂不影响主流程）
- 每个 alert_type 用不同 emoji 区分

调用方式：
    from worker.hitl_notify import notify_alert
    notify_alert("compliance_edge", payload, alert_id)
"""
from __future__ import annotations

import json
import logging
import os

import httpx

log = logging.getLogger(__name__)

EMOJI = {
    "compliance_edge": "⚖️",
    "low_confidence": "❓",
    "new_microtype": "🆕",
    "poc_purge_failed": "🗑️",
}


def _format_dingtalk(alert_type: str, payload: dict, alert_id: str | None) -> dict:
    emoji = EMOJI.get(alert_type, "🔔")
    title = f"{emoji} HITL Alert · {alert_type}"
    md_lines = [f"# {title}"]
    if alert_id:
        md_lines.append(f"alert_id: `{alert_id}`")
    md_lines.append(
        "```json\n" + json.dumps(payload, ensure_ascii=False, indent=2, default=str)[:1500] + "\n```"
    )
    md_lines.append("[在 UI 处理](http://localhost:3000/alerts)")
    return {
        "msgtype": "markdown",
        "markdown": {"title": title, "text": "\n\n".join(md_lines)},
    }


def notify_alert(alert_type: str, payload: dict, alert_id: str | None = None) -> bool:
    url = os.getenv("HITL_WEBHOOK_URL")
    if not url:
        return False
    try:
        msg = _format_dingtalk(alert_type, payload, alert_id)
        with httpx.Client(timeout=5.0) as c:
            r = c.post(url, json=msg)
            r.raise_for_status()
        return True
    except Exception as e:
        log.warning("HITL webhook failed (non-fatal): %s", e)
        return False
