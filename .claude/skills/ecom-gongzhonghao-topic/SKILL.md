---
name: ecom-gongzhonghao-topic
description: |
  公众号选题。后台搜一搜关键词 + 微信指数/5118 热词 + 竞品爆文 + 输出痛点/热点/沉淀三栏选题清单。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [公众号选题, 选题策划]
ecom: { domain: 03-private-domain, role: 运营, frequency: weekly }
---

# gongzhonghao-topic

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
# Write to ~/.zhongtai/artifacts/ecom-gongzhonghao-topic/YYYYMMDD/
feishu_card "gongzhonghao-topic" "$REPORT"
exp_record "ecom-gongzhonghao-topic" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/03-private-domain/gongzhonghao-topic/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
