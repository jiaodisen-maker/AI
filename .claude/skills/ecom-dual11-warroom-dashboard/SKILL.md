---
name: ecom-dual11-warroom-dashboard
description: |
  大促作战看板: 实时 GMV pacing + 缺货 + ROAS + 客服负荷 + 直播场均。双11/618/年货节。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [大促作战看板, 战报, 大促看板]
ecom: { domain: 06-data-analytics, role: 运营, frequency: campaign }
---

# dual11-warroom-dashboard



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
Write 到 `~/.zhongtai/artifacts/ecom-dual11-warroom-dashboard/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "dual11-warroom-dashboard" "$REPORT"
exp_record "ecom-dual11-warroom-dashboard" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/dual11-warroom-dashboard/SKILL.md (v0 spec, 如有)
