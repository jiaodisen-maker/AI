---
name: fin-vat-invoice-collect
domain: 10-finance
platform: all
role: 财务
frequency: monthly
inputs: [supplier_list / campaign_list]
outputs: [进项发票清单 + 缺失清单]
human_review_required: true
data_sources: [供应商合同, 平台账单, 达人合作, 物流/仓储, 广告账户]
allowed-tools: [Bash, Read, Write]
---

# 进项发票收集归档 (`fin-vat-invoice-collect`)

## Workflow
1. 清点本月需收票的支出:
   - 供应商 (采购原材料/成品)
   - 平台服务费 (技术服务费/佣金)
   - 达人佣金 (个人→代征票 / 工作室→专票)
   - 物流仓储
   - 广告平台消耗
   - 办公 / 差旅
2. 追票: 主动发催票邮件 / 企微 / 电话
3. 收到后录入财务系统 (认证/抵扣)
4. 归档 PDF + 原件
5. 月末出"缺票清单" → 影响利润表

## 风险点
- 达人个人票: 代征收据需与合同一致
- 跨境支付: 境外发票 (Invoice) 需做 形式发票 + 付汇凭证
- 电商平台: 先充值后消耗的广告费, 发票按充值出，消耗与发票时间不对应
