---
name: ecom-tmall-daily-check
description: |
  天猫店铺日常体检。自动登录千牛, 拉取昨日核心数据 (GMV/UV/CVR/订单/退款/差评/违规/待办),
  抓生意参谋流量来源, 扫违规中心, 生成 markdown 日报并推送飞书。完全自动化 —
  只要凭证配好了, 早上 8 点一键跑完。
  Use when user says 做天猫日检 / 千牛日检 / 天猫体检 / 天猫日报 /
  昨天天猫怎么样 / 看看天猫店 / tmall daily check.
---

# 天猫店铺日检（新版 · 使用 ecom-shared 自愈登录）

这是所有 ecom-* skill 的**标杆实现**。其他 222 个 skill 按这个模式迁移到 ecom-shared。

## Step 1: 加载共享库 + 守卫

```bash
LIB="$HOME/AI/.claude/skills/ecom-shared/lib"
[ -d "$LIB" ] || LIB="$(git rev-parse --show-toplevel)/.claude/skills/ecom-shared/lib"
source "$LIB/dataroot.sh"
source "$LIB/credentials.sh"
source "$LIB/feishu.sh"
source "$LIB/platform.sh"
zt_init_dirs

# 冷启动守卫: 未初始化就拒绝运行
if ! zt_is_initialized; then
  echo "中台未初始化, 请先跑 /ecom-bootstrap"
  exit 2
fi

_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
B="$_ROOT/.claude/skills/gstack/browse/dist/browse"
[ -x "$B" ] || B="$HOME/.claude/skills/gstack/browse/dist/browse"
YESTERDAY=$(zt_date_yesterday)
OUTDIR="$(zt_path artifacts/daily)/tmall-${YESTERDAY}"
mkdir -p "$OUTDIR"
```

## Step 2: 自愈登录

```bash
if ! ensure_login tmall; then
  # 返回 1 表示需要人工。用 AskUserQuestion 引导重登。
  # A) 打开浏览器重登 / B) 跳过今日 / C) 降级读缓存
  # A: login_interactive tmall; 成功后 retry ensure_login
  # B: exit 2
  # C: 直接用上次的缓存数据继续 + 飞书告警
  :
fi
```

## Step 3: 拉昨日店铺健康分 + 待办

```bash
$B goto "https://myseller.taobao.com/home.htm"
$B wait --networkidle
$B text > "$OUTDIR/home.txt"
$B screenshot "$OUTDIR/home.png"
```

提取：店铺体验分 / DSR 三项 / 待处理订单 / 待回复咨询 / 违规条数。

## Step 4: 生意参谋昨日概况

```bash
$B goto "https://sycm.taobao.com/portal/home.htm?dateType=day&dateRange=${YESTERDAY}|${YESTERDAY}"
$B wait --networkidle
$B network --clear
$B reload
$B wait --networkidle
$B network --capture > "$OUTDIR/sycm-api.json"
$B screenshot "$OUTDIR/sycm.png"
```

从 `sycm-api.json` 里找：GMV / 支付买家数 / UV / CVR / 客单 / 环比同比。

## Step 5: 流量来源

```bash
$B goto "https://sycm.taobao.com/flow/source?dateRange=${YESTERDAY}|${YESTERDAY}"
$B wait --networkidle
$B network --capture > "$OUTDIR/sycm-source.json"
```

抽取 Top 5 流量来源 + 占比。

## Step 6: 差评

```bash
$B goto "https://rate.tmall.com/list_seller_items.htm?tab=3"
$B wait --networkidle
$B text > "$OUTDIR/bad-reviews.txt"
```

计数昨日差评 + 摘 3 条典型。

## Step 7: 违规中心

```bash
$B goto "https://myseller.taobao.com/violation/list.htm"
$B wait --networkidle
$B text > "$OUTDIR/violations.txt"
```

列出新增违规 + 处罚类型。

## Step 8: 生成日报

Write 到 `$OUTDIR/report.md`：

```markdown
# 天猫店铺日检 · ${YESTERDAY}

**店铺**: $(python3 -c "import json;print(json.load(open('$ZHONGTAI_HOME/config.json'))['shops']['tmall']['shop_name'])")
**体验分**: ...  **DSR**: 描述 X.X / 服务 X.X / 物流 X.X

## 核心指标
| 指标 | 昨日 | 环比 | 同比 |
|------|------|-----|------|
| GMV | $(zt_fmt_gmv X) | ±% | ±% |
| UV | X | ±% | ±% |
...

## 流量来源 TOP5
1. 手淘搜索 40% (GMV $(zt_fmt_gmv Y))
...

## 待办
- [ ] 违规处理 X 条
- [ ] 差评回复 X 条
...

## 差评摘要 (3 条)
1. ...

## 建议动作
- 若 CVR 下滑 > 5% → 跑 /ecom-detail-page-ab-test
- 若 ROI 下滑 > 10% → 跑 /ecom-qianchuan-realtime-optimize
- 若某 SKU 剩余 < 7 天 → 跑 /ecom-inv-stockout-alert
```

## Step 9: 飞书推送

```bash
feishu_send_card default "$OUTDIR/report.md"
```

## Step 10: 归档

```bash
zt_jsonl_append "$(zt_path data/daily-snapshots/tmall.jsonl)" "$(python3 -c "
import json,datetime
print(json.dumps({
  'date':'${YESTERDAY}',
  'gmv': X,'uv': X,'cvr': X,'aov': X,
  'report_path':'$OUTDIR/report.md'
},ensure_ascii=False))")"
zt_log skill-runs "tmall-daily-check ${YESTERDAY} OK"
```

## 降级

| 情况 | 处理 |
|------|------|
| 千牛登录连 3 次失败 | `feishu_alert "tmall 日检" "登录失败, 请手动重登"` + 退出 |
| 生意参谋抓不到 | 用截图代替数据 + 飞书告知「需人工读屏」 |
| 违规中心 API 变 | 回退到 `$B text` + 关键词匹配 |
| 任何 Step 异常 | 记 `zt_log crawls` + 生成 "降级版" 报告 (缺的部分标 N/A) |

## STATUS

- DONE — 所有 Step 走完, report.md 生成, 飞书已推
- DONE_WITH_CONCERNS — 1-2 项数据拉取失败, 但核心 GMV/UV 有; 报告已标注缺项
- BLOCKED — 登录失败且用户拒绝重登 / gstack 未编译
