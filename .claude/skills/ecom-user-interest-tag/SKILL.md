---
name: ecom-user-interest-tag
description: |
  用户兴趣/功效/人群标签体系。从订单 + 评价 + 浏览 + 客服咨询 提取兴趣标签,
  同步到 CRM / 企微 / 投放 DMP。Use when 用户标签 / 兴趣标签 / 人群包.
allowed-tools: [Bash, Read, Write]
triggers: [用户标签, 兴趣标签, 人群包]
ecom: { domain: 07-crm, role: CRM, frequency: weekly }
---

# 兴趣标签体系

## 标签类目
- 品类偏好: 胶原/益生菌/维生素/护肝/睡眠
- 功效偏好: 免疫/美容/睡眠/消化/骨骼
- 人群: 中老年/孕产/熬夜党/健身/术后
- 消费能力: 低/中/高
- 行为: 浏览狂/下单狂/评价狂/分享狂

## Step 1: 多源数据整合
订单 / 评价 / 浏览 / 客服咨询 / 问卷。

## Step 2: NLP 抽标签
LLM 做关键词 + 语义分类。

## Step 3: 写回 CDP + 企微 + 千川 DMP
