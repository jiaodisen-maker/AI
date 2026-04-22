---
name: ecom-detail-page-ab-test
description: |
  详情页 A/B 测试。首屏/卖点顺序/CTA/价格 多版本测试 + 统计显著性。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [详情页 AB, 详情页测试]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# detail-page-ab-test

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
# Write to ~/.zhongtai/artifacts/ecom-detail-page-ab-test/YYYYMMDD/
feishu_card "detail-page-ab-test" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/detail-page-ab-test/ (v0 spec)
