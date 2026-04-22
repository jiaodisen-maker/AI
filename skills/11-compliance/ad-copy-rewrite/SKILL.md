---
name: ad-copy-rewrite
domain: 11-compliance
platform: all
role: 合规
frequency: on-demand
inputs:
  - original_copy
  - violation_report (来自 forbidden-word-scan 或 27-function-validator)
outputs:
  - 改写后的合规文案
  - 改写前后对比
human_review_required: true
compliance_filter: false
data_sources:
  - 合规替代词库
  - 历史"过审"文案库
allowed-tools:
  - Read
  - Write
---

# 不合规文案自动改写 (`ad-copy-rewrite`)

## 何时调用
`forbidden-word-scan` 命中 medium/high 后，先尝试自动改写再人工审。

## 输入
- **original_copy** — string
- **violation_report** — 命中词列表

## 输出
- `rewritten_copy` — 改写后文案
- `diff` — 原文 vs 改写 对比
- `confidence` — 改写置信度 0-1

## Workflow
1. 解析命中词 → 查合规替代词库
2. 用"能用的话术"重构句子 (保留原卖点, 只改表达)
3. 再过 `forbidden-word-scan` 验证
4. 若二次命中 → 放弃改写, 返回人工
5. 若通过 → 输出改写结果 + diff
6. 记录到经验库: 每次人工最终版 vs 自动改写 → diff → 更新替代库

## 改写策略
- 绝对化词 → 描述性词 (最好吸收 → 采用专利工艺促进吸收)
- 疗效词 → 支持性词 (治疗便秘 → 有助于润肠通便)
- 保证词 → 成分描述 (100% 有效 → 含 20g 优质胶原蛋白)
- 谐音黑话 → 禁用, 不可改写, 必须删除
