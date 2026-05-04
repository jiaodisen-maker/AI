"""冷启动 / 灾难恢复回填。

启动时 + 每天凌晨 3 点跑一次：
  - 拉过去 24h（默认）的消息 / 文档变更 / 日程变更
  - 跟本地 cursor 比对，缺失的塞回 queue
  - 过滤掉已经处理过的（idempotency 会自动去重）

usage:
  python backfill.py --once
  python backfill.py --cron
  python backfill.py --hours 72         # 临时拉更久
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

import httpx
import yaml

from .queue import enqueue
from .token_refresher import current_token

CFG = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), "config.yaml")))
LOOKBACK = CFG["backfill"]["lookback_hours"]
CURSOR_FILE = Path(CFG["backfill"]["cursor_file"])


def _load_cursor() -> datetime:
    if CURSOR_FILE.exists():
        return datetime.fromisoformat(CURSOR_FILE.read_text().strip())
    return datetime.utcnow() - timedelta(hours=LOOKBACK)


def _save_cursor(ts: datetime):
    CURSOR_FILE.write_text(ts.isoformat())


async def _list_messages(since: datetime) -> list[dict]:
    """飞书没有"列出所有消息"的 API，只能按 chat 拉。
    生产实现：维护订阅的 chat_id 列表，逐个拉。这里只示意。"""
    headers = {"Authorization": f"Bearer {await current_token()}"}
    out = []
    async with httpx.AsyncClient(headers=headers, timeout=15) as cli:
        # 拉机器人能见的所有 chat
        r = await cli.get("https://open.feishu.cn/open-apis/im/v1/chats")
        chats = r.json().get("data", {}).get("items", [])
        for chat in chats:
            cid = chat["chat_id"]
            page_token = ""
            while True:
                r = await cli.get(
                    "https://open.feishu.cn/open-apis/im/v1/messages",
                    params={
                        "container_id_type": "chat",
                        "container_id": cid,
                        "start_time": int(since.timestamp()),
                        "page_size": 50,
                        "page_token": page_token,
                    })
                d = r.json().get("data", {})
                for m in d.get("items", []):
                    # 包成事件格式，复用 translator
                    out.append({
                        "header": {"event_type": "im.message.receive_v1",
                                   "event_id": f"backfill:{m['message_id']}"},
                        "event": {"message": m,
                                  "sender": {"sender_id":
                                             {"open_id": m.get("sender", {}).get("id", "")}}},
                    })
                page_token = d.get("page_token")
                if not page_token:
                    break
    return out


async def _list_doc_changes(since: datetime) -> list[dict]:
    headers = {"Authorization": f"Bearer {await current_token()}"}
    out = []
    async with httpx.AsyncClient(headers=headers, timeout=15) as cli:
        r = await cli.get(
            "https://open.feishu.cn/open-apis/drive/v1/files",
            params={"order_by": "EditedTime",
                    "direction": "DESC", "page_size": 50})
        for f in r.json().get("data", {}).get("files", []):
            edited = datetime.fromtimestamp(int(f["modified_time"]))
            if edited < since:
                continue
            out.append({
                "header": {"event_type": "drive.file.edit_v1",
                           "event_id": f"backfill:doc:{f['token']}:{f['modified_time']}"},
                "event": {"file_token": f["token"], "file_name": f["name"],
                          "url": f["url"]},
            })
    return out


async def run_once(hours: int | None = None):
    cursor = _load_cursor() if hours is None else datetime.utcnow() - timedelta(hours=hours)
    now = datetime.utcnow()
    print(f"[backfill] from={cursor.isoformat()} to={now.isoformat()}")

    msgs = await _list_messages(cursor)
    docs = await _list_doc_changes(cursor)

    for ev in msgs + docs:
        await enqueue(ev)   # idempotency 会去重，不怕重复

    _save_cursor(now)
    print(f"[backfill] enqueued msgs={len(msgs)} docs={len(docs)}")


async def loop():
    while True:
        try:
            await run_once()
        except Exception as e:
            print(f"[backfill] err={e}")
        # 24 小时一次（cron 可以更精细）
        await asyncio.sleep(24 * 3600)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--cron", action="store_true")
    ap.add_argument("--hours", type=int, default=None)
    args = ap.parse_args()
    if args.cron:
        asyncio.run(loop())
    else:
        asyncio.run(run_once(args.hours))


if __name__ == "__main__":
    main()
