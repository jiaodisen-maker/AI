---
name: ecom-pdd-duoduo-search-ad
description: |
  多多搜索投放 + 质量分。关键词/卡位/点击率/转化率/UV 价值 优化质量分。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [多多搜索, 拼多多搜索广告]
ecom: { domain: 04-paid-ads, role: 运营, frequency: on-demand }
---

# pdd-duoduo-search-ad

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
/home/user/AI/skills/04-paid-ads/pdd-duoduo-search-ad/

## 保健品合规
资质三件套 + 必带「本品不能代替药物」+ 禁明星代言 + 禁医生形象 + 平台类目报白.
