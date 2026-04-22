---
name: ecom-tmall-product-optimize
description: |
  天猫商品标题/主图/详情页优化。关键词埋点 + A/B 测试主图 + 详情页首屏卖点重排。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [商品优化, 天猫优化, 主图优化]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# tmall-product-optimize

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
# Write to ~/.zhongtai/artifacts/ecom-tmall-product-optimize/YYYYMMDD/
feishu_card "tmall-product-optimize" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/tmall-product-optimize/ (v0 spec)
