---
name: ecom-crm-birthday-journey
description: |
  生日 journey 自动化。T-7 短信提醒 + T 日礼券 + T+3 复购推送，通过 MA 旅程
  画布上线。Use when 生日营销 / 生日礼 / 生日 journey.
allowed-tools: [Bash, Read, Write]
triggers: [生日营销, 生日礼, 生日 journey]
ecom: { domain: 07-crm, role: CRM, frequency: daily-auto }
---

# 生日 journey

## 节奏
- T-7: 短信/push「XX 好消息」+ 礼券预告
- T-0: 企微 / 短信 / APP push 祝福 + 生日礼券 + 生日专属组合
- T+3: 提醒用券 + 复购

## 礼物设计
- 等级权益: 银: 5 元券 / 金: 10 元券 / 钻: 免邮+样品 / 黑: 手写卡+礼盒

## Step 1: 每日扫当日/7天后生日用户
```python
# CDP 查: birthday = today OR today+7
```

## Step 2: 按等级匹配礼物
## Step 3: 多通道触达 (短信+企微+push)
## Step 4: 数据回收 (打开/用券/复购)
