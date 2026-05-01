"""创建 Temporal Schedule，让 poc_purge 每天 03:00 自动跑。

依赖 Temporal client + 一个简单的 PocPurgeWorkflow（worker/workflows/poc_purge.py）。
"""
from __future__ import annotations

import asyncio
import os
import sys
from datetime import timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from temporalio.client import (  # noqa: E402
    Client,
    Schedule,
    ScheduleActionStartWorkflow,
    ScheduleIntervalSpec,
    ScheduleSpec,
    ScheduleState,
)


async def main() -> int:
    client = await Client.connect(
        os.getenv("TEMPORAL_ADDRESS", "localhost:7233"),
        namespace=os.getenv("TEMPORAL_NAMESPACE", "default"),
    )

    schedule_id = "poc-purge-daily"
    task_queue = os.getenv("TEMPORAL_TASK_QUEUE", "agentic-insight")

    schedule = Schedule(
        action=ScheduleActionStartWorkflow(
            "PocPurgeWorkflow",
            id=schedule_id + "-wf",
            task_queue=task_queue,
        ),
        spec=ScheduleSpec(
            intervals=[ScheduleIntervalSpec(every=timedelta(days=1))],
        ),
        state=ScheduleState(note="auto-created by setup_purge_schedule.py"),
    )

    try:
        await client.create_schedule(schedule_id, schedule)
        print(f"Created Temporal schedule: {schedule_id} (every 24h, runs PocPurgeWorkflow)")
    except Exception as e:
        if "already exists" in str(e).lower():
            print(f"Schedule {schedule_id} already exists; skip")
        else:
            print(f"Failed: {e}")
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
