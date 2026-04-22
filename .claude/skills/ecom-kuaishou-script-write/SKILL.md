---
name: ecom-kuaishou-script-write
description: |
  快手故事化口播脚本。强情绪开头 + 老铁称呼 + 见证型证据 + 价格锚点 + 平价实用风格。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [快手脚本, 快手短视频, 快手话术]
ecom: { domain: 02-content-commerce, role: 运营, frequency: on-demand }
---

# kuaishou-script-write

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
# Write to ~/.zhongtai/artifacts/ecom-kuaishou-script-write/YYYYMMDD/
feishu_card "kuaishou-script-write" "$REPORT"
exp_record "ecom-kuaishou-script-write" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/02-content-commerce/kuaishou-script-write/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
