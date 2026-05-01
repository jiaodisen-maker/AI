"""A1 Discovery Agent — W4 实装。

双通道（PoC MediaCrawler + 生产 OAuth）。W1-W3 阶段降级为 passthrough：直接返回 case_input，
即调用方手动喂 URL。
"""
from typing import Any

from temporalio import activity


@activity.defn
async def discover(case_input: dict[str, Any]) -> dict[str, Any]:
    activity.logger.info("A1 Discovery (W4 stub - passthrough) input=%s", case_input.get("url"))
    return case_input
