"""AgenticInsight workflow — 9 Agent 全自动流水线骨架。

W1 实装：A2/A3 串到 cases + atoms + cross_validations 落库
W2 加：A4/A5/A6/A7
W3 加：A8/A9 + DSPy 自闭环
W4 加：A1 Discovery（PoC + 生产双通道）
"""
from datetime import timedelta
from typing import Any

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from ..agents import a1_discovery, a2_decomposition, a3_compliance, a4_userpain
    from ..agents import a5_conversion, a6_microtype, a7_feasibility, a8_generation, a9_critic


@workflow.defn
class AgenticInsightWorkflow:
    @workflow.run
    async def run(self, case_input: dict[str, Any]) -> dict[str, Any]:
        # case_input: {"url": ..., "data_lineage": ..., "trigger": "manual"|"auto"}

        # A1 Discovery (auto trigger only) — W4
        if case_input.get("trigger") == "auto":
            case_input = await workflow.execute_activity(
                a1_discovery.discover,
                case_input,
                start_to_close_timeout=timedelta(minutes=10),
            )

        # A2 Decomposition — W1
        case_id = await workflow.execute_activity(
            a2_decomposition.decompose,
            case_input,
            start_to_close_timeout=timedelta(minutes=30),
        )

        # 4 路交叉验证（A3 W1, A4/A5/A7 W2）— 并行
        import asyncio
        await asyncio.gather(
            workflow.execute_activity(
                a3_compliance.scan_compliance,
                case_id,
                start_to_close_timeout=timedelta(minutes=5),
            ),
            workflow.execute_activity(
                a4_userpain.match_userpain,
                case_id,
                start_to_close_timeout=timedelta(minutes=5),
            ),
            workflow.execute_activity(
                a5_conversion.fetch_conversion,
                case_id,
                start_to_close_timeout=timedelta(minutes=5),
            ),
            workflow.execute_activity(
                a7_feasibility.score_feasibility,
                case_id,
                start_to_close_timeout=timedelta(minutes=10),
            ),
        )

        # A6 Microtype 归类 — W2
        await workflow.execute_activity(
            a6_microtype.classify_microtype,
            case_id,
            start_to_close_timeout=timedelta(minutes=5),
        )

        # A8 Generation — W3
        script_ids = await workflow.execute_activity(
            a8_generation.generate_scripts,
            case_id,
            start_to_close_timeout=timedelta(minutes=15),
        )

        # A9 Critic — W3 (核心闭环)
        critic_summary = await workflow.execute_activity(
            a9_critic.critique,
            {"case_id": case_id, "script_ids": script_ids},
            start_to_close_timeout=timedelta(minutes=15),
        )

        return {"case_id": case_id, "script_ids": script_ids, "critic": critic_summary}
