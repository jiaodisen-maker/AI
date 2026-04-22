---
name: ecom-blue-cap-sync
description: 自动从国家市场监管总局特殊食品信息查询平台抓本司所有保健食品（蓝帽子）备案信息。结果写入 ~/.zhongtai/data/products/blue-cap-registry.json, 供所有合规 skill (27项校验/声明一致性/脚本预审) 读取。每周自动增量更新。Use when 同步蓝帽子 / 拉备案 / 蓝帽子备案同步 / blue-cap-sync.
---

# ecom-blue-cap-sync — 蓝帽子备案自动同步

## 数据源

国家市场监督管理总局 特殊食品信息查询平台：
- https://ypzsx.gsxt.gov.cn/specialfood/#/food/mainPage （公开查询页）

字段：批准文号 / 产品名称 / 注册人名称 / 批准日期 / 保健功能声明 / 适宜人群 / 不适宜人群 / 食用方法及食用量 / 规格 / 保质期。

## 工作流

### Step 0: 加载 lib + 守卫

```bash
LIB="$HOME/AI/.claude/skills/ecom-shared/lib"
[ -d "$LIB" ] || LIB="$(git rev-parse --show-toplevel)/.claude/skills/ecom-shared/lib"
source "$LIB/dataroot.sh"
source "$LIB/credentials.sh"
source "$LIB/feishu.sh"
source "$LIB/platform.sh"
zt_init_dirs

COMPANY=$(zt_config_get company_name "")
[ -n "$COMPANY" ] || { echo "公司名未配置, 请先跑 /ecom-bootstrap"; exit 2; }
```

### Step 1: 访问查询页

```bash
_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
B="$_ROOT/.claude/skills/gstack/browse/dist/browse"
[ -x "$B" ] || B="$HOME/.claude/skills/gstack/browse/dist/browse"

$B goto "https://ypzsx.gsxt.gov.cn/specialfood/#/food/mainPage"
$B wait --networkidle
```

### Step 2: 按企业名查询

```bash
# 切到 "保健食品" tab
$B snapshot -i
# 找到 "保健食品" 单选/tab 并点击 (refs 运行时确定)
# $B click @eN

# 填公司名
# $B fill @eN "$COMPANY"
# $B click "查询按钮"
$B wait --networkidle
```

### Step 3: 遍历结果列表

```bash
# 抓第一页所有行
$B js "Array.from(document.querySelectorAll('.result-row')).map(r => ({
  approval: r.querySelector('.approval-no')?.textContent?.trim(),
  name: r.querySelector('.product-name')?.textContent?.trim(),
  company: r.querySelector('.company-name')?.textContent?.trim(),
  detail_url: r.querySelector('a')?.href
}))" > "$(zt_path cache/blue-cap-list.json)"

# 遍历翻页直到尾页
while $B is enabled ".pagination .next"; do
  $B click ".pagination .next"
  $B wait --networkidle
  # append
done
```

### Step 4: 抓每条详情

对每个 `detail_url`：

```bash
$B goto "$url"
$B wait --networkidle
# 抓所有字段到 JSON
$B js '({
  approval: document.querySelector("[data-field=approval]")?.innerText,
  name:     document.querySelector("[data-field=name]")?.innerText,
  registrant: document.querySelector("[data-field=registrant]")?.innerText,
  approve_date: document.querySelector("[data-field=approve_date]")?.innerText,
  functions: document.querySelector("[data-field=functions]")?.innerText,
  suitable: document.querySelector("[data-field=suitable]")?.innerText,
  not_suitable: document.querySelector("[data-field=not_suitable]")?.innerText,
  dosage: document.querySelector("[data-field=dosage]")?.innerText,
  spec: document.querySelector("[data-field=spec]")?.innerText,
  shelf_life: document.querySelector("[data-field=shelf_life]")?.innerText
})'
```

具体选择器需跑一次 `$B snapshot -i` 根据实际 DOM 调整 — 这是正常的，因为政府网站改版不预告。

### Step 5: 功效声明 vs 27 项标准映射

把每条 `functions` 自由文本匹配到标准 27 项之一：

```bash
# 27 项标准清单硬编码
cat > "$(zt_path seed/27-functions.json)" <<'EOF'
[
  "增强免疫力","辅助降血脂","辅助降血糖","抗氧化","辅助改善记忆",
  "缓解视疲劳","促进排铅","清咽","辅助降血压","改善睡眠",
  "促进泌乳","缓解体力疲劳","提高缺氧耐受力","对辐射危害有辅助保护",
  "减肥","改善生长发育","增加骨密度","改善营养性贫血","对化学性肝损伤有辅助保护",
  "祛痤疮","祛黄褐斑","改善皮肤水分","改善皮肤油分","调节肠道菌群",
  "促进消化","通便","对胃黏膜损伤有辅助保护"
]
EOF

# 匹配逻辑（模糊匹配 + LLM 兜底）
python3 <<'PY'
import json, re
std = json.load(open(f"$ZHONGTAI_HOME/seed/27-functions.json"))
# ... 每条备案的 functions 映射到 std[i]
PY
```

### Step 6: 写入 registry

```bash
REG="$(zt_path data/products/blue-cap-registry.json)"
python3 <<'PY'
import json, os
data = {
  "brand": os.environ["ZT_BRAND"],
  "company": os.environ["ZT_COMPANY"],
  "last_synced_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "source": "国家市场监督管理总局特殊食品信息查询平台",
  "products": [
    # 从 Step 4 拉到的每条...
  ]
}
json.dump(data, open("$REG","w"), ensure_ascii=False, indent=2)
PY

echo "✅ 写入 $REG, $(jq '.products|length' $REG) 个 SKU"
```

### Step 7: 变更告警

如果这次同步结果 vs 上次有 diff：
- 新增 SKU → 飞书通知 "发现新备案"
- 批文变更（功效被删减）→ 飞书告警
- 缺失 SKU（过期未续）→ 飞书告警

### Step 8: 登记到每日巡更

写个 cron 提示（不是真 cron，是告诉用户）：
- 建议每周一 9:00 重跑 `/ecom-blue-cap-sync` 同步最新状态
- 或自动：加一行到系统 crontab

## Fallback: 人工上传 CSV

政府网站风控严，自动抓不到时，让用户上传 CSV：

```bash
echo "若自动抓取受阻（验证码/风控），可手动上传 CSV 到 $ZHONGTAI_HOME/seed/blue-cap-manual.csv"
echo "CSV 字段: approval,name,functions,suitable,not_suitable,dosage,spec,approve_date"
```

脚本能识别该 CSV 并转成相同 JSON。

## STATUS

- DONE — 至少抓到 1 条备案，registry.json 有效
- DONE_WITH_CONCERNS — 仅抓到部分（政府网站翻页失败或网络超时）；记录已抓的 + 告警
- BLOCKED — 风控阻塞 / 公司名在备案库里查无
