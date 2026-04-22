---
name: ecom-inv-batch-expiry-track
description: |
  保健品批次效期追踪。每日扫 ERP 全部库存批次，算每批到期剩余天数，按 90/60/30
  天三档告警，到期 90 天内自动触发促销建议（打折/赠品/直播清仓），到期 30 天内
  强制下架。Use when 扫效期 / 临期预警 / 批次到期检查 / 效期管理.
allowed-tools: [Bash, Read, Write]
triggers: [临期预警, 扫效期, 批次到期, 效期管理]
ecom: { domain: 09-supply-chain, platform: all, role: 库存, frequency: daily }
---

# 保健品批次效期追踪

## Step 1: 拉所有批次
```bash
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
source "$(cred_path erp env)"
# 从 ERP API 拉批次库存 (或读本地 CSV ~/.zhongtai/inventory/batches.csv)
```

## Step 2: 计算到期剩余天数 + 三档分类
```bash
python3 <<'PY'
import csv, datetime, json
today = datetime.date.today()
buckets = {"30d": [], "60d": [], "90d": [], "safe": []}
with open("/path/to/batches.csv") as f:
  for r in csv.DictReader(f):
    expire = datetime.date.fromisoformat(r["expiry_date"])
    days = (expire - today).days
    if days < 30: buckets["30d"].append(r)
    elif days < 60: buckets["60d"].append(r)
    elif days < 90: buckets["90d"].append(r)
    else: buckets["safe"].append(r)
print(json.dumps({k: v for k,v in buckets.items() if k != "safe"}, ensure_ascii=False))
PY
```

## Step 3: 处置建议
- **< 30 天**: 强制下架各平台 SKU + 报损申请
- **30-60 天**: 降价清仓 + 直播特惠 + 客户赠品
- **60-90 天**: 前置提醒 + 市场部加大推广

## Step 4: 推送飞书
```bash
source /home/user/AI/.claude/skills/_ecom/lib/feishu-push.sh
feishu_card "临期预警" "$REPORT"
```

## 保健品注意
- FEFO 规则: 先效先出 (非 FIFO)
- 到期前 7 天若未处置 → 升级飞书给供应链负责人 + 老板
