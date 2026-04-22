---
name: ecom-shelf-bundle-config
description: |
  组合装/赠品装/SKU 捆绑配置。主附 SKU 绑定 + 价格策略 + 库存联动。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [组合装, 赠品装, SKU 捆绑]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# shelf-bundle-config

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
# Write to ~/.zhongtai/artifacts/ecom-shelf-bundle-config/YYYYMMDD/
feishu_card "shelf-bundle-config" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/shelf-bundle-config/ (v0 spec)
