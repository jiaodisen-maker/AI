---
name: ecom-inv-stockout-alert
description: |
  缺货预警。按当前库存 / 日均销量 算剩余天数，<7 天飞书告警，<3 天升级到老板 +
  建议关千川计划避免投浪费的钱。Use when 缺货预警 / 库存预警 / 断货风险.
allowed-tools: [Bash, Read, Write]
triggers: [缺货预警, 断货风险, 库存预警]
ecom: { domain: 09-supply-chain, platform: all, role: 库存, frequency: hourly }
---

# 缺货预警

## Step 1: 拉库存 + 日均销量
同 `ecom-inv-stock-dashboard` 拉库存；销量用近 7 天均值。

## Step 2: 算剩余天数
`days_left = available_stock / avg_daily_sales`

## Step 3: 三档告警
- **< 3 天**: 🔴 飞书 @ 老板 + 建议 `ecom-qianchuan-realtime-optimize` 暂停该 SKU 投放
- **< 7 天**: 🟠 飞书 @ 供应链
- **< 14 天**: 🟡 周报

## Step 4: 触发补货
若 < 7 天且未在途 → 自动触发 `ecom-inv-replenish-plan` 生成补货单。
