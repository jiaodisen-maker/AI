---
name: ecom-pdd-activity-signup
description: |
  拼多多活动报名: 百亿补贴 / 限时秒杀 / 多多果园 / 领金币。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [拼多多报活动, 百亿补贴 PDD]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# pdd-activity-signup

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
# Write to ~/.zhongtai/artifacts/ecom-pdd-activity-signup/YYYYMMDD/
feishu_card "pdd-activity-signup" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/pdd-activity-signup/ (v0 spec)
