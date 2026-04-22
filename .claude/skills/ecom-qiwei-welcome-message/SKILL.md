---
name: ecom-qiwei-welcome-message
description: |
  企微欢迎语 + 健康问卷。营养师人设签名 + 文图+小程序+表单 + 工作日/周末分时段。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [企微欢迎语, 健康问卷]
ecom: { domain: 03-private-domain, role: 运营, frequency: on-demand }
---

# qiwei-welcome-message

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
# Write to ~/.zhongtai/artifacts/ecom-qiwei-welcome-message/YYYYMMDD/
feishu_card "qiwei-welcome-message" "$REPORT"
exp_record "ecom-qiwei-welcome-message" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/03-private-domain/qiwei-welcome-message/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
