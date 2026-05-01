"""DSPy signatures for A2 Decomposition and A8 Generation — W3 实装。

设计要点：
- DecompositionSig: input=(asr_text, ocr_text, visual_desc) → output=(segments_json, atoms_json)
  segments_json 必须满足 9 段式契约；atoms_json 4 类各 ≥1 条
- GenerationSig: input=(microtype_dict, atoms_list, n) → output=(scripts_list)
  脚本必须满足 9 段式 + microtype 5 维约束
- 二者都用 BootstrapFewShot 优化（trainset 从 critic_scores 拉）
"""
# import dspy
# class DecompositionSig(dspy.Signature): ...
# class GenerationSig(dspy.Signature): ...
