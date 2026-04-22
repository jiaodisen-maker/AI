---
name: ecom-cs-shift-schedule
description: |
  客服排班。基于历史接待量预测 + 大促作战日历 + 夜班/周末。
  Use when 客服排班 / 排班表 / 值班安排.
allowed-tools: [Bash, Read, Write]
triggers: [客服排班, 排班表, 值班安排]
ecom: { domain: 08-customer-service, role: 客服, frequency: weekly }
---

# 客服排班

## Step 1: 历史接待量预测
过去 4 周相同星期的接待量均值.

## Step 2: 大促加权
双 11 / 618 × 3x, 年货节 × 2x.

## Step 3: 算所需人力
目标: 3 分钟响应率 ≥ 95%.
`所需人力 = 预测接待 / (人均每小时处理 × 在线时长)`

## Step 4: 排班表 + 夜班轮换
上午 / 下午 / 夜班 × 工作日 / 周末.

## Step 5: 同步到企微日程
