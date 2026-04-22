---
name: ecom-crm-app-push
description: |
  APP push 推送。标题 ≤10 字, body ≤25 字, 字符限制检查 + 违禁词扫描,
  分群发送, 打开率跟踪。Use when 发 push / APP 推送.
allowed-tools: [Bash, Read, Write]
triggers: [发 push, APP 推送, push 通知]
ecom: { domain: 07-crm, role: CRM, frequency: on-demand }
---

# APP Push

## Step 1: 文案 + 字符检查
标题 ≤10 字, body ≤25 字。

## Step 2: 违禁词
```bash
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
scan_forbidden "$TITLE$BODY"
```

## Step 3: 分群
按 RFM + 标签圈人群。

## Step 4: 调推送平台 (极光 / 个推 / 友盟 / 厂商通道)
行业时段: 早 8-9 / 午 12-13 / 晚 20-21 打开率高。

## Step 5: 回收数据
送达 / 点击 / 卸载率 (过度打扰损害留存)。
