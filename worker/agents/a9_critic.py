"""A9 Critic Agent — W3 实装（核心闭环）。

1) 对每条 generated_script，用 ≥3 个不同家族 LLM 盲评：
   Deepseek-V3 / Qwen-Max / Claude-Haiku-4.5
2) rubric: hook / pain / trust / cta / compliance / creativity / exec — 各 1-10
3) 与原 case 对比打分（cross-reference）
4) confidence = 三家评分方差的反比（方差小 = 一致 = confidence 高）
5) confidence < 0.6 → 写 hitl_alert(low_confidence)
6) 写 critic_scores（每脚本 3 行，每个 evaluator 一行）
7) 触发 DSPy 优化：trainset 从 critic_scores 拉历史评分，BootstrapFewShot 重训 A2/A8 prompt，
   写 prompt_versions（含回滚机制：新 prompt 在 N 个 case 指标下降则保留旧版本激活）

返回：{avg_score, confidence, dspy_triggered}
"""
from typing import Any

from temporalio import activity


@activity.defn
async def critique(payload: dict[str, Any]) -> dict[str, Any]:
    raise NotImplementedError("A9 Critic — W3 deliverable")
