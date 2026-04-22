---
name: ecom-jd-product-publish
description: |
  京东商品发布 SOP: SKU / 属性 / 类目 / 资质 / 详情 / 定价, 保健品需经营许可证 + 蓝帽子。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [京东上架, 京东发布]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# jd-product-publish

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
# Write to ~/.zhongtai/artifacts/ecom-jd-product-publish/YYYYMMDD/
feishu_card "jd-product-publish" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/jd-product-publish/ (v0 spec)
