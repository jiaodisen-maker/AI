---
name: ecom-cs-bad-review-handle
description: |
  差评应对。24h 内公开回复 (真诚道歉 + 解决方案) + 私信召回 (补偿 + 改评引导)。
  Use when 差评处理 / 差评回复 / 改评.
allowed-tools: [Bash, Read, Write]
triggers: [差评处理, 差评回复, 改评]
ecom: { domain: 08-customer-service, role: 客服, frequency: daily }
---

# 差评应对

## Step 1: 扫所有新差评
各平台评价 API.

## Step 2: 分类
品质 / 物流 / 客服 / 价格 / 其他

## Step 3: 公开回复 (24h 内)
真诚道歉 + 针对性解决方案, 不推诿。

## Step 4: 私信召回
提供补偿 (券/样品/退差价) + 改评请求。

## Step 5: 根因归档
差评根因按类目汇总 → 周报给运营/品控。
