---
name: fin-douyin-bill-reconcile
domain: 10-finance
platform: douyin
role: 财务
frequency: monthly
inputs: [billing_period, shop_id]
outputs: [对账报告, 差异明细]
human_review_required: true
data_sources: [抖店账单, 巨量千川账单, 巨量百应佣金, ERP]
allowed-tools: [Bash, Read, Write]
---

# 抖音货款/服务费对账 (`fin-douyin-bill-reconcile`)

## Workflow
1. 抖店 → 财务管理 → 账单中心 导出
2. 巨量千川消耗导出
3. 巨量百应达人佣金结算单导出
4. ERP 成交单 + 退款 导出
5. 对账: 回款 = 支付金额 - 技术服务费 (5-10%) - 达人佣金 - 千川消耗 - 退款 - 平台违规扣款
6. 生成报告 + 推送财务

## 抖音特有
- 技术服务费按类目差异 (保健食品 10%)
- 达人佣金 T+15 结算
- 千川账户充值与消耗分账户核对
- 退店退款周期长 (T+30-60)
