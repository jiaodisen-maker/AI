---
name: ecom-shelf-presale-deposit
description: |
  大促预售定金/尾款节奏。定金规则 + 膨胀 + 尾款提醒 + 弃单召回。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [预售, 定金尾款, 大促预售]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: campaign }
---

# shelf-presale-deposit

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
# Write to ~/.zhongtai/artifacts/ecom-shelf-presale-deposit/YYYYMMDD/
feishu_card "shelf-presale-deposit" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/shelf-presale-deposit/ (v0 spec)
