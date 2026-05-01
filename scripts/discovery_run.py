"""Batch discovery driver — 调 A1 通道发现 N 个 case，逐一起 AgenticInsight workflow。

用法：
    python scripts/discovery_run.py --channel poc --query 氨糖 --n 5
    python scripts/discovery_run.py --channel prod --query 益生菌 --n 10
"""
import argparse
import asyncio
import os
import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from temporalio.client import Client  # noqa: E402

from worker.discovery import discover  # noqa: E402


async def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--channel", required=True, choices=["poc", "prod"])
    p.add_argument("--query", required=True)
    p.add_argument("--n", type=int, default=5)
    p.add_argument("--task-queue", default=os.getenv("TEMPORAL_TASK_QUEUE", "agentic-insight"))
    p.add_argument("--temporal", default=os.getenv("TEMPORAL_ADDRESS", "localhost:7233"))
    p.add_argument("--namespace", default=os.getenv("TEMPORAL_NAMESPACE", "default"))
    args = p.parse_args()

    cases = discover(args.channel, args.query, args.n)
    print(f"Discovered {len(cases)} cases via channel={args.channel} query={args.query}")
    if not cases:
        print("(empty — check feature flags / OAuth creds / crawler install)")
        return 0

    client = await Client.connect(args.temporal, namespace=args.namespace)

    started: list[tuple[str, str]] = []
    for c in cases:
        wf_id = f"agentic-insight-{uuid.uuid4()}"
        payload = dict(c)
        payload["trigger"] = "auto"
        await client.start_workflow(
            "AgenticInsightWorkflow",
            payload,
            id=wf_id,
            task_queue=args.task_queue,
        )
        started.append((wf_id, c["url"]))

    print(f"Started {len(started)} workflows:")
    for wf, url in started:
        print(f"  {wf}  url={url}")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
