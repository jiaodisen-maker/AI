---
name: ecom-qiwei-离职-handover
description: |
  离职员工客户/群继承。后台批量分配 + 24h 客户确认追踪 + 数据交接看板。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [企微离职继承, 离职交接]
ecom: { domain: 03-private-domain, role: 运营, frequency: on-demand }
---

# qiwei-离职-handover

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
# Write to ~/.zhongtai/artifacts/ecom-qiwei-离职-handover/YYYYMMDD/
feishu_card "qiwei-离职-handover" "$REPORT"
exp_record "ecom-qiwei-离职-handover" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/03-private-domain/qiwei-离职-handover/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
