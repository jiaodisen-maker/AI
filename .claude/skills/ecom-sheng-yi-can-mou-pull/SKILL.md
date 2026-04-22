---
name: ecom-sheng-yi-can-mou-pull
description: |
  生意参谋数据拉取 + 清洗。全量拉 + 字段标准化 + 入数据仓库。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [生意参谋, 拉数据参谋, 参谋数据]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: daily }
---

# sheng-yi-can-mou-pull

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
# Write to ~/.zhongtai/artifacts/ecom-sheng-yi-can-mou-pull/YYYYMMDD/
feishu_card "sheng-yi-can-mou-pull" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/sheng-yi-can-mou-pull/ (v0 spec)
