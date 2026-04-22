---
name: ecom-roi-drop-alarm
description: |
  ROI 异常下跌根因自动定位: 定向/出价/创意/落地页/供应 五维逐层排除。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [ROI 下跌, ROI 告警, ROI 异常]
ecom: { domain: 06-data-analytics, role: 运营, frequency: hourly }
---

# roi-drop-alarm



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
Write 到 `~/.zhongtai/artifacts/ecom-roi-drop-alarm/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "roi-drop-alarm" "$REPORT"
exp_record "ecom-roi-drop-alarm" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/roi-drop-alarm/SKILL.md (v0 spec, 如有)
