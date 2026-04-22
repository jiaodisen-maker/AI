---
name: ecom-cross-platform-activity-calendar
description: |
  大促档期日历生成。全年大促节奏 + 各平台节奏对齐 + 蓄水/预热/爆发/返场时间点。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [大促日历, 活动日历, 大促节奏]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: quarterly }
---

# cross-platform-activity-calendar

## Step 1: 基础设施
```bash
source /home/user/AI/.claude/skills/_ecom/lib/browser-setup.sh
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
source /home/user/AI/.claude/skills/_ecom/lib/feishu-push.sh
```

## Step 2: 核心动作
(按 description 执行; 登录平台后台 → 抓/改/发 → 过合规 → 写输出)

## Step 3: 输出 + 推送
```bash
# Write to ~/.zhongtai/artifacts/ecom-cross-platform-activity-calendar/YYYYMMDD/
feishu_card "cross-platform-activity-calendar" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/cross-platform-activity-calendar/ (v0 spec)
