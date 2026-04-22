---
name: ecom-claim-vs-blue-cap-check
description: |
  声明 vs 蓝帽子备案一致性检查。扫全文所有功效/人群/食用量声明，与备案
  信息逐条比对。Use when 批量审核文案 / 新品上架合规 / 备案一致性.
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [批量审核文案, 新品上架合规, 备案一致性]
ecom: { domain: 11-compliance, role: 合规, frequency: on-demand }
---

# 声明 vs 蓝帽子一致性

## Step 1: 读备案
```bash
REG=/home/user/AI/.claude/skills/_ecom/data/blue-cap-registry.json
# 读出 registered_functions / 适宜人群 / 不适宜人群 / 食用量
```

## Step 2: 文案声明抽取 (LLM 做语义分类)
扫全文，分到 4 类: 功效 / 适宜人群 / 不适宜人群 / 食用量

## Step 3: 逐条比对
- 功效 → `ecom-27-function-validator`
- 人群: 备案写的"中老年", 文案不能写"所有人"
- 食用量: 不能超过批文

## Step 4: 输出全量一致性报告
```markdown
# 一致性报告
- 总声明数: N
- 一致: X  不一致: Y
- 必改: ...
```
