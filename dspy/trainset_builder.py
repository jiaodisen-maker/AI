"""Build DSPy training set from critic_scores — W3 实装。

A2 trainset：
- 高分 case 的 (asr+ocr+visual) → (segments, atoms)，用于 BootstrapFewShot 学拆解
A8 trainset：
- 高分 generated_script 的 (microtype, atoms) → script，用于学反向生成
"""
