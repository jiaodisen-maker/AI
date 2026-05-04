# 05 · Coze Loop（评测 + 观测 + 提示词管理）

## 是什么

> 字节官方配套的 AI Agent 全生命周期管理平台。**Apache 2.0 开源**。

- 仓库：https://github.com/coze-dev/coze-loop
- SDK：Go / Python / Node
- 集成：Eino、LangChain
- 与 Coze Studio 同期开源（2025-07）

## 三大模块

### 1. Prompt 开发
- 可视化 Playground，实时改实时跑
- 多版本管理（diff、回滚）
- 多模型对比（同 prompt 喂不同模型看输出差异）

### 2. 评测
- 评测集管理（手动 / 自动生成）
- 评测器管理（基于规则 / LLM-as-judge）
- 实验管理（A/B、版本对比）
- 维度：准确性 / 简洁性 / 合规性 / 自定义

### 3. 观测
- 全链路 Trace：用户输入 → prompt 解析 → 模型调用 → 工具执行 → 输出
- 异常自动捕获 + 中间结果留痕
- 标注与回流（人工标注差/好回答 → 进数据集）

## 部署模式

| 模式 | 适合 | 数据 |
|---|---|---|
| **企业版 SaaS 内置** | Coze Pro 用户 | 200 万 Trace/月，180 天 |
| **自部署开源版** | 想完全可控 / 数据敏感 | 自己存 |
| **混合** | bot 在 Coze SaaS，Loop 自部署 | Trace 转出到自家 Loop |

## 替代我们之前要造的轮子

之前在 `coze-control/` 里设想的：

| 想造的 | Coze Loop 已有 |
|---|---|
| `eval.py` 黄金题回归 | ✅ 评测集 + 评测器 |
| `analyze.py` 失败模式 | ✅ Trace 标注 + 回流 |
| `optimize.py` prompt 改写 | ✅ Playground + 多版本对比 |
| `push.py` 守门发布 | ✅ 实验晋级 + 回滚 |

**结论**：删掉 `coze-control/eval`、`push`、`optimize`，全用 Coze Loop。
保留 `coze-control/pull` 当**额外的本地备份**——Loop 没有 git 化的能力。

## 关键决策点

1. **企业版 200 万 Trace 够吗？**
   50 人公司每人每天 100 次工具调用 × 22 天 = 11 万次/月。**完全够**。

2. **Loop 在企业版是默认开还是要单独配？**
   _gaps.md ⑦ —— 需要你贴文档确认。

3. **评测集怎么持续增长？**
   建议机制：用户对 bot 回复 👎 → 自动进 evaluation pending 队列 → 每周人工审 → 进黄金题集。

## 引用源

- [GitHub coze-dev/coze-loop](https://github.com/coze-dev/coze-loop)
- [Coze Loop Wiki](https://github.com/coze-dev/coze-loop/wiki)
- [字节 Coze 开源新闻](https://test-news.aibase.com/news/19989)
