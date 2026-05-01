"""Claude (Anthropic SDK). 用于 A9 Critic 三家互评中的第三家。"""
import os

from anthropic import Anthropic

DEFAULT_MODEL = "claude-haiku-4-5-20251001"


def call_claude(
    system: str,
    user: str,
    *,
    model: str = DEFAULT_MODEL,
    max_tokens: int = 4096,
) -> str:
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    resp = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    parts = [b.text for b in resp.content if b.type == "text"]
    return "".join(parts)
