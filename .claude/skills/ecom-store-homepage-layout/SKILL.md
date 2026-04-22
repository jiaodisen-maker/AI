---
name: ecom-store-homepage-layout
description: |
  旺铺/店铺首页装修。首页结构 + banner + 楼层 + 商品坑位, 多版本 A/B。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [店铺装修, 首页装修, 旺铺]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# store-homepage-layout

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
# Write to ~/.zhongtai/artifacts/ecom-store-homepage-layout/YYYYMMDD/
feishu_card "store-homepage-layout" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/store-homepage-layout/ (v0 spec)
