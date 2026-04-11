"""LLM model router: intelligent routing between local, overseas, and specialized models."""

from __future__ import annotations

import logging
import time
from typing import Any

from app.config import settings
from app.llm.models import ChatRequest, ChatResponse

logger = logging.getLogger(__name__)

# Model mapping per preference tier
MODEL_MAP: dict[str, dict[str, Any]] = {
    "local": {
        "model": f"openai/{settings.local_model_name}",
        "api_base": settings.local_model_base_url,
        "api_key": settings.local_model_api_key,
    },
    "overseas_claude": {
        "model": "anthropic/claude-sonnet-4-20250514",
        "api_key": settings.anthropic_api_key,
    },
    "overseas_openai": {
        "model": "openai/gpt-4o",
        "api_key": settings.openai_api_key,
    },
}


class ModelRouter:
    """Routes LLM requests to the appropriate model based on preference and strategy.

    Routing logic:
    - local: always use local model (Qwen via vLLM)
    - overseas: prefer Claude, fallback to GPT-4o
    - specialized: use fine-tuned model endpoint
    - auto: follow the global routing strategy setting
    """

    def __init__(self) -> None:
        self.strategy = settings.model_routing_strategy
        self._call_count = {"local": 0, "overseas": 0, "specialized": 0}

    def _resolve_model(self, preference: str) -> dict[str, Any]:
        """Resolve model preference to concrete model config."""
        if preference == "auto":
            preference = self._auto_resolve()

        if preference == "local":
            return MODEL_MAP["local"]
        elif preference == "overseas":
            # Prefer Claude if API key is configured
            if settings.anthropic_api_key:
                return MODEL_MAP["overseas_claude"]
            elif settings.openai_api_key:
                return MODEL_MAP["overseas_openai"]
            # Fallback to local if no overseas keys
            logger.warning("No overseas API keys configured, falling back to local model")
            return MODEL_MAP["local"]
        elif preference == "specialized":
            # Specialized models use the same local endpoint with a different model name
            config = MODEL_MAP["local"].copy()
            config["model"] = f"openai/{settings.local_model_name}"
            return config
        else:
            return MODEL_MAP["local"]

    def _auto_resolve(self) -> str:
        """Resolve 'auto' preference based on global strategy."""
        if self.strategy == "local_first":
            return "local"
        elif self.strategy == "overseas_first":
            return "overseas"
        elif self.strategy == "cost_optimized":
            return "local"
        return "local"

    async def chat(self, request: ChatRequest) -> ChatResponse:
        """Send a chat request through the routing layer.

        Uses LiteLLM for unified API access across providers.
        """
        import litellm

        model_config = self._resolve_model(request.model_preference)
        pref = request.model_preference
        preference = pref if pref != "auto" else self._auto_resolve()
        self._call_count[preference] = self._call_count.get(preference, 0) + 1

        messages = [{"role": m.role.value, "content": m.content} for m in request.messages]

        start = time.monotonic()
        try:
            response = await litellm.acompletion(
                model=model_config["model"],
                messages=messages,
                temperature=request.temperature,
                max_tokens=request.max_tokens,
                api_base=model_config.get("api_base"),
                api_key=model_config.get("api_key"),
            )
        except Exception as e:
            logger.error("LLM call failed (model=%s): %s", model_config["model"], e)
            # Fallback: if overseas fails, try local; if local fails, raise
            if preference == "overseas":
                logger.info("Falling back to local model")
                return await self._fallback_local(request)
            raise

        latency_ms = int((time.monotonic() - start) * 1000)

        content = response.choices[0].message.content or ""
        usage = response.usage or type("Usage", (), {"prompt_tokens": 0, "completion_tokens": 0})()

        return ChatResponse(
            content=content,
            model_used=model_config["model"],
            input_tokens=getattr(usage, "prompt_tokens", 0),
            output_tokens=getattr(usage, "completion_tokens", 0),
            latency_ms=latency_ms,
        )

    async def _fallback_local(self, request: ChatRequest) -> ChatResponse:
        """Fallback to local model when overseas model fails."""
        fallback_request = request.model_copy(update={"model_preference": "local"})
        return await self.chat(fallback_request)

    def get_stats(self) -> dict[str, int]:
        """Return call count statistics per model tier."""
        return dict(self._call_count)
