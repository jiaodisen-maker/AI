---
name: ecom-inv-stock-dashboard
description: |
  实时库存看板。聚合所有仓 + 所有平台的 可用/在途/锁定/不可售 库存，
  按 SKU 和仓位输出看板，推送飞书。Use when 看库存 / 库存看板 /
  全仓库存.
allowed-tools: [Bash, Read, Write]
triggers: [看库存, 库存看板, 全仓库存]
ecom: { domain: 09-supply-chain, platform: all, role: 库存, frequency: hourly }
---

# 实时库存看板

## Step 1: 拉所有仓数据
从 ERP (旺店通/万里牛/聚水潭) 拉: SKU × 仓位 × {可用, 在途, 锁定, 不可售, 临期}。

## Step 2: 平台端核对
并行拉天猫/京东/抖音/拼多多 各平台库存数 (平台 SKU 映射 ERP SKU)。任何差异 > 5% 标红。

## Step 3: 生成看板
Write markdown 到 `~/.zhongtai/artifacts/ecom-inv-stock-dashboard/<timestamp>.md`：
- 总库存 + 日销 + 周转天数
- Top 20 SKU 明细
- 异常 SKU (差异 / 缺货 / 积压)

## Step 4: 推送飞书 (每 6 小时一次)
```bash
source /home/user/AI/.claude/skills/_ecom/lib/feishu-push.sh
feishu_card "库存看板 $(date +%H:%M)" "$DASHBOARD"
```
