---
name: ecom-sku-portfolio-abc
description: |
  SKU ABC 分析: 按 GMV 贡献 + 毛利贡献 分 ABCD 档, 运营精力分配建议。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [ABC 分析, SKU 分级, ABCD 档]
ecom: { domain: 06-data-analytics, role: 运营, frequency: quarterly }
---

# sku-portfolio-abc



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
Write 到 `~/.zhongtai/artifacts/ecom-sku-portfolio-abc/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "sku-portfolio-abc" "$REPORT"
exp_record "ecom-sku-portfolio-abc" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/sku-portfolio-abc/SKILL.md (v0 spec, 如有)
