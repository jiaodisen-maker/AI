"""A3 Compliance Agent — W1 实装。

1) 加载 rules/banned_terms_14categories.yaml 到内存
2) 对 case_segments.asr_text + ocr_text 做 14 类正则匹配
3) Deepseek-V3 双验：LLM 对漏检 case 提候选（写 hitl_alert，不直接覆盖）
4) 命中即写 atoms.compliance_grade='R' 或 'Y'，并写 cross_validations.agent='a3_compliance'
"""
from temporalio import activity


@activity.defn
async def scan_compliance(case_id: str) -> None:
    raise NotImplementedError("A3 Compliance — W1 deliverable")
