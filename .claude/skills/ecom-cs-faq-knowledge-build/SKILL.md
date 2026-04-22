---
name: ecom-cs-faq-knowledge-build
description: |
  FAQ 话术库建设。抽客服高频问题 + 标准答案 + 合规口径 + 版本管理。
  Use when FAQ 建设 / 话术库 / 客服知识库.
allowed-tools: [Bash, Read, Write]
triggers: [FAQ 建设, 话术库, 客服知识库]
ecom: { domain: 08-customer-service, role: 客服, frequency: monthly }
---

# FAQ 话术库

## Step 1: 聚合近月客服对话
各平台客服聊天导出.

## Step 2: LLM 抽高频问题
cluster + 频次排序.

## Step 3: 标准答案起草
合规过 + 品牌声音一致.

## Step 4: 版本管理
`~/.zhongtai/faq/` 下 markdown + 版本号 + 变更记录.

## Step 5: 同步到智能客服 (机器人意图)
调 ecom-cs-bot-intent-train.
