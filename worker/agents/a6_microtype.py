"""A6 Microtype Agent — W2 实装。

1) 从 case_segments + atoms 推导 5 维标签
2) 在 microtypes 表查找唯一约束
3) 命中 → 把 microtype_id 回填到 atoms.microtype_ids[]
4) 未命中 → status='candidate' + proposed_by_agent=true + hitl_alert(new_microtype)

W1 阶段：no-op。
"""
from temporalio import activity


@activity.defn
async def classify_microtype(case_id: str) -> dict:
    activity.logger.info("A6 Microtype (W2 stub) case_id=%s", case_id)
    return {"matched": False, "reason": "W2 deliverable"}
