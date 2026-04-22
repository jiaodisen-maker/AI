---
name: ecom-douyin-topic-mining
description: |
  抖音选题挖掘。巨量算数 + 蝉妈妈 行业热词 × 爆款拆解 (完播>5s, 点赞率>3%) 筛选。
allowed-tools: [Bash, Read, Write, WebFetch, AskUserQuestion]
triggers: [抖音选题, 抖音爆款拆解]
ecom: { domain: 02-content-commerce, role: 运营, frequency: weekly }
---

# douyin-topic-mining

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
# Write to ~/.zhongtai/artifacts/ecom-douyin-topic-mining/YYYYMMDD/
feishu_card "douyin-topic-mining" "$REPORT"
exp_record "ecom-douyin-topic-mining" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/02-content-commerce/douyin-topic-mining/ (v0 spec)

## 合规红线
保健品行业: 所有内容必带「本品不能代替药物治疗疾病」+ 蓝帽子 logo. 禁疗效词/极限词/明星代言/医生形象.
