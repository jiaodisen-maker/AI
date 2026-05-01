"""A9 Critic Agent — W3 实装（核心闭环）。

≥3 个不同家族 LLM 盲评 + DSPy 自优化触发。详见 v6 §14.1 + §14.9 护栏。

W1 阶段：no-op。
"""
from typing import Any

from temporalio import activity


@activity.defn
async def critique(payload: dict[str, Any]) -> dict[str, Any]:
    activity.logger.info("A9 Critic (W3 stub) payload=%s", payload)
    return {"avg_score": None, "confidence": None, "dspy_triggered": False}
