---
name: ecom-wanxiangtai-plan-build
description: |
  万相台无界版计划搭建。7 大场景 (关键词推广/精准人群/货品/店铺/消费者/活动/内容) + 7 大资源位。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [万相台计划, 万相台搭建]
ecom: { domain: 04-paid-ads, role: 运营, frequency: on-demand }
---

# wanxiangtai-plan-build

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
/home/user/AI/skills/04-paid-ads/wanxiangtai-plan-build/

## 保健品合规
资质三件套 + 必带「本品不能代替药物」+ 禁明星代言 + 禁医生形象 + 平台类目报白.
