---
name: fin-ad-spend-reconcile
domain: 10-finance
platform: all
role: 财务
frequency: monthly
inputs: [billing_period, account_list]
outputs: [广告账户对账表 + 发票收集清单]
human_review_required: true
data_sources: [千川/万相台/京准通/多多/聚光/ADQ/知+/百度/花火 账单]
allowed-tools: [Bash, Read, Write]
---

# 投放费用对账 (`fin-ad-spend-reconcile`)

## Workflow
1. 拉每个平台广告账户的充值/消耗明细
2. 对比内部 CRM 打款记录
3. 对比财务"预付账款-广告费"科目
4. 计算真实消耗 = 充值 - 退款 - 余额
5. 按渠道 ROI 归因: [channel-attribution-split](../../06-data-analytics/channel-attribution-split/)
6. 收集平台发票 (广告公司开具 / 平台开具)
7. 生成财务级 ROI 报表

## 常见差异
- 充值优惠券未计入可用金额
- 消耗明细与财务账单延迟
- 跨账户资金调配未记录
