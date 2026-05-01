"""A4 UserPain Agent — W2 实装。

1) 从 case_segments 提取 pain 段落
2) bge-large-zh-v1.5 嵌入
3) 在 userpain_clusters.embedding 上做 top-k 相似召回
4) Deepseek-V3 判定"真痛点 / 伪痛点 / 营销造痛点"
5) 写 cross_validations.agent='a4_userpain'

W1 阶段：no-op，让 workflow 能端到端跑通。
"""
from temporalio import activity


@activity.defn
async def match_userpain(case_id: str) -> dict:
    activity.logger.info("A4 UserPain (W2 stub) case_id=%s", case_id)
    return {"verdict": "skipped", "reason": "W2 deliverable"}
