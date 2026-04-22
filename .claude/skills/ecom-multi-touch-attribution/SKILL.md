---
name: ecom-multi-touch-attribution
description: |
  多触点归因对比: last-touch vs linear vs U-shape vs 时间衰减 四种模型并列出结果供决策。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [多触点归因, U-shape 归因, 时间衰减]
ecom: { domain: 06-data-analytics, role: 运营, frequency: monthly }
---

# multi-touch-attribution



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
Write 到 `~/.zhongtai/artifacts/ecom-multi-touch-attribution/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "multi-touch-attribution" "$REPORT"
exp_record "ecom-multi-touch-attribution" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/multi-touch-attribution/SKILL.md (v0 spec, 如有)
