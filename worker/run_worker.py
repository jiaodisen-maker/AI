"""Temporal worker entrypoint. Registers AgenticInsight workflow + 9 Agent activities.

Run: python -m worker.run_worker
"""
import asyncio
import os

from temporalio.client import Client
from temporalio.worker import Worker

from .agents import (
    a1_discovery,
    a2_decomposition,
    a3_compliance,
    a4_userpain,
    a5_conversion,
    a6_microtype,
    a7_feasibility,
    a8_generation,
    a9_critic,
)
from .workflows.agentic_insight import AgenticInsightWorkflow


async def main() -> None:
    client = await Client.connect(
        os.getenv("TEMPORAL_ADDRESS", "localhost:7233"),
        namespace=os.getenv("TEMPORAL_NAMESPACE", "default"),
    )

    activities = [
        a1_discovery.discover,
        a2_decomposition.decompose,
        a3_compliance.scan_compliance,
        a4_userpain.match_userpain,
        a5_conversion.fetch_conversion,
        a6_microtype.classify_microtype,
        a7_feasibility.score_feasibility,
        a8_generation.generate_scripts,
        a9_critic.critique,
    ]

    worker = Worker(
        client,
        task_queue=os.getenv("TEMPORAL_TASK_QUEUE", "agentic-insight"),
        workflows=[AgenticInsightWorkflow],
        activities=activities,
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
