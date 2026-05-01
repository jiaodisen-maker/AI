"""A7 Feasibility Agent — W2 实装。

对每条 atom 做 4 维评分（机器友好度 / 数据依赖度 / 合规自动化度 / 正交性），
多 LLM 互评（Deepseek + Qwen + Claude）取均值。任何一项 ≤4 分的原子触发改写或拆细。
写 atoms.feasibility_4d JSONB + cross_validations.agent='a7_feasibility'

W1 阶段：no-op。
"""
from temporalio import activity


@activity.defn
async def score_feasibility(case_id: str) -> dict:
    activity.logger.info("A7 Feasibility (W2 stub) case_id=%s", case_id)
    return {"verdict": "skipped", "reason": "W2 deliverable"}
