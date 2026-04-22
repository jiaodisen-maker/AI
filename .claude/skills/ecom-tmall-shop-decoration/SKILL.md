---
name: ecom-tmall-shop-decoration
description: |
  天猫旺铺装修版本管理。大促版 / 日常版 / 节日版 切换 + 时间表。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [天猫装修, 旺铺管理]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# tmall-shop-decoration

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
# Write to ~/.zhongtai/artifacts/ecom-tmall-shop-decoration/YYYYMMDD/
feishu_card "tmall-shop-decoration" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/tmall-shop-decoration/ (v0 spec)
