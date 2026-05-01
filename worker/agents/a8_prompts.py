"""A8 Generation prompts. W3 阶段会被 DSPy signature 接管。"""

GENERATION_SYSTEM_DEFAULT = """你是保健品抖音脚本反向生成专家。给定一组目标 microtype 5 维标签 +
一批可复用原子（hooks / pains / trusts / ctas），按 9 段式输出 1 条新脚本。

9 段顺序固定：
hook → pain → product_intro → ingredient_backing → mechanism →
social_proof → use_scenario → offer → cta

规则：
- 每段 1-3 句口播文案，自然衔接
- 选用的原子须与 microtype 5 维匹配
- 严守合规：不得出现疗效宣称 / 绝对化用语 / 患者证言 / 数据造假
- 不得输出品牌名 / SKU 名（用占位符 [品牌] [产品]）
- 总字数 ≤300 字

输出严格 JSON（不要 markdown）:
{"script": "<完整 9 段脚本，段间用换行分隔>",
 "used_atom_ids": ["<atom uuid>", ...],
 "9_stage_breakdown": [{"stage": "hook", "text": "..."}, ...]}"""


def build_generation_user(microtype: dict, atoms: list[dict]) -> str:
    return f"""目标 microtype:
{_fmt_microtype(microtype)}

可选原子库（请从中挑选与 microtype 适配的）:
{_fmt_atoms(atoms)}

按 system 中的格式输出 JSON。"""


def _fmt_microtype(m: dict) -> str:
    return (
        f"  scene={m.get('scene')}\n"
        f"  audience={m.get('audience')}\n"
        f"  ingredient={m.get('ingredient')}\n"
        f"  emotion={m.get('emotion')}\n"
        f"  restriction={m.get('restriction')}"
    )


def _fmt_atoms(atoms: list[dict]) -> str:
    by_type: dict[str, list[dict]] = {"hook": [], "pain": [], "trust": [], "cta": []}
    for a in atoms:
        by_type.setdefault(a["atom_type"], []).append(a)
    lines: list[str] = []
    for t in ("hook", "pain", "trust", "cta"):
        lines.append(f"\n[{t}]")
        for a in by_type.get(t, []):
            grade = a.get("compliance_grade") or "?"
            lines.append(f"  - id={a['id']} grade={grade} content={a['content'][:120]}")
    return "\n".join(lines)
