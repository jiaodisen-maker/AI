"""Temporal workflow 包裹 scripts/poc_purge.py 的逻辑，用于 Schedule 自动触发。"""
from __future__ import annotations

from datetime import timedelta

from temporalio import activity, workflow


@activity.defn
async def run_poc_purge() -> dict:
    """直接复用 scripts/poc_purge 的核心逻辑（导入即跑 main）。"""
    # 在 activity 里 import，避免 workflow sandbox 限制
    import sys
    from pathlib import Path

    project_root = Path(__file__).resolve().parents[2]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    from scripts.poc_purge import main  # type: ignore[import-not-found]

    rc = main()
    return {"rc": rc}


@workflow.defn
class PocPurgeWorkflow:
    @workflow.run
    async def run(self) -> dict:
        return await workflow.execute_activity(
            run_poc_purge,
            start_to_close_timeout=timedelta(minutes=30),
        )
