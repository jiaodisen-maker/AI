---
name: ecom-ps-competitor-seed
description: 竞品自动发现 + 入库。读本司主营类目, 跨天猫/抖音/京东类目榜单抓 Top 20, 去重后让用户勾选 5-10 个作为追踪对象, 写入 ~/.zhongtai/data/competitors/seed.json。供 ecom-ps-competitor-price-track / newsku-detect / review-mine / copy-mine 等后续竞品 skill 使用。Use when 挖竞品 / 初始化竞品库 / 竞品种子 / competitor seed.
---

# ecom-ps-competitor-seed — 竞品自动发现

## 工作流

### Step 0: lib + 守卫

```bash
LIB="$HOME/AI/.claude/skills/ecom-shared/lib"
[ -d "$LIB" ] || LIB="$(git rev-parse --show-toplevel)/.claude/skills/ecom-shared/lib"
source "$LIB/dataroot.sh"; source "$LIB/credentials.sh"; source "$LIB/feishu.sh"; source "$LIB/platform.sh"
zt_init_dirs

CATEGORY=$(zt_config_get primary_category "")
[ -n "$CATEGORY" ] || { echo "类目未配置, 请跑 /ecom-bootstrap"; exit 2; }

_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
B="$_ROOT/.claude/skills/gstack/browse/dist/browse"
[ -x "$B" ] || B="$HOME/.claude/skills/gstack/browse/dist/browse"
```

### Step 1: 天猫榜单 Top 20

```bash
ensure_login tmall || { echo "需先登天猫"; exit 1; }

# 天猫榜单中心按 "保健食品/$CATEGORY" 筛选
$B goto "https://top.taobao.com/"
# 搜索框输入 $CATEGORY 的标准类目名
# 抓热销榜 Top 20 品牌 + SKU

$B js "Array.from(document.querySelectorAll('.rank-item')).slice(0,20).map(el => ({
  brand: el.querySelector('.brand-name')?.textContent?.trim(),
  sku_title: el.querySelector('.title')?.textContent?.trim(),
  price: el.querySelector('.price')?.textContent?.trim(),
  sales: el.querySelector('.sales')?.textContent?.trim(),
  url: el.querySelector('a')?.href,
  rank: el.querySelector('.rank-num')?.textContent?.trim(),
  source: 'tmall'
}))" > "$(zt_path cache/competitors-tmall.json)"
```

### Step 2: 抖音榜单 (蝉妈妈 / 抖店罗盘)

```bash
ensure_login douyin || echo "抖音未登录, 跳过"

# 抖店罗盘 - 行业排行
$B goto "https://compass.jinritemai.com/shop/industry-rank"
# ... 抓 Top 20
```

### Step 3: 京东榜单

```bash
ensure_login jd || echo "京东未登录, 跳过"
$B goto "https://top.jd.com/"
# 导航到 保健食品 > $CATEGORY
# 抓 Top 20
```

### Step 4: 去重 + 剔除自家品牌

```bash
BRAND=$(zt_config_get brand_cn)

python3 <<PY
import json, os
home = os.environ["ZHONGTAI_HOME"]
all_items = []
for f in ["competitors-tmall", "competitors-douyin", "competitors-jd"]:
  try:
    all_items += json.load(open(f"{home}/cache/{f}.json"))
  except FileNotFoundError: pass

# 按品牌名去重
seen = set()
uniq = []
for it in all_items:
  key = it.get("brand","").strip()
  if not key or key == "$BRAND": continue
  if key in seen: continue
  seen.add(key)
  uniq.append(it)

# 按 SKU 销量排序, 取前 30 作为候选
uniq.sort(key=lambda x: int(''.join(c for c in x.get("sales","0") if c.isdigit()) or 0), reverse=True)
json.dump(uniq[:30], open(f"{home}/cache/competitors-candidates.json","w"), ensure_ascii=False, indent=2)
PY

echo "候选 30 个已写入 cache/competitors-candidates.json"
```

### Step 5: AskUserQuestion 让用户勾选

读 `cache/competitors-candidates.json`，把前 15 个列出来让用户勾选。建议 5-10 个，重点盯：
- 类目头部（绕不过的对手）
- 价位相近（直接抢客户）
- 新晋黑马（GMV 增速最猛）

```markdown
从以下候选中勾选 5-10 个作为追踪竞品。之后 ecom-ps-competitor-price-track /
newsku-detect / copy-mine 都会每日监控这些品牌。

1. [ ] 品牌A - 爆款 SKU X, ¥199, 月销 10 万+
2. [ ] 品牌B - ...
...
```

### Step 6: 写入 seed.json

```bash
python3 <<PY
import json, os
home = os.environ["ZHONGTAI_HOME"]
picks = os.environ["COMPETITOR_PICKS"].split(",")  # 由 AskUserQuestion 结果填入
candidates = json.load(open(f"{home}/cache/competitors-candidates.json"))

seed = {
  "category": "$CATEGORY",
  "brand": "$BRAND",
  "seeded_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "competitors": [c for c in candidates if c["brand"] in picks]
}
json.dump(seed, open(f"{home}/data/competitors/seed.json","w"), ensure_ascii=False, indent=2)
PY
```

### Step 7: 飞书播报

```bash
feishu_send_card default "$(cat <<EOF
# 竞品库初始化完成

**类目**: $CATEGORY
**选定竞品**: $N 个
$(jq -r '.competitors[] | "- \(.brand) (\(.source), \(.price))"' $ZHONGTAI_HOME/data/competitors/seed.json)

后续每日会自动跟踪：
- 价格异动 > 10% → 飞书告警
- 新品上架 → 周报汇总
- 新差评堆积 → 月度复盘

手动增删竞品：编辑 $ZHONGTAI_HOME/data/competitors/seed.json
EOF
)"
```

## 手动增删

用户可以随时：
- 追加竞品 → 重跑本 skill 选 "增量模式"
- 剔除竞品 → 直接编辑 seed.json
- 换类目 → 改 config.json 的 primary_category 再重跑

## STATUS

- DONE — seed.json 有至少 5 个竞品
- DONE_WITH_CONCERNS — 仅抓到部分平台（某平台未登录或风控）；已用可用数据完成
- BLOCKED — 所有平台都未登录 / 用户放弃选择
