---
name: ecom-bootstrap
description: 保健品 AI 中台冷启动向导。首次使用前跑一次，配好所有平台登录 cookie、店铺档案、品牌档案、飞书 webhook、ERP 类型、蓝帽子备案库、竞品清单。跑完后所有 ecom-* skill 都能自动找数据和操作，不再需要手工配置。Use when user says 初始化中台 / 冷启动 / 第一次用 / ecom-bootstrap / 配置中台 / setup zhongtai.
---

# ecom-bootstrap — 中台冷启动向导

## 目标

把"从零到所有 skill 都能自主跑"的全部配置在 20-40 分钟内一次做完。跑完这个 skill 后：

- `~/.zhongtai/credentials/platforms/*.json` — 8 个平台的登录 cookie
- `~/.zhongtai/config.json` — 飞书 webhook / ERP 类型 / 品牌档案
- `~/.zhongtai/data/products/*.json` — 本司所有 SKU + 蓝帽子备案
- `~/.zhongtai/data/competitors/seed.json` — 初始竞品清单
- `~/.zhongtai/.initialized` — 初始化完成标记

之后所有 ecom-* skill 开头的 `zt_is_initialized` 检查都会通过。

## 前置要求

- gstack browse 已编译（`~/.claude/skills/gstack/browse/dist/browse` 存在）
  - 若无，先跑 `cd ~/.claude/skills/gstack && ./setup`
- 用户能在电脑上登录各平台后台（扫码或密码）
- 知道品牌名、飞书机器人 webhook URL

## 工作流

### Step 0: 加载共享库 + 建目录

```bash
LIB="$HOME/AI/.claude/skills/ecom-shared/lib"
[ -d "$LIB" ] || LIB="$(git rev-parse --show-toplevel)/.claude/skills/ecom-shared/lib"
source "$LIB/dataroot.sh"
source "$LIB/credentials.sh"
source "$LIB/feishu.sh"
source "$LIB/platform.sh"
zt_init_dirs

echo "==> 中台根目录: $ZHONGTAI_HOME"
ls -la "$ZHONGTAI_HOME"
```

### Step 1: 采集品牌基础信息

AskUserQuestion 依次问用户：

1. **品牌中文名** — 写入 `config.json → brand_cn`
2. **品牌英文名** — 写入 `config.json → brand_en`
3. **主营类目** — 维生素 / 蛋白粉 / 鱼油 / 益生菌 / 胶原蛋白 / 护肝 / 睡眠 / 骨健康 / 其他
4. **公司名（蓝帽子备案归属）** — 用于抓备案
5. **ERP 系统** — 旺店通 / 万里牛 / 聚水潭 / 管家婆 / 其他 / 无
6. **主要经营平台**（多选）— tmall / jd / pdd / douyin / kuaishou / xiaohongshu / shipinghao / qiwei

存入 `~/.zhongtai/config.json`：

```bash
zt_config_set brand_cn "$BRAND_CN"
zt_config_set brand_en "$BRAND_EN"
zt_config_set primary_category "$CATEGORY"
zt_config_set company_name "$COMPANY"
zt_config_set erp_system "$ERP"
# active_platforms 数组特殊处理
python3 -c "import json,sys
f='$ZHONGTAI_HOME/config.json'
d=json.load(open(f))
d['active_platforms']=sys.argv[1].split(',')
json.dump(d,open(f,'w'),ensure_ascii=False,indent=2)" "$PLATFORMS_CSV"
```

### Step 2: 配飞书 webhook

AskUserQuestion：
- **日常推送 webhook**（日报/周报群）
- **告警 webhook**（缺货/合规/ROI 告警群，可与上同）

存入：
```bash
zt_config_set feishu_webhook "$HOOK1"
zt_config_set feishu_alert_webhook "$HOOK2"
# 发测试消息
feishu_send_text default "【中台初始化测试】欢迎使用 $(zt_config_get brand_cn) 保健品 AI 中台 — $(date +%Y-%m-%d)"
feishu_send_text alert "【告警通道测试】此通道将用于缺货/合规/ROI 异常告警"
```

失败则返回 Step 2 让用户重填。

### Step 3: 逐平台登录

对 `active_platforms` 中每个平台，依次：

```bash
for platform in $(python3 -c "import json;print(' '.join(json.load(open('$ZHONGTAI_HOME/config.json'))['active_platforms']))"); do
  cfg=$(zt_platform_config "$platform")
  display=$(echo "$cfg" | grep ^display_name= | cut -d= -f2-)
  login_url=$(echo "$cfg" | grep ^login_url= | cut -d= -f2-)
  echo "==> 准备登录: $display ($platform)"
  echo "    登录地址: $login_url"
done
```

对每个平台：
1. AskUserQuestion：「即将打开真浏览器引导你登录 {display_name}，扫码或输入密码。准备好了吗？」
   - A) 开始登录
   - B) 跳过此平台（稍后再来）
   - C) 放弃 bootstrap
2. 如果 A → `login_interactive <platform>`:
   - `$B connect` 打开真浏览器
   - `$B goto <login_url>`
   - `$B handoff "请在浏览器里扫码/登录 $display。完成后敲回车继续。"`
   - AskUserQuestion：「登录完成了吗？」
     - A) 完成，继续下一平台
     - B) 失败，重试
   - 完成后：`$B cookies > $(zt_cred_file $platform)`
   - 自动跳 `verify_login <platform>` 验证（访问 home_url 检查 selector）
   - 成功 → feishu_send_text default "✅ $platform 登录态已保存"
   - 失败 → 回到 handoff 重试
3. 全部完成后：`$B disconnect` 返回 headless 模式

### Step 4: 采集店铺元数据

对每个已登录的平台，登录后台抓店铺 ID + 店铺名：

```bash
# tmall 例 (其他平台类似)
ensure_login tmall
$B goto "https://myseller.taobao.com/home.htm"
SHOP_ID=$($B js "document.querySelector('meta[name=shop-id]')?.content || ''")
SHOP_NAME=$($B js "document.querySelector('.shop-name')?.textContent?.trim() || ''")
python3 -c "import json
f='$ZHONGTAI_HOME/config.json'
d=json.load(open(f))
d.setdefault('shops',{})['$platform']={'shop_id':'$SHOP_ID','shop_name':'$SHOP_NAME'}
json.dump(d,open(f,'w'),ensure_ascii=False,indent=2)"
```

### Step 5: 蓝帽子备案同步（关键）

调用 `ecom-blue-cap-sync`（也可以手动跑）自动抓本司所有保健品备案：

```bash
# 这一步委托给子 skill
echo "==> 触发 ecom-blue-cap-sync 同步备案..."
```

注意：ecom-blue-cap-sync 会写 `~/.zhongtai/data/products/blue-cap-registry.json`，里面是所有 SKU × 批准文号 × 功效声明 × 人群 × 规格。之后所有合规 skill（27 项校验、声明一致性、脚本预审）都从这里读。

### Step 6: 竞品种子

调用 `ecom-ps-competitor-seed`：

```bash
echo "==> 触发 ecom-ps-competitor-seed 抓竞品..."
```

读 `primary_category` → 进天猫/抖音/京东三大类目榜单 Top 20 → 去重 → 问用户勾选 5-10 个作为追踪对象 → 写 `~/.zhongtai/data/competitors/seed.json`。

### Step 7: ERP 初始化（如配置了）

如果 ERP 不是「无」：

```bash
# 例: 旺店通
case "$(zt_config_get erp_system)" in
  旺店通)
    AskUserQuestion：「请把旺店通 API 的 app_key / sid / app_secret 填上（写到本地 ~/.zhongtai/credentials/erp-wangdiantong.json）」
    ;;
  万里牛) ... ;;
  聚水潭) ... ;;
  无) 跳过 ;;
esac
```

API 凭证测试一次（拉当天订单 1 条），确认 OK 即写入。

### Step 8: 验证 & 标记完成

```bash
# 逐项确认
for p in $(python3 -c "import json;print(' '.join(json.load(open('$ZHONGTAI_HOME/config.json'))['active_platforms']))"); do
  if verify_login "$p"; then echo "✅ $p"; else echo "❌ $p"; fi
done

# 飞书报送
feishu_send_card default "$(cat <<EOF
# 中台初始化完成 ✅

**品牌**：$(zt_config_get brand_cn)
**类目**：$(zt_config_get primary_category)
**平台**：$(python3 -c "import json;print(', '.join(json.load(open('$ZHONGTAI_HOME/config.json'))['active_platforms']))")
**ERP**：$(zt_config_get erp_system)
**SKU 数**：$(jq '.products|length' $ZHONGTAI_HOME/data/products/blue-cap-registry.json 2>/dev/null || echo 0)
**竞品数**：$(jq '.competitors|length' $ZHONGTAI_HOME/data/competitors/seed.json 2>/dev/null || echo 0)

之后所有 ecom-* skill 都可一键运行。
EOF
)"

zt_mark_initialized
echo "STATUS: DONE"
```

### Step 9: 使用引导

告诉用户可以跑的常用 skill：
- `/ecom-tmall-daily-check` — 天猫日检，最常用
- `/ecom-daily-report-generate` — 全平台日报
- `/ecom-inv-stockout-alert` — 缺货预警
- `/ecom-forbidden-word-scan` — 违禁词扫描
- 等等...

## 重入 / 修改

重跑 bootstrap 不会破坏已有数据；已初始化则问用户要修改哪部分：

- 重登某个平台
- 修改飞书 webhook
- 同步蓝帽子备案
- 重新选竞品

## 错误处理

- 登录失败 3 次：跳过此平台，标记 `inactive`，不阻塞其他平台
- 飞书 webhook 无效：警告但允许继续（日后用 `zt_config_set` 修）
- 蓝帽子抓取失败：允许用户上传 CSV 人工导入

## STATUS

- DONE — 所有必要组件就绪，`.initialized` 已写
- DONE_WITH_CONCERNS — 部分平台未登录 / 部分 seed 未抓；已记录到 `logs/bootstrap-skipped.log`
- BLOCKED — gstack browse 未编译 或 用户取消
