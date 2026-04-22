---
name: ecom-inv-fefo-pick-rule
description: |
  保健品 FEFO 先效先出拣货规则配置/验证。检查 ERP/WMS 是否按批次效期排序
  拣货，近效期批次必须先发货。Use when 配 FEFO / 拣货规则 / 先效先出.
allowed-tools: [Bash, Read, Write]
triggers: [FEFO, 先效先出, 拣货规则]
ecom: { domain: 09-supply-chain, platform: all, role: 库存, frequency: on-demand }
---

# FEFO 先效先出拣货规则

## Step 1: 读当前拣货规则
查 WMS/ERP 配置，当前是按 FIFO（先进先出）还是 FEFO（先效先出）。保健品必须 FEFO。

## Step 2: 随机抽单核对
抽 10 单最近发货，对比发出的批次 vs 仓库里最早效期批次，应一致。

## Step 3: 异常处置
发现被发出的不是最早效期 → 登记异常 → 联系 WMS 供应商调规则。
