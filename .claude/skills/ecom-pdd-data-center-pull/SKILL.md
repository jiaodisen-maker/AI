---
name: ecom-pdd-data-center-pull
description: |
  拼多多数据中心拉取。全量拉 + 清洗入仓。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [拼多多数据中心, 多多数据]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: daily }
---

# pdd-data-center-pull

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
# Write to ~/.zhongtai/artifacts/ecom-pdd-data-center-pull/YYYYMMDD/
feishu_card "pdd-data-center-pull" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/pdd-data-center-pull/ (v0 spec)
