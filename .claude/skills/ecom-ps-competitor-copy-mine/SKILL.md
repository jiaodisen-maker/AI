---
name: ecom-ps-competitor-copy-mine
description: |
  竞品文案挖掘。抓竞品详情页 / 直播话术 / 短视频口播, LLM 拆解
  痛点 / 卖点 / 话术结构, 输出差异化建议。Use when 竞品文案 / 文案挖掘.
allowed-tools: [Bash, Read, Write]
triggers: [竞品文案, 文案挖掘]
ecom: { domain: 12-product-selection, role: 选品, frequency: monthly }
---

# 竞品文案挖掘

## Step 1: 抓取
- 详情页 (gstack $B html)
- 直播话术 (飞瓜/蝉妈妈切片)
- 短视频口播 (ASR)

## Step 2: LLM 拆解
高频词 / 痛点结构 / Hook 模式 / 催单话术。

## Step 3: 差异化建议
竞品没说的 / 说错的 / 说得太多可以反其道而行。
