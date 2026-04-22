---
name: ecom-douyin-sample-send
description: |
  抖音寄样流程 + 快递单号跟踪。百应寄样 → 录单号 → 签收追踪 → 送达后 D+3 提醒催视频。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [寄样, 发样品, 寄样跟踪]
ecom: { domain: 02-content-commerce, role: 运营, frequency: on-demand }
---

# douyin-sample-send

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
# Write to ~/.zhongtai/artifacts/ecom-douyin-sample-send/YYYYMMDD/
feishu_card "douyin-sample-send" "$REPORT"
exp_record "ecom-douyin-sample-send" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/02-content-commerce/douyin-sample-send/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
