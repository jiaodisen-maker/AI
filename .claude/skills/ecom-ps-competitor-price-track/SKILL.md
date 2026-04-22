---
name: ecom-ps-competitor-price-track
description: |
  竞品价格日追踪。每日 9:00 扫竞品 SKU 当前价/划线价/券后价/活动价,
  异动 > 10% 飞书告警。Use when 竞品价格 / 跟价 / 比价.
allowed-tools: [Bash, Read, Write]
triggers: [竞品价格, 跟价, 比价]
ecom: { domain: 12-product-selection, role: 选品, frequency: daily }
---

# 竞品价格追踪

## Step 1: 读竞品 SKU 清单
~/.zhongtai/competitors.csv (品牌/SKU/各平台链接)

## Step 2: 逐平台抓价
```bash
source /home/user/AI/.claude/skills/_ecom/lib/browser-setup.sh
for URL in $COMPETITOR_URLS; do
  $B goto "$URL"
  $B wait --networkidle
  $B js "document.querySelector('.price').innerText"
done
```

## Step 3: 对比昨日快照
~/.zhongtai/competitor-prices/latest.json

## Step 4: 异动告警
涨幅 > 10% → 飞书 + 触发 ecom-shelf-sku-price-adjust 评估跟价。
