"""生产 Discovery 通道 — 抖音 OpenAPI + 巨量创意中心 API（合规栈 α）。

仅自家账号 OAuth + 巨量创意中心公开素材 API。
缺凭据时返回空列表 + WARNING（不报错，让 W4 联调能跑）。
"""
from __future__ import annotations

import logging
import os

import httpx

log = logging.getLogger(__name__)

DOUYIN_OPEN_BASE = "https://open.douyin.com"
JULIANG_CREATIVE_BASE = "https://open.oceanengine.com"


def _has_creds() -> bool:
    return bool(
        os.getenv("DOUYIN_OAUTH_CLIENT_ID")
        and os.getenv("DOUYIN_OAUTH_CLIENT_SECRET")
    )


def _douyin_self_videos(access_token: str, n: int) -> list[dict]:
    """自家账号 OAuth — 拉本账号已发布视频列表。"""
    headers = {"access-token": access_token}
    params = {"open_id": os.environ["DOUYIN_OPEN_ID"], "count": n}
    with httpx.Client(timeout=10.0) as c:
        r = c.get(f"{DOUYIN_OPEN_BASE}/api/douyin/v1/video/video_list/", headers=headers, params=params)
        r.raise_for_status()
        data = r.json()
    items = data.get("data", {}).get("list", [])
    return [
        {
            "url": it.get("share_url") or it.get("aweme_id"),
            "platform": "douyin",
            "discovery_meta": {
                "aweme_id": it.get("aweme_id"),
                "create_time": it.get("create_time"),
                "title": it.get("title"),
                "stats": it.get("statistics"),
            },
        }
        for it in items
    ]


def _juliang_creative_search(query: str, n: int) -> list[dict]:
    """巨量创意中心 — 搜索公开素材（行业可见）。"""
    api_key = os.getenv("QIANCHUAN_API_KEY")
    if not api_key:
        return []
    headers = {"Access-Token": api_key}
    params = {"keyword": query, "page_size": n}
    url = f"{JULIANG_CREATIVE_BASE}/open_api/v1.0/creative/search/"
    try:
        with httpx.Client(timeout=10.0) as c:
            r = c.get(url, headers=headers, params=params)
            r.raise_for_status()
            data = r.json()
        items = data.get("data", {}).get("list", [])
        return [
            {
                "url": it.get("video_url"),
                "platform": "juliang_creative",
                "discovery_meta": {
                    "creative_id": it.get("id"),
                    "category": it.get("category"),
                    "industry": it.get("industry"),
                },
            }
            for it in items
        ]
    except Exception as e:
        log.warning("juliang creative search failed: %s", e)
        return []


def discover_oauth(query: str, n: int = 5) -> list[dict]:
    if not _has_creds():
        log.warning("oauth discovery: DOUYIN_OAUTH_CLIENT_ID not set; returning empty")
        return []

    cases: list[dict] = []

    # 巨量创意中心（公开素材，标 public_api）
    creative = _juliang_creative_search(query, n)
    for c in creative:
        c["data_lineage"] = "public_api"
    cases.extend(creative)

    # 自家账号视频（标 oauth）— 需事先完成 OAuth flow 拿到 access_token
    access_token = os.getenv("DOUYIN_ACCESS_TOKEN")
    if access_token and os.getenv("DOUYIN_OPEN_ID"):
        try:
            mine = _douyin_self_videos(access_token, n)
            for c in mine:
                c["data_lineage"] = "oauth"
            cases.extend(mine)
        except Exception as e:
            log.warning("douyin self videos failed: %s", e)

    return cases[:n]
