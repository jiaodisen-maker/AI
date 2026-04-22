---
name: ecom-inv-damage-report
description: |
  报损/报溢单。破损/临期报废/退货二次质检不合格 → 生成报损单，走财务入账。
  Use when 报损 / 报溢 / 破损登记.
allowed-tools: [Bash, Read, Write, AskUserQuestion]
triggers: [报损, 报溢, 破损登记]
ecom: { domain: 09-supply-chain, platform: all, role: 仓储, frequency: on-demand }
---

# 报损/报溢

## Step 1: 采集信息
用 AskUserQuestion: SKU, 批号, 数量, 原因 (破损/临期/抽检不合格/盘盈盘亏), 处置方式 (销毁/返厂/捐赠).

## Step 2: 录 ERP
生成报损单号 + 附照片/COA 不合格报告。

## Step 3: 触发财务
```bash
# 写一条通知到 ecom-fin-refund-reconcile 的 "成本调整" 池
```

## Step 4: 保健品特殊
- 必须留存销毁照片 + 视频 (市监局可能查)
- 捐赠不可转销 (禁止降级销售未过期保健品到非授权渠道)
- 临期报废建议提前 30 天以上操作
