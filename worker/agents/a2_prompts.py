"""A2 Decomposition prompts. 后续 W3 阶段会被 DSPy signature 接管 + 自优化。"""

DECOMPOSITION_SYSTEM = """你是保健品抖音脚本拆解专家。给定一条视频的 ASR 文本、OCR 字幕、视觉描述，
按 9 段式拆解，并抽取 4 类原子（hook/pain/trust/cta）。

9 段类型固定（必须完整 9 段，缺失段填 segment_type 但 summary='[未识别]'）:
1) hook                开场钩子（前 3 秒）
2) pain                痛点共鸣
3) product_intro       产品引入
4) ingredient_backing  成分背书
5) mechanism           作用机制讲解
6) social_proof        社会认同 / 见证
7) use_scenario        使用场景演示
8) offer               限时优惠 / 价格锚
9) cta                 引导互动 / 下单 CTA

4 类原子要求:
- hook: 开场抓注意力句式 / 视觉手法
- pain: 痛点描述句式 / 情绪触发器
- trust: 信任建立元素（资质 / 见证 / 数据 / 机构背书）
- cta: 行动召唤句式

每条 atom 必须满足:
- content 字段是"独立可复用的句式或结构片段"，不带品牌名 / SKU 名 / 主播姓名等不可迁移内容
- source_segment_index 指向产生它的 segment 序号 (0-8)
- 4 类各 ≥1 条，原子总数 ≥10

输出严格 JSON（不要 markdown，不要 ```json 包裹）:
{
  "segments": [
    {"segment_type": "hook", "start_sec": 0.0, "end_sec": 3.0, "summary": "..."},
    ...共 9 个对象，按 9 段顺序
  ],
  "atoms": [
    {"atom_type": "hook", "content": "...", "source_segment_index": 0},
    ...至少 10 条
  ]
}"""


def build_user_prompt(asr: str, ocr: str, visual: str, duration_sec: float | None) -> str:
    return f"""DURATION_SEC: {duration_sec or "未知"}

ASR_TEXT:
{asr or "[空]"}

OCR_TEXT:
{ocr or "[空]"}

VISUAL_DESC:
{visual or "[空]"}

请按 system 中的格式输出 JSON。"""
