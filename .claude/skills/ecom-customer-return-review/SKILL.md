---
name: ecom-customer-return-review
description: |
  老客回访。旺旺 / 京麦消息 / 短信 / 企微 多渠道触达, 回访模板 + 反馈收集。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [老客回访, 老客触达]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: monthly }
---

# customer-return-review

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
# Write to ~/.zhongtai/artifacts/ecom-customer-return-review/YYYYMMDD/
feishu_card "customer-return-review" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/customer-return-review/ (v0 spec)
