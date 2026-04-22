---
name: forbidden-word-scan
domain: 11-compliance
platform: all
role: 合规
frequency: on-demand
inputs:
  - text: 需审核的文本 (文案/话术/脚本)
  - context: 发布场景 (保健食品广告/普通食品/私域/直播/客服话术)
outputs:
  - 命中词列表 + 类别 + 风险等级 + 建议替代词
  - 整体风险评分 (0-100) + block / warn / pass
human_review_required: true
compliance_filter: false
data_sources:
  - 内部违禁词库 (三类: 极限词/医疗功效/暗示功效)
  - 句易网 / 蝉妈妈 / 千瓜 (第三方校对)
  - 国家市场监督管理总局 广告法
allowed-tools:
  - Read
  - Write
---

# 广告法违禁词扫描 (`forbidden-word-scan`)

## 何时调用
任何内容生成类 skill 输出前，或客服外发话术前，或投放素材提审前。

## 输入
- **text** (必填) — string — 需审核的文本
- **context** (必填) — enum — 发布场景
- **product_type** (选填) — 保健食品 / 普通食品 / 医疗器械

## 输出
- `matches`: `[{word, category, severity, suggestion}]`
- `risk_score`: 0-100
- `action`: block | warn | pass

## Workflow
1. 加载三类违禁词库: 极限词 / 医疗功效 / 暗示功效
2. 加载上下文敏感词: 场景 = 保健品广告时额外挂"扩大宣传"词库
3. 全文 + 句级扫描（含谐音黑话、拼音变体、表情符号变体）
4. 计算 severity (critical=必违法, high=高风险, medium=建议改)
5. 每个命中词给出合规替代词
6. 输出 JSON + action 决策

## 三类词库

### 极限词
最 / 第一 / 国家级 / 100% / 顶级 / 唯一 / 王牌 / 绝对 / 最佳 / 最优 / 顶尖 / ...

### 医疗功效词
治疗 / 治愈 / 根治 / 速效 / 抗癌 / 降三高 / 防癌 / 抑制 / 替代药品 / 疗效 / 见效 / ...

### 暗示功效词
瘦十斤 / 三天见效 / 再也不用吃药 / 小糖人 (谐音) / ...

## 替代话术库
| 违禁 | 合规替代 |
|------|---------|
| 降血脂 | 辅助调节血脂 |
| 降血糖 | 辅助调节血糖 |
| 治疗便秘 | 有助于润肠通便 |
| 最佳 | 优质 / 推荐 |
| 100% 有效 | 优选成分 |

## 失败/降级
- 词库缺失 → 返回 error + 人工审
- 命中 critical → 强制 block，不可放行
- 命中 medium → warn，人工决策

## 经验沉淀
记录每次 block + 人工最终决策 → 更新词库 + 训练替代词模型。
