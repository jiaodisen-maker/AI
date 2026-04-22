---
name: ecom-pdd-store-daily-check
description: |
  拼多多多多工作台日检: 健康分 / 订单 / 售后 / 仅退款率 / 违规。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [拼多多日检, 多多日检, 拼多多体检]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: daily }
---

# pdd-store-daily-check

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
# Write to ~/.zhongtai/artifacts/ecom-pdd-store-daily-check/YYYYMMDD/
feishu_card "pdd-store-daily-check" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/pdd-store-daily-check/ (v0 spec)
