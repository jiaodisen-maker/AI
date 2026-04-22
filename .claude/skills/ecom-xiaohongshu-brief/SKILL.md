---
name: ecom-xiaohongshu-brief
description: |
  小红书达人 brief. 核心卖点 + 对标爆文 + 必拍镜头 + 违禁词清单 + 报备流程。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [小红书达人 brief, 小红书 brief]
ecom: { domain: 02-content-commerce, role: 运营, frequency: on-demand }
---

# xiaohongshu-brief

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
# Write to ~/.zhongtai/artifacts/ecom-xiaohongshu-brief/YYYYMMDD/
feishu_card "xiaohongshu-brief" "$REPORT"
exp_record "ecom-xiaohongshu-brief" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/02-content-commerce/xiaohongshu-brief/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
