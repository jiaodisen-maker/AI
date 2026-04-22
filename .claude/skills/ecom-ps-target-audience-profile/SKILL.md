---
name: ecom-ps-target-audience-profile
description: |
  目标人群画像。从订单 + 评价 + 客服 + 问卷 抽取 (年龄/性别/地域/消费力/
  痛点/场景/购买动机)。Use when 画像 / 目标人群 / 用户洞察.
allowed-tools: [Bash, Read, Write]
triggers: [画像, 目标人群, 用户洞察]
ecom: { domain: 12-product-selection, role: 选品, frequency: quarterly }
---

# 目标人群画像

## Step 1: 多源数据
订单 + 评价 + 客服聊天 + 问卷 + 千川 DMP。

## Step 2: LLM 语义分类
痛点 / 场景 / 购买动机 的高频词 + cluster.

## Step 3: 输出画像卡
姓名/年龄/职业/家庭/痛点/信息来源/决策链/客单范围。
可视化: persona.md + 头像图（可选调 AI 画图）。
