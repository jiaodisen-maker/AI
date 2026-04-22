---
name: ecom-keyword-performance
description: |
  关键词表现: 排名 / 搜索热度 / 点击 / 转化 / 蓝海词 + 优化建议。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [关键词表现, 关键词分析]
ecom: { domain: 06-data-analytics, role: 运营, frequency: weekly }
---

# keyword-performance



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
Write 到 `~/.zhongtai/artifacts/ecom-keyword-performance/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "keyword-performance" "$REPORT"
exp_record "ecom-keyword-performance" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/keyword-performance/SKILL.md (v0 spec, 如有)
