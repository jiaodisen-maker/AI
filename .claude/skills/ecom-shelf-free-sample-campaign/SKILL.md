---
name: ecom-shelf-free-sample-campaign
description: |
  试用中心/众测投放。选品 + 数量 + 人群 + 报告收集, 转化为评价。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [试用, 众测, 试用中心]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# shelf-free-sample-campaign

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
# Write to ~/.zhongtai/artifacts/ecom-shelf-free-sample-campaign/YYYYMMDD/
feishu_card "shelf-free-sample-campaign" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/shelf-free-sample-campaign/ (v0 spec)
