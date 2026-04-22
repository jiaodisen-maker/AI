---
name: ecom-pdd-product-publish
description: |
  拼多多商品发布: 类目 / 资质 / 参团 / 秒杀 / 拼购配置。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [拼多多上架, 多多发布]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# pdd-product-publish

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
# Write to ~/.zhongtai/artifacts/ecom-pdd-product-publish/YYYYMMDD/
feishu_card "pdd-product-publish" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/pdd-product-publish/ (v0 spec)
