---
name: ecom-douyin-talent-brief
description: |
  抖音达人合作 brief。卖点 TOP3 + 违禁词清单 + 必带话术 + 口播脚本骨架 + 挂车链接 + 佣金/坑位费。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [抖音达人 brief, 达人合作 brief]
ecom: { domain: 02-content-commerce, role: 运营, frequency: on-demand }
---

# douyin-talent-brief

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
# Write to ~/.zhongtai/artifacts/ecom-douyin-talent-brief/YYYYMMDD/
feishu_card "douyin-talent-brief" "$REPORT"
exp_record "ecom-douyin-talent-brief" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/02-content-commerce/douyin-talent-brief/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
