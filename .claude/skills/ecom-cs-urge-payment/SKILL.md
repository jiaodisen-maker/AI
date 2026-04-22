---
name: ecom-cs-urge-payment
description: |
  催付话术。30 分钟 / 2 小时 / 24 小时 三轮催付，用库存/活动/涨价锚点不打扰。
  Use when 催付 / 未付款催单.
allowed-tools: [Bash, Read, Write]
triggers: [催付, 未付款催单]
ecom: { domain: 08-customer-service, role: 客服, frequency: hourly }
---

# 催付

## 三轮节奏
- T+30min: 温和提醒 "您的订单 30 分钟后释放"
- T+2h: 强化 "库存紧张, 活动价即将结束"
- T+24h: 挽回 "最后 XX 小时, 为您保留"

## Step 1: 拉未支付订单
## Step 2: 按下单时长分组
## Step 3: 调旺旺 / 千牛 消息 API / 企微发消息
## Step 4: 支付率回收
