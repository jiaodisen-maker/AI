---
name: ecom-crm-churn-winback
description: |
  流失召回阶梯。60/90/180 天未购，按等级差异化召回 (营养师电话 / 定制方案 /
  召回券)。漏斗分析 + 退化复盘。Use when 流失召回 / 沉睡激活 / 召回.
allowed-tools: [Bash, Read, Write]
triggers: [流失召回, 沉睡激活, 召回]
ecom: { domain: 07-crm, role: CRM, frequency: monthly }
---

# 流失召回

## 分层
- 60 天未购: 温和提醒 (推新品/补货提醒)
- 90 天: 给券 + 营养师 1v1 关怀
- 180 天: 大额券 + 定制方案 (高价值客) / 低价体验装 (普通客)

## Step 1: 跑 RFM, 定位流失名单
## Step 2: 按客户标签个性化内容
## Step 3: 多触点召回 (短信+企微+电话)
## Step 4: 漏斗: 触达 → 打开 → 点击 → 复购
## Step 5: 失败客户: 标记 "churn" 状态, 暂停触达 6 月以上
