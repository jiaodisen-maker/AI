"""Deepseek-V3 + Qwen via OpenAI-compatible endpoints."""
import os

from openai import OpenAI

DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DASHSCOPE_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"


def _deepseek_client() -> OpenAI:
    return OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"], base_url=DEEPSEEK_BASE_URL)


def _qwen_client() -> OpenAI:
    return OpenAI(api_key=os.environ["QWEN_API_KEY"], base_url=DASHSCOPE_BASE_URL)


def call_deepseek(
    system: str,
    user: str,
    *,
    model: str = "deepseek-chat",
    temperature: float = 0.3,
    response_format_json: bool = False,
) -> str:
    client = _deepseek_client()
    kwargs: dict = {
        "model": model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "temperature": temperature,
    }
    if response_format_json:
        kwargs["response_format"] = {"type": "json_object"}
    resp = client.chat.completions.create(**kwargs)
    return resp.choices[0].message.content or ""


def call_qwen(
    system: str,
    user: str,
    *,
    model: str = "qwen-max-latest",
    temperature: float = 0.3,
) -> str:
    client = _qwen_client()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        temperature=temperature,
    )
    return resp.choices[0].message.content or ""


def call_qwen_vl(
    system: str,
    user: str,
    image_urls: list[str],
    *,
    model: str = "qwen-vl-max-latest",
) -> str:
    """多模态：传 image url 列表（公开可访问 URL 或 OSS pre-signed URL）"""
    client = _qwen_client()
    content = [{"type": "image_url", "image_url": {"url": u}} for u in image_urls]
    content.append({"type": "text", "text": user})
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": content},
        ],
    )
    return resp.choices[0].message.content or ""
