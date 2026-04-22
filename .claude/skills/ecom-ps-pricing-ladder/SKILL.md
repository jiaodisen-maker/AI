---
name: ecom-ps-pricing-ladder
description: |
  定价梯度 + 锚点策略。单瓶 / 三瓶装 / 年套装 三档 + 原价 / 日常价 / 直播价
  / 大促价 四档锚点。Use when 定价 / 价格策略 / 锚定.
allowed-tools: [Read, Write]
triggers: [定价, 价格策略, 锚定]
ecom: { domain: 12-product-selection, role: 选品, frequency: on-demand }
---

# 定价梯度

## Step 1: 市场对标
同类爆款价格分布。

## Step 2: 单价阶梯
- 单瓶: 引流装
- 三瓶装 (8.5 折): 主推
- 年套装 (7 折): 利润品 + 锁客

## Step 3: 场景价梯
- 原价 (参考价)
- 日常券后价
- 直播价 (加赠)
- 大促价 (封顶)

## Step 4: 毛利保底
每档算毛利, 直播价不低于 X%.
