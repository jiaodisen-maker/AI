---
name: ecom-ps-competitor-newsku-detect
description: |
  竞品新品检测。每周扫竞品店铺新上架 SKU + 搜索热度突起词。
  Use when 竞品新品 / 新品监控 / 竞品动向.
allowed-tools: [Bash, Read, Write]
triggers: [竞品新品, 新品监控, 竞品动向]
ecom: { domain: 12-product-selection, role: 选品, frequency: weekly }
---

# 竞品新品检测

## Step 1: 扫竞品店铺近 7 天上架
各平台店铺 API 或 gstack 抓上新时间戳。

## Step 2: 搜索热度突起词
对比本周 vs 上周搜索指数 (生意参谋/巨量算数)，找新突起。

## Step 3: 输出 + 建议
新品名单 + 估价 + 预估市场切入策略。
