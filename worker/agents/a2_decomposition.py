"""A2 Decomposition Agent — W1 实装。

5 步内部活动：
1) yt-dlp 下载视频 → MinIO
2) FunASR 转写 → asr_text
3) PaddleOCR 抽关键帧字幕 → ocr_text
4) Qwen2.5-VL 视觉理解 → visual_desc
5) Deepseek-V3 (DSPy signature) 9 段拆解 + 4 类原子抽取 → 写 cases / case_segments / atoms

返回：case_id (UUID)
"""
from typing import Any

from temporalio import activity


@activity.defn
async def decompose(case_input: dict[str, Any]) -> str:
    raise NotImplementedError("A2 Decomposition — W1 deliverable")
