---
name: ecom-baidu-ocpc-plan
description: |
  百度 oCPC / 搜索 / 信息流。百青藤信息流 + 品专 + 基木鱼落地页 + 商盾反作弊。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [百度投放, 百度 oCPC, 百度信息流]
ecom: { domain: 04-paid-ads, role: 运营, frequency: on-demand }
---

# baidu-ocpc-plan

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
/home/user/AI/skills/04-paid-ads/baidu-ocpc-plan/

## 保健品合规
资质三件套 + 必带「本品不能代替药物」+ 禁明星代言 + 禁医生形象 + 平台类目报白.
