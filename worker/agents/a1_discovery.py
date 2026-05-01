"""A1 Discovery Agent — workflow 内的轻量 enrich 节点。

发现批量逻辑在 worker/discovery/ + scripts/discovery_run.py，
进入 workflow 时 case_input 已经带 url + data_lineage。

A1 在 workflow 内职责（极小）：
- 兜底设置 data_lineage（默认 manual）
- 兜底设置 poc_purge_at（poc_crawled 必填，由后续 A2 写库时使用）
- 记录 discovery_meta（如果上游传了）
"""
from __future__ import annotations

import logging
import os
from datetime import UTC, datetime, timedelta
from typing import Any

from temporalio import activity

log = logging.getLogger(__name__)


@activity.defn
async def discover(case_input: dict[str, Any]) -> dict[str, Any]:
    activity.logger.info("A1 Discovery enrich url=%s", case_input.get("url"))

    enriched = dict(case_input)
    enriched.setdefault("data_lineage", "manual")

    if enriched["data_lineage"] == "poc_crawled":
        ttl = int(os.getenv("POC_DATA_TTL_DAYS", "30"))
        enriched.setdefault(
            "poc_purge_at",
            (datetime.now(UTC) + timedelta(days=ttl)).isoformat(),
        )

    return enriched
