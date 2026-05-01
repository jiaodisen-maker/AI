"""A1 Discovery 模块 — 双通道实装。

- poc_crawler: MediaCrawler / DrissionPage 抓抖音 / 小红书公开 case
- oauth_api: 抖音 OpenAPI + 巨量创意中心（合规栈 α）

调用入口：worker.discovery.discover(channel, query, n) → list[CaseInput]
"""
from typing import Any, TypedDict


class CaseInput(TypedDict, total=False):
    url: str
    data_lineage: str       # poc_crawled / public_api / oauth
    platform: str | None
    brand: str | None
    sku: str | None
    category: str | None
    manual_payload: dict[str, Any] | None
    discovery_meta: dict[str, Any] | None


def discover(channel: str, query: str, n: int = 5) -> list[CaseInput]:
    if channel == "poc":
        from .poc_crawler import discover_poc

        return discover_poc(query, n)
    if channel in ("prod", "oauth", "public_api"):
        from .oauth_api import discover_oauth

        return discover_oauth(query, n)
    raise ValueError(f"unknown channel: {channel!r} (expected poc / prod)")


__all__ = ["CaseInput", "discover"]
