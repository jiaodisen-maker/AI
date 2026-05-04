"""告警分发：根据 severity 路由到飞书 / 邮件 / 电话。

INFO/WARN/CRITICAL/FATAL — 通道按 config.yaml 配置。
带 cooldown 去重，避免风暴。
"""
from __future__ import annotations

import os
from datetime import timedelta
from typing import Literal

import httpx
import yaml

from .state import State

CFG = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), "config.yaml")))
ALERTS = CFG["alerts"]
HC = CFG["healthcheck"]
COOLDOWN = timedelta(minutes=HC["escalation"]["cooldown_minutes"])

Severity = Literal["INFO", "WARN", "CRITICAL", "FATAL"]
_state = State(CFG["storage"]["state_db"])


async def emit(severity: Severity, title: str, body: str,
               dedup_key: str | None = None) -> None:
    if dedup_key and not _state.should_emit(f"{severity}:{dedup_key}", COOLDOWN):
        return

    channels = ALERTS["channels_by_severity"].get(severity, [])
    for ch in channels:
        try:
            if ch == "feishu_chat":
                await _feishu_chat(severity, title, body)
            elif ch == "feishu_at":
                await _feishu_chat(severity, title, body, at_oncall=True)
            elif ch == "feishu_phone":
                await _feishu_phone(title, body)
            elif ch == "email":
                await _email(severity, title, body)
            elif ch == "sms":
                pass   # 接你公司的短信网关
        except Exception as e:
            print(f"[alerts] {ch} failed: {e}")


async def _feishu_chat(severity: str, title: str, body: str,
                       at_oncall: bool = False) -> None:
    webhook = os.path.expandvars(ALERTS.get("feishu_bot_webhook", ""))
    if not webhook:
        return
    text = f"[{severity}] {title}\n{body}"
    if at_oncall:
        oncall = ALERTS["oncall_users"]["primary"]
        text = f"<at user_id=\"{oncall}\"></at> " + text
    async with httpx.AsyncClient(timeout=5) as cli:
        await cli.post(webhook, json={
            "msg_type": "text",
            "content": {"text": text},
        })


async def _feishu_phone(title: str, body: str) -> None:
    hook = os.path.expandvars(ALERTS.get("oncall_phone_webhook", ""))
    if not hook:
        return
    async with httpx.AsyncClient(timeout=5) as cli:
        await cli.post(hook, json={"title": title, "body": body})


async def _email(severity: str, title: str, body: str) -> None:
    # 接你公司的邮件网关；这里留 stub
    print(f"[alerts:email] {severity} {title}")
