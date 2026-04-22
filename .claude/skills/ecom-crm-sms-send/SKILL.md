---
name: ecom-crm-sms-send
description: |
  短信批量发送。阿里云/腾讯云短信 API，必带「退订」+ 违禁词预审，
  发送速率控制，结果回收。Use when 发短信 / 批量短信 / 短信召回.
allowed-tools: [Bash, Read, Write]
triggers: [发短信, 批量短信, 短信召回]
ecom: { domain: 07-crm, role: CRM, frequency: on-demand }
---

# 短信发送

## Step 1: 过合规
```bash
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
scan_forbidden "$SMS_TEMPLATE"
```

## Step 2: 必带 "回T退订"
保健品短信必备 (《短信息服务管理规定》)。

## Step 3: 分批调 API
阿里云 dysmsapi / 腾讯云 SMS。每批 1000, 速率控制。

## Step 4: 回收送达率 + 点击率
链接加 UTM。

## Step 5: 沉淀经验
开花率最高的模板 / 发送时段 / 人群。
