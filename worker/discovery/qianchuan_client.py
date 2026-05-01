"""千川 Marketing API client — 视频维度 metrics 拉取。

API 文档：https://open.oceanengine.com/labels/7/docs/1696710652103694
- /open_api/v1.0/qianchuan/material/video/get/  视频信息
- /open_api/v3.0/qianchuan/report/aweme/get/    抖音视频投放报表（CPM/CTR/CVR/GMV）
"""
from __future__ import annotations

import logging
from datetime import date, timedelta
from typing import Any

import httpx

from .oauth_tokens import get_token

log = logging.getLogger(__name__)

BASE_URL = "https://ad.oceanengine.com"


class QianchuanClient:
    def __init__(self, account_id: str):
        tok = get_token("qianchuan", account_id)
        if tok is None or not tok.access_token:
            raise RuntimeError(f"no qianchuan oauth token for account_id={account_id}")
        if not tok.advertiser_id:
            raise RuntimeError("qianchuan token missing advertiser_id")
        self.access_token = tok.access_token
        self.advertiser_id = tok.advertiser_id

    @property
    def _headers(self) -> dict[str, str]:
        return {"Access-Token": self.access_token}

    def video_info(self, item_id: str) -> dict[str, Any]:
        params = {
            "advertiser_id": self.advertiser_id,
            "item_id": item_id,
        }
        with httpx.Client(timeout=10.0) as c:
            r = c.get(f"{BASE_URL}/open_api/v1.0/qianchuan/material/video/get/",
                      headers=self._headers, params=params)
            r.raise_for_status()
        return r.json().get("data", {})

    def video_report(self, item_id: str, days: int = 7) -> dict[str, Any]:
        end = date.today()
        start = end - timedelta(days=days)
        payload = {
            "advertiser_id": self.advertiser_id,
            "start_date": start.isoformat(),
            "end_date": end.isoformat(),
            "filtering": {"item_ids": [item_id]},
            "fields": ["cpm", "ctr", "cvr", "play_over_rate", "stat_cost", "total_pay_amount"],
        }
        with httpx.Client(timeout=10.0) as c:
            r = c.post(f"{BASE_URL}/open_api/v3.0/qianchuan/report/aweme/get/",
                       headers=self._headers, json=payload)
            r.raise_for_status()
        return r.json().get("data", {})


def fetch_metrics(account_id: str, item_id: str) -> dict | None:
    """统一入口：失败返回 None（让 A5 走 graceful path）。"""
    try:
        cli = QianchuanClient(account_id)
        info = cli.video_info(item_id)
        report = cli.video_report(item_id)
        return {"info": info, "report": report}
    except Exception as e:
        log.warning("qianchuan fetch failed account=%s item=%s: %s", account_id, item_id, e)
        return None
