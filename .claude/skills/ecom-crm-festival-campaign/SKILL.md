---
name: ecom-crm-festival-campaign
description: |
  节日大促 campaign 规划。春节/618/双11/中秋/重阳 (保健品重点)，包含
  人群分层 + 触达节奏 + 素材 + 落地承接 + 数据看板。Use when 节日营销 /
  大促 campaign / 节日触达.
allowed-tools: [Bash, Read, Write]
triggers: [节日营销, 大促 campaign, 节日触达]
ecom: { domain: 07-crm, role: CRM, frequency: campaign }
---

# 节日大促 Campaign

## Step 1: 节点 + 人群
- 重阳/中秋: 中老年客群主打
- 春节: 年货 + 礼盒
- 618/双11: 全客群

## Step 2: 节奏
T-15 蓄水 → T-7 预热 → T-1 预告 → T 爆发 → T+1 返场

## Step 3: 触达组合
短信 + 企微 + 朋友圈 + APP push + 公众号 + 直播预告 全渠道。

## Step 4: 素材合规
全部过 scan_forbidden + warning-statement-insert。

## Step 5: 作战看板
调 ecom-dual11-warroom-dashboard.
