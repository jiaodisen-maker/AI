---
name: ecom-fin-refund-reconcile
description: |
  退款三方对账: 平台退款 × 银行流水 × ERP 退货单 三方匹配，识别异常退款
  (仅退款无退货 / 已退无流水)。Use when 退款对账 / 三方对账 / 仅退款核查.
allowed-tools: [Bash, Read, Write]
triggers: [退款对账, 三方对账, 仅退款核查]
ecom: { domain: 10-finance, role: 财务, frequency: weekly }
---

# 退款三方对账

## Step 1: 三源拉取
- 各平台退款 API (按订单号)
- 银行流水 (按退款付款)
- ERP 退货单 (按订单号)

## Step 2: 匹配 + 标异常
```python
# 平台已退 × 银行已付 × ERP 有退 → 正常
# 其他组合 → 异常清单
```

## Step 3: 保健品特殊档
质量问题/过敏反馈退款单独留档。跨境退款涉关税单列。
