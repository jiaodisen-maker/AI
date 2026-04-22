---
name: ecom-xiaohongshu-cover-3-4
description: |
  小红书 3:4 封面 brief。大标题 + 利益点 + 高对比 + 6-9 张种草图方向。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [小红书封面, 3:4 封面]
ecom: { domain: 02-content-commerce, role: 运营, frequency: on-demand }
---

# xiaohongshu-cover-3-4

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
# Write to ~/.zhongtai/artifacts/ecom-xiaohongshu-cover-3-4/YYYYMMDD/
feishu_card "xiaohongshu-cover-3-4" "$REPORT"
exp_record "ecom-xiaohongshu-cover-3-4" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/02-content-commerce/xiaohongshu-cover-3-4/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
