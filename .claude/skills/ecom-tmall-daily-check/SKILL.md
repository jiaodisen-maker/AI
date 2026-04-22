---
name: ecom-tmall-daily-check
description: |
  天猫店铺日常体检。自动登录千牛，拉取昨日核心数据（GMV/UV/CVR/订单/退款/
  差评/违规/待办），抓生意参谋流量来源，扫违规中心，生成 markdown 日报并
  推送飞书。完全自动化 — 只要凭证配好了，早上 8 点一键跑完。
  Use when user says 做天猫日检 / 千牛日检 / 天猫体检 / 天猫日报 /
  昨天天猫怎么样 / 看看天猫店 / tmall daily check.
allowed-tools:
  - Bash
  - Read
  - Write
  - WebFetch
  - AskUserQuestion
triggers:
  - 做天猫日检
  - 千牛日检
  - 天猫店铺体检
  - 天猫日报
  - 昨天天猫怎么样
ecom:
  domain: 01-shelf-commerce
  platform: tmall
  role: 店铺运营
  frequency: daily
  human_review_required: false
  compliance_filter: false
  data_sources: [千牛, 生意参谋]
---

# 天猫店铺日检

你会帮老板/运营每天早上做天猫店铺的体检。这件事完全 hands-off — 从登录到输出都你来做。

## Step 1: 加载共用基础设施

```bash
source /home/user/AI/.claude/skills/_ecom/lib/browser-setup.sh   # 导出 $B
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh     # cred_*
source /home/user/AI/.claude/skills/_ecom/lib/experience.sh      # exp_record
source /home/user/AI/.claude/skills/_ecom/lib/feishu-push.sh     # feishu_card
```

## Step 2: 检查千牛登录态

```bash
ensure_login tmall
```

**若输出 `NEEDS_LOGIN: tmall`**：
1. 用 `AskUserQuestion` 问："千牛没有登录态。要不要现在打开浏览器登一次？(gstack 会从你电脑的 Comet/Chrome 导入)"
2. 若用户同意 → 执行：
   ```bash
   $B cookie-import-browser comet --domain .taobao.com
   $B cookie-import-browser comet --domain .tmall.com
   $B cookie-import-browser comet --domain .aliyun.com
   # 导出到 credentials
   $B cookies > "$(cred_path tmall)"
   ```
3. 再跑 `verify_login tmall https://myseller.taobao.com/home.htm ".nav-user-name"` 确认

**若输出 `STALE`**：cookies 过期，走上面同样的重登录流程。

## Step 3: 拉昨日店铺健康分 + 待办

```bash
YESTERDAY=$(date -d 'yesterday' +%Y-%m-%d 2>/dev/null || date -v-1d +%Y-%m-%d)
$B goto "https://myseller.taobao.com/home.htm"
$B wait --networkidle
# 抓首页健康分 + 待办卡片
$B text > /tmp/tmall-home-${YESTERDAY}.txt
$B screenshot "/tmp/tmall-home-${YESTERDAY}.png"
```

用 Read 读 `/tmp/tmall-home-${YESTERDAY}.txt`，提取：
- 店铺体验分
- DSR (描述/服务/物流)
- 待处理订单数
- 待回复咨询数
- 违规条数

## Step 4: 拉生意参谋昨日概况

```bash
$B goto "https://sycm.taobao.com/portal/home.htm?dateType=day&dateRange=${YESTERDAY}|${YESTERDAY}"
$B wait --networkidle
$B network --clear
$B reload
$B wait --networkidle
# 用新版 gstack v1.6+ 的 network --capture 抓 JSON 响应
$B network --capture > /tmp/sycm-api-${YESTERDAY}.json
$B screenshot /tmp/sycm-home-${YESTERDAY}.png
```

Read `/tmp/sycm-api-${YESTERDAY}.json`，在 API 响应里找:
- 支付金额 (GMV)
- 支付买家数
- 访客数 UV
- 支付转化率
- 客单价
- 环比/同比

## Step 5: 拉流量来源结构

```bash
$B goto "https://sycm.taobao.com/flow/source?dateRange=${YESTERDAY}|${YESTERDAY}"
$B wait --networkidle
$B network --capture > /tmp/sycm-source-${YESTERDAY}.json
```

提取 Top 流量来源（手淘搜索/手淘推荐/购物车/直通车/万相台/直播…）+ 占比。

## Step 6: 拉差评 + 客诉

```bash
$B goto "https://rate.tmall.com/list_seller_items.htm?tab=3"
$B wait --networkidle
$B text > /tmp/tmall-bad-reviews-${YESTERDAY}.txt
```

计数昨日差评条数 + 摘 3 条典型差评内容。

## Step 7: 扫违规中心

```bash
$B goto "https://myseller.taobao.com/violation/list.htm"
$B wait --networkidle
$B text > /tmp/tmall-violation-${YESTERDAY}.txt
```

列出昨日新增违规 + 处罚类型（警告/扣分/下架/封店）。

## Step 8: 生成日检报告

用 Write 工具生成 markdown 到 `~/.zhongtai/artifacts/ecom-tmall-daily-check/${YESTERDAY}/report.md`：

```markdown
# 天猫店铺日检 · YYYY-MM-DD

**店铺**: <store-name>
**体验分**: X.X  (vs 前日 ±)
**DSR**: 描述 X.X / 服务 X.X / 物流 X.X

## 核心指标
| 指标 | 昨日 | 环比 | 同比 |
|------|------|-----|------|
| GMV | ¥X | ±% | ±% |
| UV | X | ±% | ±% |
| CVR | X% | | |
| 客单 | ¥X | | |

## 流量来源 TOP5
...

## 待办
- [ ] 违规处理 X 条
- [ ] 差评回复 X 条
- [ ] 客诉处理 X 单
- [ ] 待发货 X 单

## 昨日差评摘要 (3 条典型)
1. ...
2. ...

## 建议动作
基于异常指标自动给出 1-3 条行动建议（如 ROI 下滑建议查千川、CVR 下滑建议查详情页 A/B）。
```

## Step 9: 推送飞书

```bash
REPORT=$(cat "$HOME/.zhongtai/artifacts/ecom-tmall-daily-check/${YESTERDAY}/report.md")
feishu_card "天猫日检 · ${YESTERDAY}" "$REPORT"
```

## Step 10: 经验沉淀

```bash
exp_record "ecom-tmall-daily-check" '"date":"'${YESTERDAY}'","report_path":"'$HOME'/.zhongtai/artifacts/ecom-tmall-daily-check/'${YESTERDAY}'/report.md"'
```

## 失败 / 降级
- 千牛登录失败 2 次 → 飞书告警 + 停止后续步骤
- 生意参谋抓不到数据 → 用 `$B screenshot` 截图替代，标注「需人工读屏」
- 违规中心接口变了 → 回退到 `text` 全文搜索关键词「违规 / 处罚」

## 巡逻调度
可被 cron 每天 08:30 自动触发。建议配置:
```
30 8 * * 1-7 cd /home/user/AI && claude --skill ecom-tmall-daily-check --non-interactive
```

## 注意
- 不要在下单高峰 (14:00 / 20:00) 跑，避免挤占带宽
- 首次跑需要 2-3 分钟（登录 + 多次 goto + wait networkidle）
- 后续跑约 1-2 分钟
