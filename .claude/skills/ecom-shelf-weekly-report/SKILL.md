---
name: ecom-shelf-weekly-report
description: |
  货架电商周报自动生成。天猫/京东/拼多多 汇总周度 GMV + TOP 品 + 问题清单。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [货架周报, 电商周报]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: weekly }
---

# shelf-weekly-report

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
# Write to ~/.zhongtai/artifacts/ecom-shelf-weekly-report/YYYYMMDD/
feishu_card "shelf-weekly-report" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/shelf-weekly-report/ (v0 spec)
