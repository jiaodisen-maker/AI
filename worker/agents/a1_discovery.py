"""A1 Discovery Agent — W4 实装。

双通道：
- PoC 通道：MediaCrawler / DrissionPage 抓抖音 / 小红书公开 case URL（仅 metadata + 视频地址，
  不抓评论 / 不模拟登录）；写 cases.data_lineage='poc_crawled' + poc_purge_at=now()+30d
- 生产通道：抖音 OpenAPI + 巨量创意中心 API；写 data_lineage='public_api' 或 'oauth'

W4 之前可降级为"接受手动 URL"——直接返回入参 case_input。
"""
from typing import Any

from temporalio import activity


@activity.defn
async def discover(case_input: dict[str, Any]) -> dict[str, Any]:
    raise NotImplementedError("A1 Discovery — W4 deliverable")
