"""队列消费者。把 event 翻译成 memory_write 调用。

启动多份并发消费：
  python worker.py --consumer w1 &
  python worker.py --consumer w2 &
  ...
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import socket
import sys
import time

import yaml
import httpx

from .queue import consume, ack, to_dlq
from .translator import translate

CFG = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), "config.yaml")))
MAX_RETRIES = CFG["queue"]["max_retries"]
BACKOFF = CFG["queue"]["backoff_base_ms"] / 1000
MEMORY_ENDPOINT = CFG["memory"]["mcp_endpoint"]


async def _call_memory_write(content: str, hints: dict) -> dict:
    """调聚合 MCP 的 memory_write。这里走 HTTP；stdio 模式见 mcp_server.py。"""
    if MEMORY_ENDPOINT == "stdio":
        from ...scripts.router import MemoryRouter
        res = await MemoryRouter().write(content, hints)
        return res.__dict__

    async with httpx.AsyncClient(timeout=CFG["memory"]["timeout_ms"] / 1000) as cli:
        r = await cli.post(f"{MEMORY_ENDPOINT}/memory_write",
                           json={"content": content, "hints": hints})
        r.raise_for_status()
        return r.json()


async def _fetch_doc_body(token: str) -> str:
    """飞书 drive 文档拉正文（用 tenant_access_token）。"""
    from .token_refresher import current_token
    headers = {"Authorization": f"Bearer {await current_token()}"}
    async with httpx.AsyncClient() as cli:
        r = await cli.get(
            f"https://open.feishu.cn/open-apis/docx/v1/documents/{token}/raw_content",
            headers=headers, timeout=10)
        r.raise_for_status()
        return r.json().get("data", {}).get("content", "")


async def _fetch_meeting_transcript(meeting_id: str) -> str:
    from .token_refresher import current_token
    headers = {"Authorization": f"Bearer {await current_token()}"}
    async with httpx.AsyncClient() as cli:
        r = await cli.get(
            f"https://open.feishu.cn/open-apis/vc/v1/meetings/{meeting_id}/transcript",
            headers=headers, timeout=30)
        r.raise_for_status()
        return r.json().get("data", {}).get("transcript", "")


async def process_one(event: dict) -> None:
    payload = translate(event)
    if not payload:
        return

    hints = payload["hints"]
    content = payload["content"]

    # 异步外拉补全（飞书 webhook 不带正文的情况）
    if hints.pop("needs_full_fetch", False):
        body = await _fetch_doc_body(hints["feishu_token"])
        content = f"{content}\n\n---\n{body}"
    if hints.pop("needs_transcript_fetch", False):
        meeting_id = event.get("event", {}).get("meeting", {}).get("id")
        if meeting_id:
            transcript = await _fetch_meeting_transcript(meeting_id)
            content = f"{content}\n\n## 转写\n{transcript}"

    await _call_memory_write(content, hints)


async def loop(consumer: str):
    print(f"[worker:{consumer}] started", flush=True)
    async for msg_id, event in consume(consumer):
        for attempt in range(MAX_RETRIES):
            try:
                await process_one(event)
                await ack(msg_id)
                break
            except Exception as e:
                wait = BACKOFF * (2 ** attempt)
                print(f"[worker:{consumer}] msg={msg_id} try={attempt} err={e} "
                      f"wait={wait:.1f}s", file=sys.stderr, flush=True)
                await asyncio.sleep(wait)
        else:
            await to_dlq(event, reason=f"exceeded {MAX_RETRIES} retries")
            await ack(msg_id)
            print(f"[worker:{consumer}] DLQ msg={msg_id}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--consumer",
                    default=f"w-{socket.gethostname()}-{os.getpid()}")
    args = ap.parse_args()
    asyncio.run(loop(args.consumer))


if __name__ == "__main__":
    main()
