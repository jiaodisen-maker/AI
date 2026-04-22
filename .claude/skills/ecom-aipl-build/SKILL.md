---
name: ecom-aipl-build
description: |
  AIPL 人群资产流转: Awareness→Interest→Purchase→Loyalty 每层规模 + 流入/流出率 + 漏损诊断。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [AIPL, 人群资产, 数据银行]
ecom: { domain: 06-data-analytics, role: 运营, frequency: monthly }
---

# aipl-build



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
Write 到 `~/.zhongtai/artifacts/ecom-aipl-build/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "aipl-build" "$REPORT"
exp_record "ecom-aipl-build" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/aipl-build/SKILL.md (v0 spec, 如有)
