---
name: ecom-jd-store-daily-check
description: |
  京麦日检: 京东店铺健康分 / 订单 / 售后 / 违规 / 待办, 生成日报推飞书。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [京东日检, 京麦日检, 京东体检]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: daily }
---

# jd-store-daily-check

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
# Write to ~/.zhongtai/artifacts/ecom-jd-store-daily-check/YYYYMMDD/
feishu_card "jd-store-daily-check" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/jd-store-daily-check/ (v0 spec)
