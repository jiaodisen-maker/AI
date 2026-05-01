"""LLM client wrappers — used by A2 (Decomposition), A3 (Compliance double-validation),
A7 (Feasibility互评), A8 (Generation), A9 (Critic 三家互评).

3 个家族：
- Deepseek-V3 (deepseek-chat) via OpenAI-compatible endpoint @ api.deepseek.com
- Qwen-Max / Qwen2.5-VL via DashScope OpenAI-compatible endpoint
- Claude (claude-haiku-4-5-20251001) via anthropic SDK
"""
from .claude import call_claude
from .deepseek import call_deepseek, call_qwen, call_qwen_vl

__all__ = ["call_deepseek", "call_qwen", "call_qwen_vl", "call_claude"]
