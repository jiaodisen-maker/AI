---
name: ecom-taobao-product-publish
description: |
  淘宝商品发布 SOP。登录千牛 → 类目选择 → 属性填写 → 主图/详情/SKU/定价 → 上架 → 保健品资质挂。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [淘宝上架, 淘宝发布, 淘宝商品发布]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# taobao-product-publish

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
# Write to ~/.zhongtai/artifacts/ecom-taobao-product-publish/YYYYMMDD/
feishu_card "taobao-product-publish" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/taobao-product-publish/ (v0 spec)
