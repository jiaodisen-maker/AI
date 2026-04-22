---
name: ecom-live-console-data-monitor
description: |
  直播大屏监控 (在线/UV/GMV/转化/停留/互动)。巨量百应 + 抖店罗盘 + 磁力金牛经营中枢。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [直播大屏, 直播数据, 实时监控]
ecom: { domain: 05-live-commerce, role: 运营, frequency: per-live-session }
---

# live-console-data-monitor

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
/home/user/AI/skills/05-live-commerce/live-console-data-monitor/

## 保健品合规
资质三件套 + 必带「本品不能代替药物」+ 禁明星代言 + 禁医生形象 + 平台类目报白.
