"""LLM model router using LiteLLM's built-in Router for retry/fallback/cooldown."""

from __future__ import annotations

import logging
import time
from typing import Any

from app.config import settings
from app.llm.models import ChatRequest, ChatResponse

logger = logging.getLogger(__name__)


def _build_model_list() -> list[dict[str, Any]]:
    """Build LiteLLM Router model list from settings."""
    models = []

    # Local model (always available)
    models.append({
        "model_name": "local",
        "litellm_params": {
            "model": f"openai/{settings.local_model_name}",
            "api_base": settings.local_model_base_url,
            "api_key": settings.local_model_api_key,
        },
    })

    # Overseas Claude (if configured)
    if settings.anthropic_api_key:
        models.append({
            "model_name": "overseas",
            "litellm_params": {
                "model": "anthropic/claude-sonnet-4-20250514",
                "api_key": settings.anthropic_api_key,
            },
        })

    # Overseas OpenAI (if configured)
    if settings.openai_api_key:
        models.append({
            "model_name": "overseas",
            "litellm_params": {
                "model": "openai/gpt-4o",
                "api_key": settings.openai_api_key,
            },
        })

    return models


class ModelRouter:
    """Routes LLM requests using LiteLLM Router (built-in retry, fallback, cooldown).

    No more hand-written fallback logic.
    """

    def __init__(self) -> None:
        from litellm import Router

        model_list = _build_model_list()
        self._router = Router(
            model_list=model_list,
            num_retries=2,
            timeout=30,
            fallbacks=[{"overseas": ["local"]}],  # overseas fails → try local
        )
        self._call_count: dict[str, int] = {}

    def _resolve_model_name(self, preference: str) -> str:
        """Map preference to LiteLLM Router model_name."""
        if preference == "auto":
            if settings.model_routing_strategy == "overseas_first":
                return "overseas"
            return "local"
        if preference in ("local", "overseas", "specialized"):
            return preference if preference != "specialized" else "local"
        return "local"

    async def chat(self, request: ChatRequest) -> ChatResponse:
        """Send a chat request through LiteLLM Router."""
        model_name = self._resolve_model_name(request.model_preference)
        self._call_count[model_name] = self._call_count.get(model_name, 0) + 1

        messages = [
            {"role": m.role.value, "content": m.content}
            for m in request.messages
        ]

        start = time.monotonic()
        try:
            response = await self._router.acompletion(
                model=model_name,
                messages=messages,
                temperature=request.temperature,
                max_tokens=request.max_tokens,
            )
        except Exception as e:
            logger.error("LLM call failed: %s", e)
            raise

        latency_ms = int((time.monotonic() - start) * 1000)
        content = response.choices[0].message.content or ""
        usage = response.usage

        return ChatResponse(
            content=content,
            model_used=model_name,
            input_tokens=getattr(usage, "prompt_tokens", 0) if usage else 0,
            output_tokens=getattr(usage, "completion_tokens", 0) if usage else 0,
            latency_ms=latency_ms,
        )

    def get_stats(self) -> dict[str, int]:
        """Return call count statistics."""
        return dict(self._call_count)
