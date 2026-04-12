"""Evaluation set framework for Skills.

An EvalSet is a collection of test cases used to measure
Skill quality (correctness, compliance, latency).

Phase 6 introduces:
  - EvalCase: input + expected output / properties
  - EvalSet: collection with versioning
  - EvalRunner: runs cases against a Skill, computes metrics
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class EvalCase:
    """A single evaluation case."""

    id: str
    input_message: str
    expected_contains: list[str] = field(default_factory=list)
    expected_not_contains: list[str] = field(default_factory=list)
    expected_skill_id: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class EvalResult:
    """Result of running one case against a skill."""

    case_id: str
    passed: bool
    reason: str = ""
    output: str = ""
    latency_ms: int = 0


@dataclass
class EvalSet:
    """A collection of EvalCases for a skill."""

    name: str
    skill_id: str
    cases: list[EvalCase] = field(default_factory=list)
    version: str = "1.0.0"

    def add_case(self, case: EvalCase) -> None:
        self.cases.append(case)


class EvalRunner:
    """Runs an EvalSet against a Skill and computes metrics."""

    def __init__(self, registry: Any) -> None:
        self.registry = registry

    async def run(self, eval_set: EvalSet) -> dict[str, Any]:
        """Execute all cases in the eval set, return metrics."""
        from app.skills.models import SkillInput

        skill = self.registry.get(eval_set.skill_id)
        if not skill:
            return {"error": f"Skill {eval_set.skill_id} not found"}

        results: list[EvalResult] = []
        for case in eval_set.cases:
            si = SkillInput(user_message=case.input_message)
            try:
                record = await skill.run(si)
                output = record.output.content
                latency = record.execution_time_ms

                # Check expected contains
                passed = True
                reason = ""
                for needle in case.expected_contains:
                    if needle not in output:
                        passed = False
                        reason = f"Missing expected: {needle}"
                        break

                if passed:
                    for needle in case.expected_not_contains:
                        if needle in output:
                            passed = False
                            reason = f"Contains forbidden: {needle}"
                            break

                results.append(EvalResult(
                    case_id=case.id, passed=passed, reason=reason,
                    output=output, latency_ms=latency,
                ))
            except Exception as e:
                results.append(EvalResult(
                    case_id=case.id, passed=False, reason=str(e),
                ))

        passed = sum(1 for r in results if r.passed)
        total = len(results)
        avg_latency = sum(r.latency_ms for r in results) / total if total else 0

        return {
            "eval_set": eval_set.name,
            "skill_id": eval_set.skill_id,
            "version": eval_set.version,
            "total": total,
            "passed": passed,
            "failed": total - passed,
            "pass_rate": passed / total if total else 0,
            "avg_latency_ms": int(avg_latency),
            "failures": [
                {"case_id": r.case_id, "reason": r.reason}
                for r in results if not r.passed
            ],
        }


# ============================================================
# Auto-eval generation: build eval cases from examples
# ============================================================


def generate_eval_set_from_examples(
    skill_id: str,
    examples: list[dict[str, Any]],
) -> EvalSet:
    """Auto-generate an EvalSet from example input/output pairs."""
    eval_set = EvalSet(name=f"{skill_id}-auto", skill_id=skill_id)
    for i, ex in enumerate(examples):
        case = EvalCase(
            id=f"auto-{i}",
            input_message=ex.get("input", ""),
            expected_contains=ex.get("expected_contains", []),
            expected_not_contains=ex.get("expected_not_contains", []),
        )
        eval_set.add_case(case)
    return eval_set
