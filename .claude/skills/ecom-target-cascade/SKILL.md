---
name: ecom-target-cascade
description: |
  目标逐层分解。年目标 → 店铺 → 类目 → SKU → 日, 每级独立可追踪可归责。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [目标分解, 拆目标, 逐级下压]
ecom: { domain: 06-data-analytics, role: 运营, frequency: quarterly }
---

# target-cascade



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
Write 到 `~/.zhongtai/artifacts/ecom-target-cascade/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "target-cascade" "$REPORT"
exp_record "ecom-target-cascade" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/target-cascade/SKILL.md (v0 spec, 如有)
