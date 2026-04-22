---
name: fin-jd-bill-reconcile
domain: 10-finance
platform: jd
role: 财务
frequency: monthly
inputs: [billing_period, store_id]
outputs: [对账报告, 差异明细]
human_review_required: true
data_sources: [京东商家后台账单, 京准通账单, ERP]
allowed-tools: [Bash, Read, Write, WebFetch]
---

# 京东货款对账 (`fin-jd-bill-reconcile`)

## Workflow
1. 京东商家后台 → 财务 → 账单中心 导出
2. 京准通消耗导出
3. ERP 成交/退款单导出
4. 对账逻辑: 货款 = 成交 - 扣点 (5-8% POP) - 京准通消耗 - 退款
5. 差异定位 + 对账报告
6. 特别关注: POP vs 自营 扣点不同, 京东物流费单独出账

## 京东特有
- 账期: T+15 / T+30 / T+45 (依据合作类型)
- 结算方式: 货款 - 违规扣款 - 服务费
- 预留金 / 保证金 核对
