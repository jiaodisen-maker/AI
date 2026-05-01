"""DSPy prompt optimizer — W3 实装。

入口：
- optimize_decomposition(trainset) → 写 prompt_versions(agent='a2', ...)
- optimize_generation(trainset) → 写 prompt_versions(agent='a8', ...)

回滚机制：
- 新 prompt 跑 N 个 case，若 critic 平均分较旧 prompt 下降 >threshold，回滚（保留旧 active 版本）
- 触发条件：A9 Critic 累计 K 条新 critic_scores 后调用一次
"""
