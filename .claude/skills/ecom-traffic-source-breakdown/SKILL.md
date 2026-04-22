---
name: ecom-traffic-source-breakdown
description: |
  流量来源结构: 手淘搜索/推荐/猜你喜欢/购物车/付费/直播 的占比 + 环比 + 贡献 GMV。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [流量来源, 流量结构]
ecom: { domain: 06-data-analytics, role: 运营, frequency: weekly }
---

# traffic-source-breakdown



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
Write 到 `~/.zhongtai/artifacts/ecom-traffic-source-breakdown/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "traffic-source-breakdown" "$REPORT"
exp_record "ecom-traffic-source-breakdown" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/traffic-source-breakdown/SKILL.md (v0 spec, 如有)
