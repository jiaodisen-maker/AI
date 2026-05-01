"""A6 Microtype Agent — W2 实装。

1) 从 case_segments + atoms 推导 5 维标签（场景 / 人群 / 成分 / 情绪 / 限制）
2) 在 microtypes 表查找 (scene, audience, ingredient, emotion, restriction) 唯一约束
3) 命中 → 把 microtype_id 回填到 atoms.microtype_ids[]
4) 未命中 → 写 status='candidate' + proposed_by_agent=true + 触发 hitl_alert(new_microtype)
"""
from temporalio import activity


@activity.defn
async def classify_microtype(case_id: str) -> None:
    raise NotImplementedError("A6 Microtype — W2 deliverable")
