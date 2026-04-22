---
name: ecom-ps-margin-feasibility
description: |
  毛利测算。出厂价 + 平台扣点 + 物流 + 营销 + 退货损耗 → 算真实毛利率。
  Use when 算毛利 / 成本结构 / 这个价能不能做.
allowed-tools: [Read, Write, AskUserQuestion]
triggers: [算毛利, 成本结构, 价能不能做]
ecom: { domain: 12-product-selection, role: 选品, frequency: on-demand }
---

# 毛利测算

## Step 1: 拿出厂价 + 目标售价
AskUserQuestion 补齐。

## Step 2: 加扣点
- 天猫 3-5%
- 京东 5-8%
- 抖音 10% (保健品)
- 拼多多 + 提现手续费
- 小红书 5-10%

## Step 3: 加营销 / 退货
- CAC (千川 ROI 倒推)
- 退货率 (类目平均 15-25% 保健品)

## Step 4: 真实毛利
`毛利 = 售价 - 成本 - 扣点 - 物流 - 营销摊销 - 退货损耗`

## Step 5: 输出毛利敏感度表
各变量 ±10% 毛利变化。
