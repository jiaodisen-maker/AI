---
name: fin-refund-reconcile
domain: 10-finance
platform: all
role: 财务
frequency: weekly
inputs: [billing_period]
outputs: [三方对账报告, 异常退款清单]
human_review_required: true
data_sources: [平台退款记录, 银行流水, ERP 退货单]
allowed-tools: [Bash, Read, Write]
---

# 退款三方对账 (`fin-refund-reconcile`)

## Workflow
1. 拉每个平台的退款明细 (按订单号)
2. 拉银行流水 (按退款打款记录)
3. 拉 ERP 退货单 (按订单号)
4. 三方匹配:
   - 平台已退 → 银行已付 → ERP 有退货 → 正常
   - 平台已退 → 银行已付 → ERP 无退货 → 异常 (仅退款/丢包?)
   - 平台已退 → 银行未付 → 异常 (需追)
5. 生成差异清单 + 责任人

## 保健品特殊
- 质量问题 / 过敏反馈退款需单独档 (留档以防投诉)
- 跨境保健品退款涉及关税
