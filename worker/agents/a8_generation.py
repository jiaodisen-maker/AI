"""A8 Generation Agent — W3 实装。

1) 读 cases.data_lineage 决定 for_internal_research_only：poc_crawled → True，否则 False
2) 选当前 case 归属的 microtype + 同 microtype 下高质量 atoms
3) 用 DSPy GenerationSig 反向生成 N=5 候选脚本
4) 写 generated_scripts（trigger 强校验 PoC 隔离）

W1 阶段：no-op。
"""
from temporalio import activity


@activity.defn
async def generate_scripts(case_id: str) -> list[str]:
    activity.logger.info("A8 Generation (W3 stub) case_id=%s", case_id)
    return []
