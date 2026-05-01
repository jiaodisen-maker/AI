"""A7 Feasibility Agent — W2 实装。

对每条 atom 做 4 维评分（机器友好度 / 数据依赖度 / 合规自动化度 / 正交性），
用多 LLM 互评（Deepseek + Qwen + Claude）取均值。

任何一项 ≤4 分的原子触发改写或拆细（A7 自驱重写）。
写 atoms.feasibility_4d JSONB + cross_validations.agent='a7_feasibility'
"""
from temporalio import activity


@activity.defn
async def score_feasibility(case_id: str) -> None:
    raise NotImplementedError("A7 Feasibility — W2 deliverable")
