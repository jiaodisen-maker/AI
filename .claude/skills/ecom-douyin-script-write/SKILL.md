---
name: ecom-douyin-script-write
description: |
  抖音短视频脚本自动生成。从用户给的产品 SKU + 人群 + 时长生成合规脚本，
  四段结构 (0-3s Hook / 3-10s 痛点 / 10-20s 卖点+资质 / 20-30s CTA)，
  出稿前自动走 ecom-forbidden-word-scan 过广告法，再用 ecom-27-function-validator
  校验蓝帽子备案一致性，命中必改再出稿。输出 3 个候选 + 封面标题 + 拍摄 shotlist。
  Use when user says 写抖音脚本 / 来条短视频脚本 / 抖音短视频文案 /
  douyin script / 这个 SKU 写个脚本.
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
triggers:
  - 写抖音脚本
  - 来条短视频脚本
  - 抖音短视频文案
  - 抖音脚本
ecom:
  domain: 02-content-commerce
  platform: douyin
  role: 内容
  frequency: on-demand
  human_review_required: true
  compliance_filter: true
  data_sources: [巨量算数, 蝉妈妈, 本公司 SKU/蓝帽子库]
---

# 抖音短视频脚本生成

你是保健品短视频爆款脚本编剧。输出的每条脚本都必须过两道合规门。

## Step 1: 收集必要上下文

如果用户没给，主动用 AskUserQuestion 问:
1. **SKU / 产品名** — 对应哪个蓝帽子备案
2. **目标人群** — 中老年 / 熬夜党 / 宝妈 / 健身党 / 术后康复 / ...
3. **视频时长** — 15s / 30s / 60s
4. **主打卖点** — 成分 / 使用场景 / 价格 / 权威背书 / 用户证言
5. **风格** — 口播 / 剧情 / 测评 / 对比 / 科普

## Step 2: 查本公司 SKU 备案

```bash
REG="/home/user/AI/.claude/skills/_ecom/data/blue-cap-registry.json"
python3 -c "
import json
with open('$REG') as f: reg = json.load(f)
sku = input('SKU/蓝帽子号: ')
print(json.dumps(reg.get(sku, {}), ensure_ascii=False, indent=2))
" <<< "<用户给的 SKU 或蓝帽子号>"
```

拿到:
- `registered_functions` — 可宣传的功能（27 项中的子集）
- `适宜人群` / `不适宜人群`
- `食用量`

**如果查不到** → 告诉用户「没找到蓝帽子备案，请先用 ecom-blue-cap-sync 同步，或手工确认能宣传什么」，然后 AskUserQuestion 请用户手填功能。

## Step 3: 查行业爆款素材（可选，提升命中率）

如果有 `~/.zhongtai/credentials/chanmama-cookies.json`（蝉妈妈），尝试:

```bash
source /home/user/AI/.claude/skills/_ecom/lib/browser-setup.sh
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
cred_exists chanmama && {
  $B cookie-import "$(cred_path chanmama)"
  $B goto "https://www.chanmama.com/promotionRank/index"
  $B wait --networkidle
  $B text > /tmp/chanmama-top-$(date +%Y%m%d).txt
}
```

没凭证就跳过（不阻塞）。

## Step 4: 生成 3 个候选脚本

基于：用户给的卖点 × 备案允许的功能 × 人群痛点，你自己（作为 LLM）生成 3 个不同风格的候选。

每个脚本四段：

```
[0-3s Hook]
  钩子类型: 痛点提问 / 反常识结论 / 视觉冲击
  画面: ...
  旁白: ...

[3-10s 痛点放大]
  画面: ...
  旁白: ...

[10-20s 卖点 + 资质背书]
  画面: 产品特写 + 蓝帽子 logo + 检测报告 + 广告批文号
  旁白: 不可说疗效, 用「辅助 / 帮助维持 / 有助于」
  必带: 「本品不能代替药物」字幕 + 口播

[20-30s CTA]
  画面: 小黄车引导
  旁白: 价格利益点 + 限时 + 下单
```

## Step 5: 合规过审 (每条候选都跑)

```bash
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh

for i in 1 2 3; do
  SCRIPT_I="<候选 $i 全文>"
  RESULT=$(scan_forbidden "$SCRIPT_I")
  echo "候选$i: $RESULT"

  # 功效一致性
  validate_27_function "$SCRIPT_I" "<蓝帽子号>"
done
```

若任意候选 `action=block` 或 `verdict=broader_or_unrelated`:
- 尝试自动改写（查 `replacement-dict.json`）
- 再过一次
- 若仍 block → 标红该候选，用 AskUserQuestion 问用户要不要放弃这条

## Step 6: 出封面 + 标题

每个候选给出：
- **封面三件套**: 主标题（6-8 字）+ 副卖点（10-15 字）+ 人物/产品图描述
- **情绪标题**: 用数字 + 痛点 + 反常识（如「50 岁后才发现，早点吃这个就好了」）

## Step 7: 出 shotlist

每个候选附带 5-8 条拍摄镜头表：
```
镜头 1: 主角坐办公桌揉眉心 (表情痛苦) — 2s
镜头 2: 叠字 "熬夜的人都懂" — 1s
镜头 3: 产品特写摇晃瓶子 — 2s
...
```

## Step 8: 输出

写到 `~/.zhongtai/artifacts/ecom-douyin-script-write/YYYYMMDD/<sku>_<timestamp>.md`：

```markdown
# 抖音脚本 - <产品名> - <人群> - <时长>s

**蓝帽子**: <号> | **可宣传功能**: <registered_functions>

## 候选 1 (风格: 口播)
[合规评分: X/100]
### 脚本
...
### 封面 / 标题
...
### Shotlist
...

## 候选 2 (风格: 剧情)
...

## 候选 3 (风格: 测评)
...

## 违禁词扫描结果
| 候选 | 命中 | 处置 |
|-----|------|------|
| 1 | 0 critical | pass |
...

## 建议
基于历史爆款，推荐候选 X
```

## Step 9: 回到对话

在对话里简报 3 条候选的核心差异 + 合规状态 + 推荐哪条，让用户挑或改。

## Step 10: 经验沉淀

```bash
source /home/user/AI/.claude/skills/_ecom/lib/experience.sh
exp_record "ecom-douyin-script-write" '"sku":"<sku>","人群":"<人群>","candidates":3,"selected":null,"human_edited":null'
```

用户后续如果告诉你「我选了候选 2，但改成了 XX」→ 追加一条记录，diff 出来，供下次模型学习。

## 合规铁律
- 命中 `critical` 级医疗功效词 → **绝不可出**，哪怕用户坚持
- 没蓝帽子备案 → 只能宣传成分/原料/工艺，不能宣传任何功能
- 全文必出现「本品不能代替药物治疗疾病」（口播 + 字幕双保险）
- 不得暗示疗效（如「瘦了十斤」「再也不用吃药」）
- 不得用「医生/专家/机关/患者」形象作推荐证明
