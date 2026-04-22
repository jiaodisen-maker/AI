---
name: ecom-qianchuan-realtime-optimize
description: |
  千川实时调控。加预算/换素材/关计划, 步长 5%, 日调频次 ≤3。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [千川调控, 千川优化, 实时调千川]
ecom: { domain: 04-paid-ads, role: 运营, frequency: hourly }
---

# qianchuan-realtime-optimize

## Step 1: 基础设施
```bash
source /home/user/AI/.claude/skills/_ecom/lib/browser-setup.sh
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
source /home/user/AI/.claude/skills/_ecom/lib/feishu-push.sh
source /home/user/AI/.claude/skills/_ecom/lib/experience.sh
```

## Step 2: 核心动作
按 description 执行. 登录对应平台后台 → 抓数据/搭计划/改出价/上素材 → 过合规 → 写输出.

## Step 3: 输出 + 飞书
```bash
# Write artifacts + feishu_card
```

## 参考 v0 规范
/home/user/AI/skills/04-paid-ads/qianchuan-realtime-optimize/

## 保健品合规
资质三件套 + 必带「本品不能代替药物」+ 禁明星代言 + 禁医生形象 + 平台类目报白.
