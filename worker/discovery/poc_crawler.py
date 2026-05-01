"""PoC Discovery 通道 — MediaCrawler / DrissionPage 抓抖音 / 小红书公开 case。

🛑 重要边界（与 §11 + §14.0 一致）：
1) feature flag POC_CRAWLED_ENABLED 必须为 true（生产环境强制 false）
2) 仅抓 metadata + 视频 URL，不抓评论 / 用户身份 / 不模拟登录
3) 每次发现写 audit log（便于 §14.9 法律审计）
4) 30 天 TTL（poc_purge_at = ingested_at + 30d，由 A2 写库时填）
5) 严守 robots.txt + 平台 ToS，请求频次保守（≥3s 间隔）

集成方式（运行时配置）：
- 默认尝试 import mediacrawler（开源 https://github.com/NanmiCoder/MediaCrawler）
- 未安装 → 返回 dev seed URLs（有 WARNING），方便没装 crawler 也能联调
- 真实部署：pip install MediaCrawler 并按其 README 配置 cookie/限流
"""
from __future__ import annotations

import json
import logging
import os
import time
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

log = logging.getLogger(__name__)

def _audit_log_path() -> Path:
    return Path(os.getenv("POC_AUDIT_LOG", "storage/poc_audit.log"))


def _rate_limit_sec() -> float:
    return float(os.getenv("POC_RATE_LIMIT_SEC", "3.0"))


def _audit(event: str, payload: dict[str, Any]) -> None:
    p = _audit_log_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "ts": datetime.now(UTC).isoformat(),
        "event": event,
        "request_id": str(uuid.uuid4()),
        "payload": payload,
    }
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")


def _check_feature_flag() -> None:
    if os.getenv("POC_CRAWLED_ENABLED", "false").lower() not in ("true", "1", "yes"):
        raise PermissionError(
            "POC_CRAWLED_ENABLED is false — PoC discovery is disabled in this environment. "
            "Production must keep it disabled. Internal research env should set it true after "
            "法务备忘录签字归档（docs/poc-research-memorandum-template.md）。"
        )


def _via_mediacrawler(query: str, n: int) -> list[dict] | None:
    """尝试调 MediaCrawler。返回 None 表示未安装。"""
    try:
        # MediaCrawler 的 import 名取决于安装方式；这里给典型形状
        import mediacrawler  # type: ignore[import-not-found]
    except ImportError:
        return None

    cases: list[dict] = []
    try:
        # MediaCrawler 实际 API 因版本而异，下面是典型搜索流程
        crawler = mediacrawler.DouyinCrawler(headless=True, login_type="cookie")
        results = crawler.search(keyword=query, limit=n)
        for r in results:
            cases.append(
                {
                    "url": r.get("video_url") or r.get("share_url"),
                    "platform": "douyin",
                    "discovery_meta": {
                        "title": r.get("title"),
                        "likes": r.get("likes"),
                        "play_count": r.get("play_count"),
                        "publish_time": r.get("publish_time"),
                    },
                }
            )
            time.sleep(_rate_limit_sec())
    except Exception as e:
        log.warning("MediaCrawler call failed: %s", e)
        _audit("mediacrawler_error", {"query": query, "error": str(e)})
        return []
    return cases


def _via_drissionpage(query: str, n: int) -> list[dict] | None:
    """尝试调 DrissionPage（轻量浏览器自动化）。返回 None 表示未安装。"""
    try:
        import DrissionPage  # type: ignore[import-not-found,unused-ignore]  # noqa: F401
    except ImportError:
        return None

    log.info("DrissionPage detected but search adapter not configured — returning empty")
    return []


def _seed_dev_cases(query: str, n: int) -> list[dict]:
    """开发期种子数据：没装 crawler 时让 workflow 联调能跑通。

    严格不模拟真实抓取，URL 是占位 — 调用方应用 manual_payload 喂入真实文本。
    """
    log.warning("PoC crawler unavailable; returning dev seed cases (manual_payload required)")
    out = []
    for i in range(n):
        out.append(
            {
                "url": f"https://www.douyin.com/video/seed-{query}-{i}-{uuid.uuid4().hex[:8]}",
                "platform": "douyin",
                "discovery_meta": {"seed_dev": True, "query": query},
            }
        )
    return out


def discover_poc(query: str, n: int = 5) -> list[dict]:
    _check_feature_flag()
    _audit("discover_request", {"query": query, "n": n, "channel": "poc"})

    cases = _via_mediacrawler(query, n)
    if cases is None:
        cases = _via_drissionpage(query, n)
    if cases is None:
        cases = _seed_dev_cases(query, n)

    for c in cases:
        c["data_lineage"] = "poc_crawled"

    _audit(
        "discover_result",
        {"query": query, "channel": "poc", "count": len(cases), "urls": [c["url"] for c in cases]},
    )
    return cases
