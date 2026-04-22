---
name: ecom-ps-category-market-size
description: |
  保健品类目市场容量扫描。跨生意参谋 + 巨量算数 + 蝉妈妈多源数据，
  输出类目 12 月 GMV / 增速 / 竞争集中度 / 头部品牌份额。
  Use when 类目调研 / 市场容量 / 看这个赛道多大.
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [类目调研, 市场容量, 看赛道]
ecom: { domain: 12-product-selection, role: 选品, frequency: monthly }
---

# 类目市场容量

## Step 1: 自动登录多源后台
```bash
source /home/user/AI/.claude/skills/_ecom/lib/browser-setup.sh
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
for P in shengyi-canmou juliang-suanshu chanmama; do
  ensure_login $P && $B cookie-import "$(cred_path $P)"
done
```

## Step 2: 拉类目 12 月 GMV + 增速
生意参谋 市场大盘 / 巨量算数 行业榜 / 蝉妈妈 品类榜。

## Step 3: 头部集中度 CR5 / CR10
前 5/10 品牌份额占比。

## Step 4: 输出报告
artifacts/ecom-ps-category-market-size/YYYYMM/<类目>.md
