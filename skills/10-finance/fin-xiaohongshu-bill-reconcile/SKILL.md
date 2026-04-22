---
name: fin-xiaohongshu-bill-reconcile
domain: 10-finance
platform: xiaohongshu
role: 财务
frequency: monthly
inputs: [billing_period, store_id]
outputs: [对账报告]
human_review_required: true
data_sources: [千帆账单, 聚光消耗, 蒲公英佣金, ERP]
allowed-tools: [Bash, Read, Write]
---

# 小红书货款/综合服务费对账 (`fin-xiaohongshu-bill-reconcile`)

## Workflow
1. 千帆 → 财务 → 账单导出
2. 聚光/蒲公英消耗导出
3. ERP 成交单导出
4. 对账: 回款 = 成交 - 综合服务费 (5-10%) - 聚光消耗 - 蒲公英结算 - 退款
5. 保健品品类特别关注: 类目综合扣点

## 小红书特有
- 综合服务费按类目档位
- 蒲公英 T+N 结算，需另设达人佣金明细表
- 跨平台商品同价校验
