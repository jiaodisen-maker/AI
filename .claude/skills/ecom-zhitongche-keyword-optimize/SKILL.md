---
name: ecom-zhitongche-keyword-optimize
description: |
  直通车/关键词推广 关键词优化。加词/删词/改匹配/人群溢价最高 +300%。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [直通车优化, 直通车关键词]
ecom: { domain: 04-paid-ads, role: 运营, frequency: daily }
---

# zhitongche-keyword-optimize

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
/home/user/AI/skills/04-paid-ads/zhitongche-keyword-optimize/

## 保健品合规
资质三件套 + 必带「本品不能代替药物」+ 禁明星代言 + 禁医生形象 + 平台类目报白.
