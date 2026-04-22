---
name: ecom-shelf-violation-appeal
description: |
  平台违规申诉单生成。读违规详情 + 举证材料 + LLM 起草申诉书 + 提交。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [违规申诉, 申诉, 平台申诉]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# shelf-violation-appeal

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
# Write to ~/.zhongtai/artifacts/ecom-shelf-violation-appeal/YYYYMMDD/
feishu_card "shelf-violation-appeal" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/shelf-violation-appeal/ (v0 spec)
