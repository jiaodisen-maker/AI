---
name: ecom-qiwei-mass-send
description: |
  企微群发助手 + 敏感词预审。周计划群发 + 标签筛选 + 合规过审 + 监控触达/未读/删友。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [企微群发, 群发助手]
ecom: { domain: 03-private-domain, role: 运营, frequency: weekly }
---

# qiwei-mass-send

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
# Write to ~/.zhongtai/artifacts/ecom-qiwei-mass-send/YYYYMMDD/
feishu_card "qiwei-mass-send" "$REPORT"
exp_record "ecom-qiwei-mass-send" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/03-private-domain/qiwei-mass-send/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
