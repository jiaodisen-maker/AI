---
name: ecom-kuaishou-shop-publish
description: |
  快手小店商品上架 + 分销广场。类目资质 (保健品需蓝帽子) + 分销佣金 + 橱窗排序。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [快手小店上架, 快手分销]
ecom: { domain: 02-content-commerce, role: 运营, frequency: on-demand }
---

# kuaishou-shop-publish

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
# Write to ~/.zhongtai/artifacts/ecom-kuaishou-shop-publish/YYYYMMDD/
feishu_card "kuaishou-shop-publish" "$REPORT"
exp_record "ecom-kuaishou-shop-publish" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/02-content-commerce/kuaishou-shop-publish/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
