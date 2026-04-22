---
name: ecom-inv-purchase-order
description: |
  采购单生成 + 供应商确认。从补货计划生成正式 PO，走审批流程，发给供应商，
  跟踪回执。Use when 下采购单 / 发 PO / 采购单生成.
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [下采购单, 发 PO, 采购单]
ecom: { domain: 09-supply-chain, platform: all, role: 采购, frequency: on-demand }
---

# 采购单

## Step 1: 读补货计划 CSV
```bash
LATEST_PO=$(ls -t ~/.zhongtai/purchase-orders/*.csv | head -1)
```

## Step 2: 按供应商拆单
多个 SKU 可能来自不同供应商 → 拆成独立 PO。

## Step 3: 生成 PDF PO (ReportLab / pandoc)
包含: PO 号, 下单日, 供应商, SKU 明细, 数量, 单价, 总价, 付款条件, 交货地址, 质检要求 (保健品: COA 随货)。

## Step 4: 发邮件/企微给供应商
```bash
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
# 用 SMTP 或企微 API 发
```

## Step 5: 跟踪回执 (D+1, D+3, D+7)
无回执 → 飞书升级采购主管。
