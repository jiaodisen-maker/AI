---
name: ecom-ps-bluesea-keyword-find
description: |
  蓝海关键词挖掘。搜索热度高 + 竞争度低 + 转化潜力高的词。
  Use when 蓝海词 / 关键词挖掘 / 找新流量入口.
allowed-tools: [Bash, Read, Write]
triggers: [蓝海词, 关键词挖掘, 找新流量]
ecom: { domain: 12-product-selection, role: 选品, frequency: monthly }
---

# 蓝海词挖掘

## Step 1: 拉行业词表
生意参谋搜索词查询 + 5118 热词 + 千瓜关键词。

## Step 2: 三维筛选
- 月搜索 > N
- 竞争度 < X (商品数 / 搜索量)
- 转化 CVR > Y (已有相关商品的平均)

## Step 3: LLM 扩展长尾
核心词 → 搜索意图变体 → 新长尾。

## Step 4: 输出 TOP 50 词 + 匹配产品建议
