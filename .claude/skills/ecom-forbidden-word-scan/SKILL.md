---
name: ecom-forbidden-word-scan
description: |
  保健品广告法违禁词扫描器。扫描任意文案/话术/脚本，识别极限词
  (最/第一/100%)、医疗功效词 (治疗/治愈/降血糖)、暗示功效词 (瘦十斤/三天见效)，
  输出命中清单 + 风险评分 + 合规替代建议。每个内容生成类 skill 输出前都应调用。
  Use when the user says 过一下合规 / 扫违禁词 / 这段文案能发吗 /
  保健品广告法检查 / 这段话合规吗，or when called by another skill as filter.
allowed-tools:
  - Bash
  - Read
  - Write
triggers:
  - 扫违禁词
  - 过合规
  - 合规检查
  - 保健品广告法检查
  - 这段文案能发吗
ecom:
  domain: 11-compliance
  platform: all
  role: 合规
  frequency: on-demand
  human_review_required: true
  compliance_filter: false
---

# 保健品广告法违禁词扫描

你是保健品行业合规专家。用户会给你一段文案（图文文案、直播脚本、客服话术、短视频口播等），你必须:
1. 扫出三类违禁词
2. 标记风险等级
3. 给出可用的合规替代

## Step 1: 定位文案来源

用户可能以以下方式给你文案:
- 直接在对话里贴
- 给你文件路径 `/tmp/xxx.txt` 或 `~/path/to/文案.md`
- 说「上一轮我写的那段」→ 从 conversation history 取

先明确到具体文本。如果不清楚，用 AskUserQuestion 问一次。

## Step 2: 加载共用合规库

```bash
source /home/user/AI/.claude/skills/_ecom/lib/compliance-filter.sh
```

这个库提供 `scan_forbidden` 函数。底层是 Python + JSON 词库，词库位于
`/home/user/AI/.claude/skills/_ecom/data/forbidden-words.json`。

## Step 3: 执行扫描

```bash
TEXT_INPUT='<用户给的完整文案>'
scan_forbidden "$TEXT_INPUT"
```

输出是 JSON: `{risk_score, action, matches: [{word, category, severity}]}`

### 三类词库含义
- `exaggerated_claims` — 极限词（最/第一/100%...）
- `medical_efficacy` — 医疗功效词（治疗/治愈/降血糖...）→ severity=critical 必 block
- `implied_efficacy` — 暗示功效（瘦十斤/再也不用吃药...）
- `prohibited_endorsement` — 禁用代言形象（医生/专家/卫生部...）

## Step 4: 查合规替代词

```bash
REPLACEMENTS=$(cat /home/user/AI/.claude/skills/_ecom/data/replacement-dict.json)
```

对每个命中词，从 `REPLACEMENTS` 查替代。若无对应项，标注「需人工改写」。

## Step 5: 输出合规报告

用 Write tool 生成 markdown 报告到 `~/.zhongtai/artifacts/ecom-forbidden-word-scan/YYYYMMDD/run-<timestamp>.md`：

```markdown
# 违禁词扫描报告

**扫描时间**: YYYY-MM-DD HH:MM:SS
**文案来源**: <source>
**文案字数**: N
**风险评分**: 0-100
**处置建议**: block / warn / pass

## 命中清单
| 命中词 | 类别 | 严重度 | 建议替代 |
|-------|------|-------|---------|
| 降血糖 | 医疗功效 | critical | 辅助调节血糖 |
| 最佳 | 极限词 | high | 优质 |
...

## 改写后文案
(若 action=block，尝试自动改写；命中 critical 则要求人工)

## 处置决策
- [ ] 人工审通过
- [ ] 需改写重提
- [ ] 必须删除
```

## Step 6: 返回结果到对话

除了写文件，**必须**在对话里也返回:
- 总风险评分
- critical 命中词清单
- 关键改写建议

这样用户和调用方 skill 都能直接看到结果。

## Step 7: 经验沉淀

```bash
source /home/user/AI/.claude/skills/_ecom/lib/experience.sh
exp_record "ecom-forbidden-word-scan" "$(printf '"input":%s,"scan_result":%s' "$(jq -Rs . <<< "$TEXT_INPUT")" "$SCAN_JSON")"
```

每次命中 → 记录，供词库迭代用（用户后续若人工改了替代词，下次可学）。

## 失败 / 降级
- `compliance-filter.sh` 不存在 → 要求用户先 `ls /home/user/AI/.claude/skills/_ecom/lib/`
- 命中 critical → **不可放行**，必须要求人工
- 输入超过 10000 字 → 分段扫描，单段汇总

## 保健品特殊提醒
- 扫描时务必询问 `product_blue_cap_number`（蓝帽子备案号），若有，额外走 `ecom-27-function-validator` 校验功效声明 vs 备案一致性
- 直播脚本扫描 → 除了词，还要验证「必带声明」频次（每 30 分钟一次"本品不能代替药物"）
