---
name: ecom-ps-competitor-review-mine
description: |
  竞品评价挖掘。抓差评 / 中评 / 好评 做 topic cluster, 找竞品槽点作为本品
  差异化机会。Use when 竞品评价 / 差评挖掘 / 竞品槽点.
allowed-tools: [Bash, Read, Write]
triggers: [竞品评价, 差评挖掘, 竞品槽点]
ecom: { domain: 12-product-selection, role: 选品, frequency: monthly }
---

# 竞品评价挖掘

## Step 1: 抓评价
各平台评价页 (尤其近 30 天)。

## Step 2: 情感 + 主题
sentiment (正/负) × topic (功效/口味/包装/物流/价格/客服)。

## Step 3: 识别共性槽点
Top 3 负面主题 → 本品改进方向。

## Step 4: 识别共性好评
Top 3 正面主题 → 本品学习方向。
