---
name: fin-pdd-bill-reconcile
domain: 10-finance
platform: pdd
role: 财务
frequency: monthly
inputs: [billing_period, store_id]
outputs: [对账报告]
human_review_required: true
data_sources: [拼多多资金账单, 推广中心账单, ERP]
allowed-tools: [Bash, Read, Write]
---

# 拼多多货款对账 (`fin-pdd-bill-reconcile`)

## Workflow
1. 多多工作台 → 资金管理 → 账单 导出
2. 推广中心消耗导出
3. ERP 成交单导出
4. 对账: 回款 = 成交 - 提现手续费 - 平台扣款 - 推广消耗 - 退款
5. 生成报告

## 拼多多特有
- 资金提现手续费
- 先用后付 / 分期订单 账期
- 保证金 / 质保金 核对
- 仅退款 比例高于其他平台需单独分析
