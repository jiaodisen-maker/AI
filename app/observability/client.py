"""Langfuse observability integration with no-op fallback."""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


class ObservabilityClient:
    """Langfuse client wrapper with no-op fallback.

    Set LANGFUSE_PUBLIC_KEY + LANGFUSE_SECRET_KEY in .env to enable.
    """

    def __init__(self) -> None:
        self._client = None
        self._enabled = False
        self._init_langfuse()

    def _init_langfuse(self) -> None:
        try:
            from app.config import settings
            public_key = getattr(settings, "langfuse_public_key", "")
            secret_key = getattr(settings, "langfuse_secret_key", "")
            if not public_key or not secret_key:
                logger.info("Langfuse not configured, observability disabled")
                return

            from langfuse import Langfuse
            self._client = Langfuse(
                public_key=public_key,
                secret_key=secret_key,
                host=getattr(
                    settings, "langfuse_host", "https://cloud.langfuse.com"
                ),
            )
            self._enabled = True
            logger.info("Langfuse observability enabled")
        except ImportError:
            logger.info("Langfuse SDK not installed")
        except Exception as e:
            logger.warning("Langfuse init failed: %s", e)

    @property
    def enabled(self) -> bool:
        return self._enabled

    def trace_skill_execution(
        self,
        skill_id: str,
        user_id: str,
        input_message: str,
        output_content: str,
        execution_time_ms: int,
        success: bool = True,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """Record a skill execution trace."""
        if not self._enabled or not self._client:
            return
        try:
            self._client.trace(
                name=f"skill:{skill_id}",
                user_id=user_id,
                input={"message": input_message},
                output={"content": output_content},
                metadata={
                    "execution_time_ms": execution_time_ms,
                    "success": success,
                    **(metadata or {}),
                },
            )
        except Exception as e:
            logger.warning("Langfuse trace failed: %s", e)

    def trace_llm_call(
        self,
        model: str,
        messages: list[dict],
        response: str,
        tokens_input: int,
        tokens_output: int,
        latency_ms: int,
    ) -> None:
        """Record an LLM API call."""
        if not self._enabled or not self._client:
            return
        try:
            self._client.generation(
                name=f"llm:{model}",
                model=model,
                input=messages,
                output=response,
                usage={"input": tokens_input, "output": tokens_output},
                metadata={"latency_ms": latency_ms},
            )
        except Exception as e:
            logger.warning("Langfuse generation trace failed: %s", e)

    def flush(self) -> None:
        if self._client:
            try:
                self._client.flush()
            except Exception:
                pass


_observability: ObservabilityClient | None = None


def get_observability() -> ObservabilityClient:
    global _observability
    if _observability is None:
        _observability = ObservabilityClient()
    return _observability
