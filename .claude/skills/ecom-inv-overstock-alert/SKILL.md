---
name: ecom-inv-overstock-alert
description: |
  库存积压预警。周转 > 120 天的 SKU 自动列出，建议清仓策略
  （打折/赠品/直播清仓/捐赠/报损）。Use when 积压预警 / 滞销预警 / 周转慢.
allowed-tools: [Bash, Read, Write]
triggers: [积压预警, 滞销预警, 周转慢]
ecom: { domain: 09-supply-chain, platform: all, role: 库存, frequency: weekly }
---

# 库存积压预警

## Step 1: 算周转天数
`周转天数 = 库存 / 日均销量`

## Step 2: 三档分类
- **> 180 天**: 🔴 强建议报损 / 捐赠（保健品临期后不可转非保健渠道）
- **120-180 天**: 🟠 直播/社群清仓，配合 `ecom-xiaohongshu-note-topic` 出测评内容拉动
- **90-120 天**: 🟡 降价券 5-10%

## Step 3: 结合效期
若积压 SKU 同时临期 → 合并到 `ecom-inv-batch-expiry-track` 处理。
