---
name: ecom-shelf-sku-price-adjust
description: |
  跨平台价格调整。读内部价格策略 + 比价竞品 + 平台比价规则 + 合规比价, 批量改各平台价。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [改价格, 全网调价, 跨平台调价]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# shelf-sku-price-adjust

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
# Write to ~/.zhongtai/artifacts/ecom-shelf-sku-price-adjust/YYYYMMDD/
feishu_card "shelf-sku-price-adjust" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/shelf-sku-price-adjust/ (v0 spec)
