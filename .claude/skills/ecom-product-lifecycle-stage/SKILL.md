---
name: ecom-product-lifecycle-stage
description: |
  商品生命周期分级: 导入 / 成长 / 成熟 / 衰退, 每阶段匹配运营动作。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [商品生命周期, 周期分级]
ecom: { domain: 06-data-analytics, role: 运营, frequency: monthly }
---

# product-lifecycle-stage



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
Write 到 `~/.zhongtai/artifacts/ecom-product-lifecycle-stage/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "product-lifecycle-stage" "$REPORT"
exp_record "ecom-product-lifecycle-stage" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/product-lifecycle-stage/SKILL.md (v0 spec, 如有)
