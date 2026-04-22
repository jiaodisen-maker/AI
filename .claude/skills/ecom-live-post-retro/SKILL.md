---
name: ecom-live-post-retro
description: |
  直播下播后复盘 (商品/流量/转化/人货场)。UV 价值/坑产/退款率 + 下次动作清单。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [直播复盘, 下播复盘]
ecom: { domain: 05-live-commerce, role: 运营, frequency: per-live-session }
---

# live-post-retro

## Step 1: 基础设施
```bash
source /home/user/AI/.claude/skills/_ecom/lib/browser-setup.sh
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
source /home/user/AI/.claude/skills/_ecom/lib/feishu-push.sh
source /home/user/AI/.claude/skills/_ecom/lib/experience.sh
```

## Step 2: 核心动作
按 description 执行. 登录对应平台后台 → 抓数据/搭计划/改出价/上素材 → 过合规 → 写输出.

## Step 3: 输出 + 飞书
```bash
# Write artifacts + feishu_card
```

## 参考 v0 规范
/home/user/AI/skills/05-live-commerce/live-post-retro/

## 保健品合规
资质三件套 + 必带「本品不能代替药物」+ 禁明星代言 + 禁医生形象 + 平台类目报白.
