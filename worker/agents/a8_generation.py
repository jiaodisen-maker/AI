"""A8 Generation Agent — W3 实装。

1) 读 cases.data_lineage 决定 for_internal_research_only：poc_crawled → True，否则 False
2) 选当前 case 归属的 microtype + 同 microtype 下高质量 atoms（compliance_grade<>R, feasibility ≥6）
3) 用 DSPy signature `GenerationSig(microtype, atoms) -> script`
4) 生成 N=5 候选脚本，写 generated_scripts（trigger 强校验 PoC 隔离）
"""
from temporalio import activity


@activity.defn
async def generate_scripts(case_id: str) -> list[str]:
    raise NotImplementedError("A8 Generation — W3 deliverable")
