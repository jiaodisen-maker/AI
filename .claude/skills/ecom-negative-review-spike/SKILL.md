---
name: ecom-negative-review-spike
description: |
  差评/客诉/退款暴增检测 + topic clustering 识别具体问题 (品质/物流/虚假宣传)。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [差评暴增, 客诉激增, 负面爆发]
ecom: { domain: 06-data-analytics, role: 运营, frequency: hourly }
---

# negative-review-spike



## Step 1: 加载基础设施
```bash
source /home/user/AI/.claude/skills/_ecom/lib/browser-setup.sh
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
source /home/user/AI/.claude/skills/_ecom/lib/feishu-push.sh
source /home/user/AI/.claude/skills/_ecom/lib/experience.sh
```

## Step 2: 执行核心动作
(见 description, 具体做什么)

## Step 3: 输出
Write 到 `~/.zhongtai/artifacts/ecom-negative-review-spike/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "negative-review-spike" "$REPORT"
exp_record "ecom-negative-review-spike" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/negative-review-spike/SKILL.md (v0 spec, 如有)
