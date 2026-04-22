---
name: ecom-cs-return-exchange-flow
description: |
  退换货流程处理。原因核实 / 地址 / 运费判定 / 退款金额 / 入库复查。
  保健品拆封过开封不予退换规则特别留意。Use when 退换货 / 退货 / 换货.
allowed-tools: [Bash, Read, Write]
triggers: [退换货, 退货, 换货]
ecom: { domain: 08-customer-service, role: 客服, frequency: daily }
---

# 退换货

## Step 1: 核实原因
品质 / 描述不符 / 不喜欢 / 过敏

## Step 2: 运费判定
- 商家原因: 商家承担
- 客户原因: 客户承担 + 运费险

## Step 3: 保健品特殊
- 已拆封/过开封: 原则不退 (食品安全), 除非质量问题
- 过敏反馈: 必须退 + 留档 (合规证据)

## Step 4: 退货到仓 → 二次质检
合格入库 / 不合格报损 (调 ecom-inv-damage-report)
