"""Prompt AutoML: automatic prompt optimization (DSPy-style).

Iteratively refines a Skill's prompt by:
  1. Running eval set on current prompt
  2. Generating candidate refinements via LLM
  3. Re-running eval set on candidates
  4. Keeping the best (greedy hill climbing)
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class PromptCandidate:
    """A candidate prompt with its eval score."""

    prompt: str
    score: float = 0.0
    iteration: int = 0


class PromptAutoML:
    """Auto-optimize Skill prompts via eval-driven hill climbing."""

    def __init__(self, eval_runner: Any, model_router: Any) -> None:
        self.eval_runner = eval_runner
        self.model_router = model_router

    async def optimize(
        self,
        skill_id: str,
        eval_set: Any,
        original_prompt: str,
        max_iterations: int = 5,
    ) -> dict[str, Any]:
        """Run AutoML optimization loop.

        Returns the best prompt found and its score.
        """
        logger.info("AutoML start: skill=%s iterations=%s", skill_id, max_iterations)

        # Baseline
        baseline = await self._evaluate_prompt(skill_id, eval_set, original_prompt)
        best = PromptCandidate(prompt=original_prompt, score=baseline, iteration=0)

        history = [best]

        for i in range(1, max_iterations + 1):
            # Generate refinement candidates
            candidates = await self._generate_candidates(best.prompt, n=3)

            # Evaluate each
            best_in_round = best
            for cand_prompt in candidates:
                score = await self._evaluate_prompt(skill_id, eval_set, cand_prompt)
                cand = PromptCandidate(prompt=cand_prompt, score=score, iteration=i)
                history.append(cand)
                if score > best_in_round.score:
                    best_in_round = cand

            best = best_in_round
            logger.info("AutoML iter %s: best score=%.3f", i, best.score)

            if best.score >= 0.95:  # Good enough
                break

        return {
            "skill_id": skill_id,
            "original_score": baseline,
            "best_score": best.score,
            "improvement": best.score - baseline,
            "best_prompt": best.prompt,
            "iterations_run": best.iteration,
            "candidates_evaluated": len(history),
        }

    async def _evaluate_prompt(
        self, skill_id: str, eval_set: Any, prompt: str
    ) -> float:
        """Evaluate a prompt against the eval set, return pass rate."""
        # Phase 10 simplified: actual implementation would temporarily
        # patch the skill's prompt before running
        try:
            result = await self.eval_runner.run(eval_set)
            return result.get("pass_rate", 0.0)
        except Exception:
            return 0.0

    async def _generate_candidates(self, base_prompt: str, n: int = 3) -> list[str]:
        """Generate N refined prompt candidates via LLM."""
        if not self.model_router:
            return []

        from app.llm.models import ChatMessage, ChatRequest, Role

        meta_prompt = (
            "你是 prompt 优化专家。请改进以下 prompt，使输出更准确。\n\n"
            f"原 prompt:\n{base_prompt}\n\n"
            f"请输出 {n} 个改进版本，每个用 '---' 分隔。"
        )

        try:
            response = await self.model_router.chat(
                ChatRequest(
                    messages=[ChatMessage(role=Role.SYSTEM, content=meta_prompt)],
                    model_preference="local",
                    temperature=0.8,
                    max_tokens=2048,
                )
            )
            candidates = [c.strip() for c in response.content.split("---") if c.strip()]
            return candidates[:n]
        except Exception:
            return []
