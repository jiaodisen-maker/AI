---
name: fin-tmall-bill-reconcile
domain: 10-finance
platform: tmall
role: 财务
frequency: monthly
inputs:
  - billing_period
  - store_id
outputs:
  - 对账报告 + 差异明细
human_review_required: true
compliance_filter: false
data_sources:
  - 天猫账期账单
  - 阿里妈妈账单
  - ERP 销售单
allowed-tools: [Bash, Read, Write, WebFetch]
---

# 天猫货款/佣金对账 (`fin-tmall-bill-reconcile`)

## 何时调用
每月账期结束后 3 日内。

## Workflow
1. 从商家中心 → 财务管理 → 账期账单 导出明细 (CSV)
2. 从阿里妈妈导出 直通车/万相台/引力魔方 消耗明细
3. 从 ERP 导出 当月成交订单 + 退款单
4. 三表按订单号/日期对账:
   - 货款 = 成交金额 - 技术服务费 - 营销扣点 - 退款
   - 技术服务费按类目 2-5%
5. 标红差异 > 1 元的条目
6. 生成对账报告 markdown + 财务录入 Excel
7. 推送财务主管复核

## 常见差异
- 平台扣点口径不同 (是否含运费/优惠券补贴)
- 跨期退款未冲减
- 保健品类目扣点档位变动
