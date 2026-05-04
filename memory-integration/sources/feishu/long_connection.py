"""飞书长连接（WebSocket）入口。

适用场景：
  - 没公网域名 / 不想暴露 HTTPS
  - 内网部署 / 本地开发

跟 server.py 互斥，二选一即可。共用 worker / queue / translator。
"""
from __future__ import annotations

import asyncio
import os
import yaml

import lark_oapi as lark    # pip install lark-oapi
from lark_oapi.adapter.ws.client import Client

from .idempotency import seen_before
from .queue import enqueue

CFG = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), "config.yaml")))
APP_ID = os.path.expandvars(CFG["feishu"]["app_id"])
APP_SECRET = os.path.expandvars(CFG["feishu"]["app_secret"])


async def _on_event(event: dict) -> None:
    event_id = event.get("header", {}).get("event_id")
    if not event_id or await seen_before(event_id):
        return
    await enqueue(event)


def main():
    # lark-oapi 的长连接客户端会自动重连、自动续 token
    handler = (lark.EventDispatcherHandler.builder("", "")
               .register_p2_im_message_receive_v1(
                   lambda data: asyncio.run(_on_event(data.dict())))
               .register_p2_drive_file_edit_v1(
                   lambda data: asyncio.run(_on_event(data.dict())))
               .register_p2_calendar_calendar_event_changed_v4(
                   lambda data: asyncio.run(_on_event(data.dict())))
               .register_p2_approval_instance_approved_v4(
                   lambda data: asyncio.run(_on_event(data.dict())))
               .register_p2_vc_meeting_recording_ready_v1(
                   lambda data: asyncio.run(_on_event(data.dict())))
               .register_p2_contact_user_updated_v3(
                   lambda data: asyncio.run(_on_event(data.dict())))
               .build())

    cli = Client.builder() \
        .app_id(APP_ID) \
        .app_secret(APP_SECRET) \
        .event_handler(handler) \
        .build()

    cli.start()  # 阻塞，自动重连


if __name__ == "__main__":
    main()
