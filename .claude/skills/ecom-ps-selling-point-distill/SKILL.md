---
name: ecom-ps-selling-point-distill
description: |
  卖点提炼。从成分 + 工艺 + 认证 + 对比 提炼 TOP 5 卖点,
  每个卖点给 合规话术 + 场景例句 + 视觉建议。Use when 提卖点 / 卖点提炼.
allowed-tools: [Bash, Read, Write]
triggers: [提卖点, 卖点提炼, 提炼卖点]
ecom: { domain: 12-product-selection, role: 选品, frequency: on-demand }
---

# 卖点提炼

## Step 1: 读产品档案
配方 / 工艺 / 认证 / COA / 蓝帽子。

## Step 2: 五维提炼 (FABE 模型)
- Feature: 原料 / 含量
- Advantage: vs 市面通常产品
- Benefit: 合规功效 (27 项内)
- Evidence: 检测报告 / 认证

## Step 3: 合规筛
```bash
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
for SP in 卖点候选; do scan_forbidden "$SP"; done
```

## Step 4: 输出 TOP 5 + 话术变体
