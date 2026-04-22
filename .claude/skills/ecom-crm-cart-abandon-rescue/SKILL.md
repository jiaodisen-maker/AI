---
name: ecom-crm-cart-abandon-rescue
description: |
  弃购召回。T+1h APP push + T+24h 短信 + T+72h 优惠券, 分层给力度。
  Use when 弃购召回 / 购物车召回 / 购物车未付.
allowed-tools: [Bash, Read, Write]
triggers: [弃购召回, 购物车召回, 购物车未付]
ecom: { domain: 07-crm, role: CRM, frequency: hourly }
---

# 弃购召回

## 节奏
- T+1h: APP push「购物车还有 XX 等你」
- T+24h: 短信 + 原价可能变高警示
- T+72h: 专属券 (按客单比例)

## 分层
- 新客: 首单大券
- 老客: 小券 (避免养成刷弃)
- VIP: 营养师电话咨询

## Step 1: 拉弃购列表 (各平台/私域)
## Step 2: 分层匹配券
## Step 3: 多渠道触达
## Step 4: 漏斗回收
