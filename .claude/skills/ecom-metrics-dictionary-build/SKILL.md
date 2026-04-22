---
name: ecom-metrics-dictionary-build
description: |
  指标字典建设。每个指标含 定义/口径/数据源/责任人, 全公司统一避免歧义。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [指标字典, 指标口径, 定义字典]
ecom: { domain: 06-data-analytics, role: 运营, frequency: quarterly }
---

# metrics-dictionary-build



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
Write 到 `~/.zhongtai/artifacts/ecom-metrics-dictionary-build/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "metrics-dictionary-build" "$REPORT"
exp_record "ecom-metrics-dictionary-build" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/metrics-dictionary-build/SKILL.md (v0 spec, 如有)
