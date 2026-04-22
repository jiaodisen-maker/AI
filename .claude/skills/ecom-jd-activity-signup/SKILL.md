---
name: ecom-jd-activity-signup
description: |
  京东活动报名: 京东秒杀 / 京超 / 京东健康 全部报名。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [京东报活动, 京东秒杀报名]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# jd-activity-signup

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
# Write to ~/.zhongtai/artifacts/ecom-jd-activity-signup/YYYYMMDD/
feishu_card "jd-activity-signup" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/jd-activity-signup/ (v0 spec)
