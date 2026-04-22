---
name: ecom-cs-complaint-classify
description: |
  客诉分类 + 响应 + 升级路由。品质 / 物流 / 虚假宣传 / 其他 四大类,
  虚假宣传类立即升级法务。Use when 客诉分类 / 投诉处理.
allowed-tools: [Bash, Read, Write]
triggers: [客诉分类, 投诉处理]
ecom: { domain: 08-customer-service, role: 客服, frequency: daily }
---

# 客诉分类

## 四类
1. 品质: 异物/变质/过敏 → 品控部 + 留档
2. 物流: 丢件/破损 → 物流部 + 快递商
3. 虚假宣传: 立即升级法务 + 合规 + CEO
4. 其他: 客服主管处理

## Step 1: 拉所有新客诉
## Step 2: LLM 分类 + 置信度
## Step 3: 路由对应处理人
## Step 4: 闭环跟踪 + SLA (虚假宣传 2h 响应)
