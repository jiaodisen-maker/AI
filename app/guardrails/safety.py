"""Safety guardrails for agent inputs and outputs.

Checks for prompt injection, PII leakage, and harmful content.
This is the first-pass rule-based layer; NeMo Guardrails adds
LLM-based semantic checking on top.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class GuardResult:
    """Result of a safety check."""

    passed: bool = True
    issues: list[str] = field(default_factory=list)


# Patterns that indicate prompt injection attempts
INJECTION_PATTERNS: list[re.Pattern] = [
    re.compile(r"ignore\s+(all\s+)?previous\s+instructions", re.IGNORECASE),
    re.compile(r"disregard\s+(all\s+)?prior", re.IGNORECASE),
    re.compile(r"you\s+are\s+now\s+(?:a|an)\s+", re.IGNORECASE),
    re.compile(r"system\s*:\s*", re.IGNORECASE),
    re.compile(r"<\s*system\s*>", re.IGNORECASE),
    re.compile(r"忽略.*(?:之前|上面|以上).*(?:指令|指示|要求)", re.IGNORECASE),
    re.compile(r"你现在是", re.IGNORECASE),
]

# PII patterns (Chinese ID, phone, email)
PII_PATTERNS: list[tuple[str, re.Pattern]] = [
    ("身份证号", re.compile(r"\d{17}[\dXx]")),
    ("手机号", re.compile(r"1[3-9]\d{9}")),
    ("邮箱", re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")),
    ("银行卡号", re.compile(r"\d{16,19}")),
]


class SafetyGuard:
    """Rule-based safety checks for inputs and outputs."""

    def check_input(self, text: str) -> GuardResult:
        """Check user input for injection and safety issues."""
        result = GuardResult()

        for pattern in INJECTION_PATTERNS:
            if pattern.search(text):
                result.passed = False
                result.issues.append(
                    f"检测到潜在的 prompt 注入攻击: {pattern.pattern[:50]}"
                )

        return result

    def check_output(self, text: str) -> GuardResult:
        """Check agent output for PII leakage."""
        result = GuardResult()

        for pii_name, pattern in PII_PATTERNS:
            if pattern.search(text):
                result.issues.append(f"输出中可能包含{pii_name}，建议脱敏")

        return result

    def check_both(self, input_text: str, output_text: str) -> GuardResult:
        """Run both input and output checks."""
        input_result = self.check_input(input_text)
        output_result = self.check_output(output_text)

        return GuardResult(
            passed=input_result.passed and output_result.passed,
            issues=input_result.issues + output_result.issues,
        )
