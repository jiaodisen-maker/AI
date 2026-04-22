---
name: ecom-shelf-coupon-plan
description: |
  优惠券/满减方案。按客群 + SKU + 活动 设计券策略 + 领取门槛 + 使用条件 + 成本测算。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [券策略, 优惠券, 满减方案]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# shelf-coupon-plan

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
# Write to ~/.zhongtai/artifacts/ecom-shelf-coupon-plan/YYYYMMDD/
feishu_card "shelf-coupon-plan" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/shelf-coupon-plan/ (v0 spec)
