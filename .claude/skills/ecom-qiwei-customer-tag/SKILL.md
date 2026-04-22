---
name: ecom-qiwei-customer-tag
description: |
  企微客户标签体系。症状/年龄段/疾病史/产品偏好/客单价 自动打标 + 阶段维护。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [企微标签, 客户标签, 打标]
ecom: { domain: 03-private-domain, role: 运营, frequency: on-demand }
---

# qiwei-customer-tag

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
# Write to ~/.zhongtai/artifacts/ecom-qiwei-customer-tag/YYYYMMDD/
feishu_card "qiwei-customer-tag" "$REPORT"
exp_record "ecom-qiwei-customer-tag" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/03-private-domain/qiwei-customer-tag/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
