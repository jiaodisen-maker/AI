"""媒体管道 — yt-dlp + FunASR + PaddleOCR + Qwen-VL。

完整实装。依赖在 [media] extras：
    pip install -e .[media]

入口：extract(url, workflow_id) -> dict   等价 manual_payload 结构
{
    "asr_text": str,
    "ocr_text": str,
    "visual_desc": str,
    "duration_sec": float | None,
    "media_uri": str   # MinIO s3://bucket/key
}
"""
from __future__ import annotations

import logging
import os
import tempfile
from pathlib import Path
from typing import Any

log = logging.getLogger(__name__)


def _check_deps() -> tuple[bool, str]:
    missing: list[str] = []
    try:
        import yt_dlp  # noqa: F401
    except ImportError:
        missing.append("yt-dlp")
    try:
        import funasr  # noqa: F401
    except ImportError:
        missing.append("funasr")
    try:
        import paddleocr  # noqa: F401
    except ImportError:
        missing.append("paddleocr")
    if missing:
        return False, "missing media deps: " + ", ".join(missing)
    return True, ""


def _download(url: str, out_dir: Path) -> tuple[Path, dict[str, Any]]:
    import yt_dlp

    out_template = str(out_dir / "%(id)s.%(ext)s")
    opts = {
        "outtmpl": out_template,
        "format": "best[ext=mp4]/best",
        "quiet": True,
        "no_warnings": True,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        path = Path(ydl.prepare_filename(info))
    return path, {
        "duration": info.get("duration"),
        "title": info.get("title"),
        "uploader": info.get("uploader"),
        "view_count": info.get("view_count"),
        "like_count": info.get("like_count"),
    }


def _upload_minio(path: Path, workflow_id: str) -> str:
    from ..storage import ensure_bucket, get_minio_client

    bucket = os.getenv("MINIO_BUCKET", "cases-media")
    client = get_minio_client()
    ensure_bucket(client, bucket)
    key = f"{workflow_id}/{path.name}"
    client.fput_object(bucket, key, str(path))
    return f"s3://{bucket}/{key}"


def _extract_audio(video_path: Path, audio_path: Path) -> None:
    import subprocess

    subprocess.run(
        [
            "ffmpeg",
            "-i", str(video_path),
            "-vn", "-ac", "1", "-ar", "16000",
            "-acodec", "pcm_s16le",
            "-y", str(audio_path),
        ],
        check=True,
        capture_output=True,
    )


def _asr(audio_path: Path) -> str:
    from funasr import AutoModel

    model = AutoModel(
        model="paraformer-zh",
        vad_model="fsmn-vad",
        punc_model="ct-punc",
        disable_update=True,
    )
    res = model.generate(input=str(audio_path))
    if isinstance(res, list) and res:
        return res[0].get("text", "")
    return ""


def _extract_keyframes(video_path: Path, out_dir: Path, interval_sec: float = 3.0) -> list[Path]:
    import subprocess

    out_dir.mkdir(parents=True, exist_ok=True)
    pattern = str(out_dir / "frame_%03d.jpg")
    subprocess.run(
        [
            "ffmpeg", "-i", str(video_path),
            "-vf", f"fps=1/{interval_sec}",
            "-q:v", "2",
            "-y", pattern,
        ],
        check=True,
        capture_output=True,
    )
    return sorted(out_dir.glob("frame_*.jpg"))


def _ocr_frames(frames: list[Path]) -> str:
    from paddleocr import PaddleOCR

    ocr = PaddleOCR(lang="ch", show_log=False)
    pieces: list[str] = []
    for f in frames:
        try:
            res = ocr.ocr(str(f), cls=True)
            if not res:
                continue
            for page in res:
                if not page:
                    continue
                for line in page:
                    if isinstance(line, list) and len(line) >= 2:
                        text = line[1][0] if isinstance(line[1], (tuple, list)) else None
                        if text:
                            pieces.append(text)
        except Exception as e:
            log.warning("OCR frame %s failed: %s", f.name, e)
    seen: set[str] = set()
    dedup: list[str] = []
    for t in pieces:
        if t not in seen:
            seen.add(t)
            dedup.append(t)
    return " / ".join(dedup)


def _visual_desc(frames: list[Path], minio_uri_prefix: str | None = None) -> str:
    """Qwen-VL 视觉理解。MinIO 给 pre-signed URL；本地路径直接读不可行，需 URL。

    简化：用前 5 张帧 base64 编码送 Qwen-VL（OpenAI-compatible 多模态接口）。
    """
    import base64

    from ..llm.deepseek import _qwen_client

    if not frames:
        return ""

    sampled = frames[: min(5, len(frames))]
    image_parts = []
    for f in sampled:
        b64 = base64.b64encode(f.read_bytes()).decode("ascii")
        image_parts.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{b64}"},
        })
    image_parts.append({
        "type": "text",
        "text": "请描述这组关键帧的核心视觉元素：人物 / 场景 / 道具 / 镜头切换 / 字幕样式。"
                "输出 1 段 ≤200 字的中文描述。",
    })

    client = _qwen_client()
    try:
        resp = client.chat.completions.create(
            model="qwen-vl-max-latest",
            messages=[{"role": "user", "content": image_parts}],
        )
        return resp.choices[0].message.content or ""
    except Exception as e:
        log.warning("Qwen-VL call failed: %s", e)
        return ""


def extract(url: str, workflow_id: str) -> dict[str, Any]:
    """主入口。失败抛异常让 Temporal 重试。"""
    ok, msg = _check_deps()
    if not ok:
        raise NotImplementedError(msg + " — install with `pip install -e .[media]`")

    with tempfile.TemporaryDirectory(prefix="a2-media-") as tmp:
        tmp_dir = Path(tmp)
        log.info("A2 media: downloading %s", url)
        video_path, meta = _download(url, tmp_dir)

        media_uri = _upload_minio(video_path, workflow_id)
        log.info("A2 media: uploaded → %s", media_uri)

        audio_path = tmp_dir / "audio.wav"
        _extract_audio(video_path, audio_path)
        asr_text = _asr(audio_path)
        log.info("A2 media: ASR done (%d chars)", len(asr_text))

        frames_dir = tmp_dir / "frames"
        frames = _extract_keyframes(video_path, frames_dir)
        log.info("A2 media: extracted %d keyframes", len(frames))

        ocr_text = _ocr_frames(frames)
        log.info("A2 media: OCR done (%d chars)", len(ocr_text))

        visual = _visual_desc(frames)
        log.info("A2 media: Qwen-VL visual desc done")

    return {
        "asr_text": asr_text,
        "ocr_text": ocr_text,
        "visual_desc": visual,
        "duration_sec": meta.get("duration"),
        "media_uri": media_uri,
        "raw_meta": meta,
    }
