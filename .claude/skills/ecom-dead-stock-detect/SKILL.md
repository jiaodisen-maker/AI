---
name: ecom-dead-stock-detect
description: |
  滞销品识别: 动销率 < 阈值, 库存周转 > N 天, 给清仓处置建议。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [滞销识别, 死库存, 动销差]
ecom: { domain: 06-data-analytics, role: 运营, frequency: weekly }
---

# dead-stock-detect



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
Write 到 `~/.zhongtai/artifacts/ecom-dead-stock-detect/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "dead-stock-detect" "$REPORT"
exp_record "ecom-dead-stock-detect" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/dead-stock-detect/SKILL.md (v0 spec, 如有)
