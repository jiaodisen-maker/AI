---
name: ecom-tmall-activity-signup
description: |
  天猫活动报名: 聚划算 / 淘抢购 / 百亿补贴 / 欢聚日 全部报名流程。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [天猫报活动, 聚划算报名, 百亿补贴]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# tmall-activity-signup

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
# Write to ~/.zhongtai/artifacts/ecom-tmall-activity-signup/YYYYMMDD/
feishu_card "tmall-activity-signup" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/tmall-activity-signup/ (v0 spec)
