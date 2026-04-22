---
name: ecom-fin-talent-commission-settle
description: |
  达人佣金月度结算。拉各平台 (百应/淘宝联盟/聚星/蒲公英/视频号互选) 结算单，
  核对 GMV × 佣金率 ± 退款扣减，发票收集，违约条款触发。
  Use when 达人结算 / 佣金结算 / 达人对账.
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [达人结算, 佣金结算, 达人对账]
ecom: { domain: 10-finance, role: 财务, frequency: monthly }
---

# 达人佣金结算

## Step 1: 拉各平台结算单
百应/淘宝联盟/聚星/蒲公英/视频号互选，汇总 CSV。

## Step 2: 对比合同
坑位费 + 佣金率 + 保底 GMV + 退款率上限。

## Step 3: 差异处理
- 超出退款率 → 扣减佣金
- 达人违规（保健品违禁） → 罚则条款触发

## Step 4: 财务打款 + 收票
个人走代征票, 工作室走专票。

## Step 5: 达人信用等级更新
准时供货/按约播/退款率 三维打分，写回达人池。
