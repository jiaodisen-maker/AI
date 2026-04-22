---
name: ecom-live-replay-clip
description: |
  直播切片二剪 + DOU+ 投流. 3-15 秒爆款片段 + Demo 片段 + 催单片段, 挂小黄车发矩阵号。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [直播切片, 直播二剪]
ecom: { domain: 05-live-commerce, role: 运营, frequency: post-live }
---

# live-replay-clip

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
/home/user/AI/skills/05-live-commerce/live-replay-clip/

## 保健品合规
资质三件套 + 必带「本品不能代替药物」+ 禁明星代言 + 禁医生形象 + 平台类目报白.
