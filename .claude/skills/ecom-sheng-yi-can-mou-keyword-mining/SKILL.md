---
name: ecom-sheng-yi-can-mou-keyword-mining
description: |
  生意参谋热搜词/蓝海词挖掘。搜索人气 + 竞争度 + 转化 三维筛。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [参谋关键词, 热搜词, 蓝海词]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: weekly }
---

# sheng-yi-can-mou-keyword-mining

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
# Write to ~/.zhongtai/artifacts/ecom-sheng-yi-can-mou-keyword-mining/YYYYMMDD/
feishu_card "sheng-yi-can-mou-keyword-mining" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/sheng-yi-can-mou-keyword-mining/ (v0 spec)
