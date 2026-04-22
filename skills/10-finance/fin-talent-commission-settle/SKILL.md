---
name: fin-talent-commission-settle
domain: 10-finance
platform: all
role: 财务
frequency: monthly
inputs: [billing_period]
outputs: [佣金结算单 + 发票收集清单]
human_review_required: true
data_sources: [巨量百应, 淘宝联盟, 磁力聚星, 蒲公英, 视频号互选, 合作合同]
allowed-tools: [Bash, Read, Write]
---

# 达人佣金结算 (`fin-talent-commission-settle`)

## Workflow
1. 拉各平台达人结算单 (百应/淘宝联盟/聚星/蒲公英/视频号互选)
2. 核对 GMV × 佣金率 ± 退款扣减
3. 核对合同约定: 坑位费 + 佣金 + 保底 GMV + 退款率上限
4. 差异项列出 → 与达人/MCN 核对
5. 财务打款 + 收集对方发票 (个人工作室→代征/专票)
6. 达人信用等级更新 (准时供货/按约播出/退款率)

## 风险点
- 虚假交易 / 刷单 → 仅退款率飙升 → 扣减结算
- 合同外费用 (临时加价) → 必须补合同
- 保健品达人违规带货 → 罚则条款触发
