---
name: ecom-shelf-ip-dispute
description: |
  知识产权投诉/维权。对抄袭/盗图/恶意差评提诉讼, 证据链生成。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [知识产权, IP 维权, 盗图投诉]
ecom: { domain: 01-shelf-commerce, role: 运营, frequency: on-demand }
---

# shelf-ip-dispute

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
# Write to ~/.zhongtai/artifacts/ecom-shelf-ip-dispute/YYYYMMDD/
feishu_card "shelf-ip-dispute" "$REPORT"
```

## 参考规范
/home/user/AI/skills/01-shelf-commerce/shelf-ip-dispute/ (v0 spec)
