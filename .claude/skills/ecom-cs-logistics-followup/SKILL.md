---
name: ecom-cs-logistics-followup
description: |
  物流催收/异常件处理。扫已发货但 > 3 天无揽收, 或滞留, 或破损, 自动给客户
  推送 + 催快递。Use when 物流催收 / 物流异常.
allowed-tools: [Bash, Read, Write]
triggers: [物流催收, 物流异常, 查快递]
ecom: { domain: 08-customer-service, role: 客服, frequency: hourly }
---

# 物流催收

## Step 1: 拉所有已发货订单 + 物流节点
## Step 2: 异常判定
- 无揽收 > 24h
- 滞留 > 48h
- 破损/丢失

## Step 3: 两线操作
- 对客户: 自动道歉 + 实时进度更新 + 补偿券
- 对快递: 提工单 / 电话催

## Step 4: 补偿策略
小额 5-10 元券 / 免邮 / 补发.
