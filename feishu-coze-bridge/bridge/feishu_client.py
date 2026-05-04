"""飞书 OpenAPI 客户端：拉取 webhook 事件中没带的细节（如文档正文、转写、通讯录详情）。

token 自动从 Redis 拉（token_refresher.py 在续）。
"""
from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

import httpx
import redis.asyncio as redis

from .config import FEISHU, QUEUE


LOG = logging.getLogger("bridge.feishu_client")
BASE = "https://open.feishu.cn/open-apis"
_TOKEN_KEY = "feishu:tenant_access_token"
_r = redis.from_url(QUEUE.redis_url, db=2)


async def _token() -> str:
    """从 Redis 拿当前 token；没有时兜底现拉。"""
    val = await _r.get(_TOKEN_KEY)
    if val:
        return val.decode()
    # 兜底拉一次（理论上 token_refresher 会一直在续，不应走这）
    async with httpx.AsyncClient(timeout=10) as cli:
        r = await cli.post(
            f"{BASE}/auth/v3/tenant_access_token/internal",
            json={"app_id": FEISHU.app_id, "app_secret": FEISHU.app_secret},
        )
        r.raise_for_status()
        d = r.json()
        tok = d["tenant_access_token"]
        await _r.set(_TOKEN_KEY, tok, ex=max(d["expire"] - 600, 60))
        return tok


async def _get(path: str, params: dict | None = None) -> dict:
    headers = {"Authorization": f"Bearer {await _token()}"}
    async with httpx.AsyncClient(timeout=15) as cli:
        r = await cli.get(f"{BASE}{path}", params=params, headers=headers)
        r.raise_for_status()
        return r.json()


# ---- 文档 -----------------------------------------------------------

async def get_docx_raw_content(file_token: str) -> str:
    """拉飞书云文档纯文本正文。"""
    d = await _get(f"/docx/v1/documents/{file_token}/raw_content")
    return d.get("data", {}).get("content", "")


# ---- 会议转写 -------------------------------------------------------

async def get_vc_transcript(meeting_id: str) -> str:
    """拉飞书会议转写（需开启转写权限）。"""
    d = await _get(f"/vc/v1/meetings/{meeting_id}/transcript")
    return d.get("data", {}).get("transcript", "")


async def list_vc_attendees(meeting_id: str) -> list[dict]:
    d = await _get(f"/vc/v1/meetings/{meeting_id}/attendees")
    return d.get("data", {}).get("attendees", [])


# ---- 通讯录 ---------------------------------------------------------

async def list_users(page_size: int = 100,
                      page_token: str = "") -> tuple[list[dict], str]:
    """分页拉所有用户。"""
    d = await _get("/contact/v3/users", {
        "page_size": page_size,
        "page_token": page_token,
    })
    data = d.get("data", {})
    return data.get("items", []), data.get("page_token", "")


async def get_user(open_id: str) -> dict | None:
    try:
        d = await _get(f"/contact/v3/users/{open_id}")
        return d.get("data", {}).get("user")
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return None
        raise


# ---- 多维表格 -------------------------------------------------------

async def bitable_get_record(app_token: str, table_id: str,
                              record_id: str) -> dict:
    d = await _get(
        f"/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}")
    return d.get("data", {}).get("record", {})


# ---- 邮箱 -----------------------------------------------------------

async def get_mail_message(mailbox: str, message_id: str) -> dict:
    d = await _get(
        f"/mail/v1/user_mailboxes/{mailbox}/messages/{message_id}")
    return d.get("data", {}).get("message", {})


# ---- 消息历史（用于回填）-------------------------------------------

async def list_chat_messages(chat_id: str, since: datetime
                               ) -> list[dict]:
    """拉一个 chat 在 since 之后的消息（最多 50 条/次，需分页）."""
    d = await _get("/im/v1/messages", {
        "container_id_type": "chat",
        "container_id": chat_id,
        "start_time": int(since.timestamp()),
        "page_size": 50,
    })
    return d.get("data", {}).get("items", [])


async def list_chats() -> list[dict]:
    """所有 bot 可见的 chat（用于回填扫描）."""
    d = await _get("/im/v1/chats")
    return d.get("data", {}).get("items", [])


# ---- 文档变更 -------------------------------------------------------

async def list_recent_docs(since: datetime, page_size: int = 50
                             ) -> list[dict]:
    """按修改时间降序拉文档，按 since 截断。"""
    d = await _get("/drive/v1/files", {
        "order_by": "EditedTime",
        "direction": "DESC",
        "page_size": page_size,
    })
    out = []
    for f in d.get("data", {}).get("files", []):
        try:
            mt = datetime.fromtimestamp(int(f["modified_time"]))
        except (KeyError, ValueError):
            continue
        if mt >= since:
            out.append(f)
    return out
