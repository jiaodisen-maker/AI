---
name: ecom-shipinghao-private-publish
description: |
  视频号私域内容发布。选时段 + 封面 + 话题/位置 + 扩展链接小程序商城 + 私信分流。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [视频号私域, 视频号发布]
ecom: { domain: 03-private-domain, role: 运营, frequency: on-demand }
---

# shipinghao-private-publish

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
# Write to ~/.zhongtai/artifacts/ecom-shipinghao-private-publish/YYYYMMDD/
feishu_card "shipinghao-private-publish" "$REPORT"
exp_record "ecom-shipinghao-private-publish" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/03-private-domain/shipinghao-private-publish/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
