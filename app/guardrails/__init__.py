"""Guardrails layer: input/output safety validation.

Uses rule-based checks for common safety patterns.
NeMo Guardrails integration planned for Phase 2.
"""

from app.guardrails.safety import SafetyGuard

__all__ = ["SafetyGuard"]
