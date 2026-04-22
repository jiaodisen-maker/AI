---
name: skill-name-in-kebab
domain: NN-domain-folder
platform: all | tmall | jd | pdd | douyin | kuaishou | xiaohongshu | shipinghao | wechat
role: 运营 | 内容 | 投手 | 客服 | 数据 | 财务 | 合规 | 选品
frequency: on-demand | hourly | daily | weekly | monthly | campaign
inputs:
  - 字段名: 说明
outputs:
  - 输出文件/报表/动作
human_review_required: false
compliance_filter: false
data_sources:
  - 平台后台/API/ERP
allowed-tools:
  - Bash
  - Read
  - Write
  - WebFetch
---

# 中文标题 (`skill-name-in-kebab`)

## 何时调用
<业务场景, 例如: "每日早上 9 点, 运营想看昨日店铺表现"; 或 "临近大促, 需要把所有未报名的活动补报">

## 输入
- **字段名** (必填/选填) — 类型 — 说明

## 输出
- **输出 1** — 格式 — 内容示例
- **输出 2**

## Workflow
1. 步骤 1 — 具体动作 (点 XX / 导 XX / 调 XX)
2. 步骤 2
3. 步骤 3
4. 审批/复核环节 (如适用)

## 合规要点 (content/customer-service/live 类必填)
- 违禁词扫描: [forbidden-word-scan](../../11-compliance/forbidden-word-scan/SKILL.md)
- 蓝帽子 27 项功能校验: [27-function-validator](../../11-compliance/27-function-validator/SKILL.md)

## 数据来源
- 平台后台: XX
- 第三方数据: XX (蝉妈妈/飞瓜/千瓜)
- 内部系统: XX (ERP / CDP / CRM)

## 经验沉淀 hooks
- 每次 diff(ai_output, human_edited) → 提取 pattern 入 `experience_store/<skill-name>`
- 聚合置信度 ≥ 0.7 的 pattern → 注入下次调用的 system prompt

## 失败/降级
- 平台接口失败 → 回退到上次缓存 + 人工提醒
- 合规词命中 → block 输出, 要求人工改写
