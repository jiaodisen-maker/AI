"""Claude (Anthropic SDK). 用于 A9 Critic 三家互评中的第三家。

支持两种模式：
1) LLM_BASE_URL + LLM_API_KEY 设置 → 通过 OpenAI 兼容接口调（聚合端点）
2) ANTHROPIC_API_KEY 设置 → 走原生 Anthropic SDK
"""
import os

DEFAULT_MODEL = "claude-haiku-4-5-20251001"


def call_claude(
    system: str,
    user: str,
    *,
    model: str | None = None,
    max_tokens: int = 4096,
) -> str:
    model = model or os.getenv("LLM_MODEL_CLAUDE") or DEFAULT_MODEL
    # 聚合端点优先（OpenAI 兼容）
    if os.getenv("LLM_BASE_URL") and os.getenv("LLM_API_KEY"):
        from openai import OpenAI

        client = OpenAI(api_key=os.environ["LLM_API_KEY"], base_url=os.environ["LLM_BASE_URL"])
        resp = client.chat.completions.create(
            model=model,
            max_tokens=max_tokens,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        return resp.choices[0].message.content or ""

    # 原生 Anthropic SDK
    from anthropic import Anthropic

    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    resp = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    parts = [b.text for b in resp.content if b.type == "text"]
    return "".join(parts)
