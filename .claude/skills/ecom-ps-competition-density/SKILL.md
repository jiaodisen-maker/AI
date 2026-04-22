---
name: ecom-ps-competition-density
description: |
  类目竞争度评估。SKU 数量 / 新品进入难度 / 头部价格带分布 / 平均推广投入。
  Use when 竞争度 / 红海蓝海 / 能进这个类目吗.
allowed-tools: [Bash, Read, Write]
triggers: [竞争度, 红海蓝海, 能进类目吗]
ecom: { domain: 12-product-selection, role: 选品, frequency: monthly }
---

# 竞争度评估

## Step 1: 统计类目 SKU 数 + 近 30 天新品数
## Step 2: 价格带分布直方图
## Step 3: 头部 TOP10 的投放量 (估算)
## Step 4: 综合评分 (红海/中度/蓝海)
