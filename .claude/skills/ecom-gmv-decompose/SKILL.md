---
name: ecom-gmv-decompose
description: |
  GMV 5 层驱动树拆解。流量×点击率×CVR×客单价×复购率逐层归因, 找出最大贡献因子和最大下跌因子。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [GMV 拆解, 驱动树, GMV 归因]
ecom: { domain: 06-data-analytics, role: 运营, frequency: weekly }
---

# gmv-decompose



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
Write 到 `~/.zhongtai/artifacts/ecom-gmv-decompose/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "gmv-decompose" "$REPORT"
exp_record "ecom-gmv-decompose" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/gmv-decompose/SKILL.md (v0 spec, 如有)
