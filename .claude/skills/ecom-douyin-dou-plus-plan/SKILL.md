---
name: ecom-douyin-dou-plus-plan
description: |
  DOU+ / 小店随心推 加热计划。自然视频起量 + 直播间直投, 预算/人群/出价策略。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [DOU+ 加热, 随心推, 直投]
ecom: { domain: 02-content-commerce, role: 运营, frequency: on-demand }
---

# douyin-dou-plus-plan

## Step 1: 基础设施
```bash
source /home/user/AI/.claude/skills/_ecom/lib/browser-setup.sh
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
source /home/user/AI/.claude/skills/_ecom/lib/feishu-push.sh
source /home/user/AI/.claude/skills/_ecom/lib/experience.sh
```

## Step 2: 核心动作
自主登录对应平台, 执行 description 所述动作. 内容类必过 `scan_forbidden` 违禁词 + `validate_27_function` 蓝帽子校验.

## Step 3: 输出 + 飞书推送
```bash
# Write to ~/.zhongtai/artifacts/ecom-douyin-dou-plus-plan/YYYYMMDD/
feishu_card "douyin-dou-plus-plan" "$REPORT"
exp_record "ecom-douyin-dou-plus-plan" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/02-content-commerce/douyin-dou-plus-plan/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
