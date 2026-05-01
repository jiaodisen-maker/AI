"""DSPy signatures for A2 Decomposition and A8 Generation.

`import dspy` 是 pip 包 dspy-ai；本目录已从 dspy/ 改名 dspy_opt/ 避免冲突。
"""
from __future__ import annotations

try:
    import dspy
except ImportError:
    dspy = None  # type: ignore[assignment]


if dspy is not None:

    class DecompositionSig(dspy.Signature):
        """从抖音保健品视频的 ASR/OCR/视觉描述拆 9 段式 + 4 类原子。"""

        asr_text: str = dspy.InputField(desc="视频 ASR 转写文本")
        ocr_text: str = dspy.InputField(desc="视频关键帧 OCR 字幕")
        visual_desc: str = dspy.InputField(desc="视觉理解描述")

        segments_json: str = dspy.OutputField(desc="9 段式 JSON 数组")
        atoms_json: str = dspy.OutputField(desc="hook/pain/trust/cta 4 类原子 JSON 数组")

    class GenerationSig(dspy.Signature):
        """根据目标 microtype + 可复用 atoms 反向生成 1 条新脚本。"""

        microtype_json: str = dspy.InputField(desc="目标 microtype 5 维标签 JSON")
        atoms_json: str = dspy.InputField(desc="可选原子库 JSON")

        script_json: str = dspy.OutputField(desc="完整 9 段脚本 + used_atom_ids JSON")
