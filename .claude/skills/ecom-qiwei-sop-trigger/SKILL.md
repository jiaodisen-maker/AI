---
name: ecom-qiwei-sop-trigger
description: |
  企业微信新客 SOP 自动触达。扫 24 小时内新加好友的客户，按 D1/D3/D7/D15
  节奏触发对应 SOP 动作（健康问卷/科普文章/首单券/复购提醒），通过企微 API
  自动发消息 + 朋友圈。触达前过广告法合规，记录每次触达的打开/回复/转化。
  Use when user says 跑企微 SOP / 今天的 SOP 触达 / 新客 SOP /
  D3 触达 / 企微自动发消息 / qiwei-sop.
allowed-tools:
  - Bash
  - Read
  - Write
  - WebFetch
  - AskUserQuestion
triggers:
  - 跑企微 SOP
  - 新客 SOP
  - 今天的 SOP 触达
  - D3 触达
  - 企微自动发消息
ecom:
  domain: 03-private-domain
  platform: wechat-work
  role: 私域运营
  frequency: daily
  human_review_required: false
  compliance_filter: true
  data_sources: [企业微信 API, 本地 SCRM 客户表]
---

# 企业微信新客 SOP 自动触达

你负责每天给私域新客按节奏发营养师 1v1 消息 + 内容。

## Step 1: 加载基础设施

```bash
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
source /home/user/AI/.claude/skills/_ecom/lib/experience.sh
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
source /home/user/AI/.claude/skills/_ecom/lib/feishu-push.sh
```

## Step 2: 读企微 API token

```bash
cred_exists wechat-work || {
  echo "NEEDS_LOGIN: wechat-work"
  # AskUserQuestion: 「企微 API token 没配置, 要现在配吗？」
  # 用户同意 → 引导: 管理后台→应用→企业应用→自建→获取 corpid+secret
  # 保存到 ~/.zhongtai/credentials/wechat-work.env
}
source "$(cred_path wechat-work env)"  # 加载 CORPID / SECRET / AGENTID
```

## Step 3: 拿 access_token

```bash
ACCESS_TOKEN=$(curl -s "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=${CORPID}&corpsecret=${SECRET}" | jq -r '.access_token')
[ -z "$ACCESS_TOKEN" ] || [ "$ACCESS_TOKEN" = "null" ] && {
  echo "TOKEN_FAIL"; exit 1
}
```

## Step 4: 拉"应触达"客户名单

客户数据来源两种:
- (a) 如果有本地 SCRM CSV: `~/.zhongtai/scrm/customers.csv` (字段: external_userid, add_date, tag, stage, last_touch)
- (b) 否则用企微 API 拉外部联系人列表

读 CSV 计算每个人的天数 delta:
```bash
TODAY=$(date +%Y-%m-%d)
python3 <<PY
import csv, datetime, json
today = datetime.date.fromisoformat("$TODAY")
triggers = {"D1": [], "D3": [], "D7": [], "D15": [], "D30": []}
with open("$HOME/.zhongtai/scrm/customers.csv") as f:
    for row in csv.DictReader(f):
        d = (today - datetime.date.fromisoformat(row["add_date"])).days
        key = f"D{d}" if d in (1,3,7,15,30) else None
        if key: triggers[key].append(row["external_userid"])
print(json.dumps(triggers, ensure_ascii=False))
PY
```

## Step 5: 为每个节点准备内容 + 合规过

| 节点 | 动作 | 内容 |
|------|------|------|
| D1 | 发一段语音 + 健康问卷链接 | 「Hi, 我是XX营养师, 欢迎! 先花 30 秒问卷让我了解你」 |
| D3 | 发一篇科普文章 | 主题: 跟用户人群相关的痛点科普 (不做功效承诺) |
| D7 | 发首单券 + 推荐组合 | 基于 D1 问卷推荐适配产品 |
| D15 | 朋友圈定向可见 | 用户证言合集 (合规版) |
| D30 | 首购提醒 / 复购咨询 | 按用法周期推送 |

每段文案 → 走 `scan_forbidden` 过合规:
```bash
for STAGE in D1 D3 D7 D15 D30; do
  TEXT="<该节点对应的模板文案>"
  RESULT=$(scan_forbidden "$TEXT")
  echo "$STAGE: $RESULT"
  # 命中 block → 改写 or 切到备用话术
done
```

## Step 6: 调企微 API 发送

对每个节点的名单循环发:

```bash
for USERID in $(echo "$D3_LIST" | jq -r '.[]'); do
  curl -s -X POST "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/send_welcome_msg?access_token=${ACCESS_TOKEN}" \
    -H "Content-Type: application/json" \
    -d "{
      \"welcome_code\": \"...\",
      \"text\": {\"content\": \"$D3_TEXT\"},
      \"attachments\": [{\"msgtype\": \"image\", \"image\": {\"media_id\": \"$MEDIA_ID\"}}]
    }"
  sleep 0.5  # 防封控
done
```

### 注意企微接口限制
- 单日单客户最多 1 条 (避免封号)
- 群发助手单企业单日上限 3 万
- 客户标签/朋友圈规则 详见官方文档

## Step 7: 记录触达结果

每次发完：
- 成功/失败数
- errcode 统计
- 失败客户清单 (供人工跟进)

```bash
exp_record "ecom-qiwei-sop-trigger" '"date":"'$TODAY'","D1":'$D1_COUNT',"D3":'$D3_COUNT',"D7":'$D7_COUNT',"D15":'$D15_COUNT',"D30":'$D30_COUNT',"success_rate":"'$SUCCESS_PCT'"'
```

## Step 8: 次日回收数据 (另一个 skill 做)

- D+1 看触达的 open_rate / reply_rate
- D+7 看 SOP 转化 (首单 / 咨询)
- 低于阈值 → 飞书告警 + 触发 [ecom-private-repurchase-reminder](../ecom-private-repurchase-reminder/) 调优

## Step 9: 推送每日 SOP 摘要到飞书

```bash
feishu_card "私域 SOP 触达 · ${TODAY}" "
**D1**: ${D1_COUNT} 发, 成功率 ${D1_SUCCESS}%
**D3**: ${D3_COUNT} 发, 成功率 ${D3_SUCCESS}%
...
**合规命中**: ${COMPLIANCE_BLOCK} 条被拦 (详见 artifacts)
"
```

## 失败 / 降级
- access_token 拿不到 → 检查 CORPID/SECRET 是否过期
- 发送 errcode=45009 → 触达频次过高，拉长 sleep
- 发送 errcode=48002 → 用户删除/拉黑企微 → 标记 churn 到 CSV, 不再触达

## 合规红线 (保健品朋友圈/群发特别注意)
- 朋友圈/群发属商业广告, 必出现「本品不能代替药物」
- 单日每人最多 3 条朋友圈广告
- 不得用国家机关/医生形象
- 分销层级 ≤ 2 级
- 健康问卷不得诱导填写敏感疾病 (会触发平台风控)
