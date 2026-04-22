---
name: ecom-cs-bot-intent-train
description: |
  智能客服机器人意图训练。从 FAQ 库生成训练数据, 推上各平台机器人 (飞鸽/快服务/
  阿里客服云), 配兜底话术 + 转人工规则。Use when 训练客服机器人 / 机器人优化.
allowed-tools: [Bash, Read, Write]
triggers: [训练客服机器人, 机器人优化]
ecom: { domain: 08-customer-service, role: 客服, frequency: weekly }
---

# 机器人训练

## Step 1: 从 FAQ 生成训练对
问题变体 × 标准答案.

## Step 2: 合规过筛所有答案
## Step 3: 上传各平台机器人
飞鸽 / 快服务 / 阿里云客服 / 小红书私信机器人.

## Step 4: 配转人工规则
- 保健品"治 XX 病"类问题 → 转人工
- 情绪值 < 阈值 → 转人工
- 金额 > X → 转人工
