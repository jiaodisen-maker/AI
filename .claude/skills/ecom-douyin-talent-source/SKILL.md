---
name: ecom-douyin-talent-source
description: |
  巨量百应达人筛选。按带货数据/粉丝画像/退款率/口碑分 多维筛选, 分级 S/A/B/C。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [抖音找达人, 百应选号, 抖音 KOL]
ecom: { domain: 02-content-commerce, role: 运营, frequency: on-demand }
---

# douyin-talent-source

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
# Write to ~/.zhongtai/artifacts/ecom-douyin-talent-source/YYYYMMDD/
feishu_card "douyin-talent-source" "$REPORT"
exp_record "ecom-douyin-talent-source" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/02-content-commerce/douyin-talent-source/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
