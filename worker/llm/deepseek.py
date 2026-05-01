"""Deepseek-V3 + Qwen via OpenAI-compatible endpoints.

支持三种凭据来源（优先级由高到低）：
1) LLM_BASE_URL + LLM_API_KEY  — 统一聚合端点（如 dataeyes.ai）
2) DEEPSEEK_BASE_URL / QWEN_BASE_URL + 各自的 API_KEY  — 分别配置
3) 硬编码默认（api.deepseek.com / dashscope.aliyuncs.com）
"""
import os

from openai import OpenAI

DEEPSEEK_DEFAULT = "https://api.deepseek.com"
DASHSCOPE_DEFAULT = "https://dashscope.aliyuncs.com/compatible-mode/v1"


def _resolve(url_env: str, key_env: str, url_default: str) -> tuple[str, str]:
    """聚合端点优先 → 单独配置 → 默认。返回 (base_url, api_key)。"""
    if os.getenv("LLM_BASE_URL") and os.getenv("LLM_API_KEY"):
        return os.environ["LLM_BASE_URL"], os.environ["LLM_API_KEY"]
    base = os.getenv(url_env) or url_default
    key = os.environ[key_env]
    return base, key


def _deepseek_client() -> OpenAI:
    base, key = _resolve("DEEPSEEK_BASE_URL", "DEEPSEEK_API_KEY", DEEPSEEK_DEFAULT)
    return OpenAI(api_key=key, base_url=base)


def _qwen_client() -> OpenAI:
    base, key = _resolve("QWEN_BASE_URL", "QWEN_API_KEY", DASHSCOPE_DEFAULT)
    return OpenAI(api_key=key, base_url=base)


def call_deepseek(
    system: str,
    user: str,
    *,
    model: str | None = None,
    temperature: float = 0.3,
    response_format_json: bool = False,
) -> str:
    model = model or os.getenv("LLM_MODEL_DEEPSEEK") or "deepseek-chat"
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
    model: str | None = None,
    temperature: float = 0.3,
) -> str:
    model = model or os.getenv("LLM_MODEL_QWEN") or "qwen-max-latest"
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
    model: str | None = None,
) -> str:
    """多模态：传 image url 列表（公开可访问 URL 或 OSS pre-signed URL）"""
    model = model or os.getenv("LLM_MODEL_QWEN_VL") or "qwen-vl-max-latest"
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
