---
name: ecom-fin-ad-spend-reconcile
description: |
  投放费用对账。拉各平台广告账户 充值/消耗/退款 明细，对比财务"预付广告费"
  科目，按渠道出 ROI 财务级归因。Use when 广告费对账 / 投放对账.
allowed-tools: [Bash, Read, Write]
triggers: [广告费对账, 投放对账]
ecom: { domain: 10-finance, role: 财务, frequency: monthly }
---

# 投放费用对账

## Step 1: 拉账户明细
千川 / 万相台 / 京准通 / 多多 / 聚光 / ADQ / 花火 / 知+ / 百度 全部。

## Step 2: 对比 CRM 打款 & 财务预付
真实消耗 = 充值 - 退款 - 余额。

## Step 3: 按渠道 ROI 归因
调 ecom-channel-attribution-split，出财务级含全部平台费/扣点的真实 ROI。

## Step 4: 收票 (广告公司/平台开具)
