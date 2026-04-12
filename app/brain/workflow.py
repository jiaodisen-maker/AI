"""SOP Workflow Engine — driven by ontology workflows.yaml.

Executes multi-step business processes with mixed
deterministic (rules) + probabilistic (LLM) steps.

Each workflow step specifies:
  - role: which agent handles this step
  - type: deterministic / probabilistic / human_approval
  - skill: which Skill to call (if any)
  - gate: condition to proceed to next step
"""

from __future__ import annotations

import logging
from typing import Any

from app.skills.models import SkillInput
from app.skills.registry import SkillRegistry

logger = logging.getLogger(__name__)


class WorkflowEngine:
    """Executes SOP workflows defined in ontology/definitions/workflows.yaml.

    Each workflow is a sequence of steps. Each step:
    1. Finds the responsible role agent (or uses coordinator)
    2. If step has a skill, calls that Skill through full lifecycle
    3. If step is human_approval, pauses and notifies
    4. If step has a gate, checks before proceeding
    """

    def __init__(
        self,
        skill_registry: SkillRegistry,
        ontology_service: Any = None,
    ) -> None:
        self.skill_registry = skill_registry
        self.ontology_service = ontology_service

    async def execute_workflow(
        self,
        workflow_name: str,
        initial_context: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Execute a named workflow from the ontology.

        Returns execution result with per-step outcomes.
        """
        if not self.ontology_service:
            return {"error": "本体服务未初始化"}

        workflow = self.ontology_service.query_workflow(workflow_name)
        if "error" in workflow:
            return workflow

        steps = workflow.get("steps", [])
        if not steps:
            return {"error": f"工作流 '{workflow_name}' 没有步骤"}

        context = dict(initial_context or {})
        results = []

        logger.info("Starting workflow: %s (%d steps)", workflow_name, len(steps))

        for step in steps:
            step_result = await self._execute_step(step, context)
            results.append(step_result)

            # Check gate condition
            if step_result.get("blocked"):
                logger.warning(
                    "Workflow %s blocked at step %s: %s",
                    workflow_name,
                    step.get("id", "?"),
                    step_result.get("reason", "unknown"),
                )
                break

            # Pass output to next step's context
            if step_result.get("output"):
                context[f"step_{step.get('id', len(results))}_output"] = (
                    step_result["output"]
                )

        return {
            "workflow": workflow_name,
            "steps_total": len(steps),
            "steps_completed": len(results),
            "blocked": results[-1].get("blocked", False) if results else False,
            "results": results,
        }

    async def _execute_step(
        self,
        step: dict[str, Any],
        context: dict[str, Any],
    ) -> dict[str, Any]:
        """Execute a single workflow step."""
        step_id = step.get("id", 0)
        step_type = step.get("type", "deterministic")
        skill_id = step.get("skill", "")
        role = step.get("role", "")
        action = step.get("action", "")
        condition = step.get("condition", "")
        gate = step.get("gate", "")

        logger.info(
            "Step %s [%s] role=%s action=%s",
            step_id, step_type, role, action,
        )

        # Check condition (if step has a condition, evaluate it)
        if condition:
            # Simple condition evaluation against context
            if not self._evaluate_condition(condition, context):
                return {
                    "step_id": step_id,
                    "status": "skipped",
                    "reason": f"条件不满足: {condition}",
                    "output": None,
                }

        # Execute based on step type
        if step_type == "human_approval":
            return {
                "step_id": step_id,
                "status": "pending_approval",
                "role": role,
                "action": action,
                "blocked": True,
                "reason": f"等待 {role} 审批",
                "output": None,
            }

        if skill_id:
            # Call Skill through full lifecycle
            skill = self.skill_registry.get(skill_id)
            if not skill:
                return {
                    "step_id": step_id,
                    "status": "error",
                    "reason": f"Skill '{skill_id}' 未找到",
                    "output": None,
                }

            skill_input = SkillInput(
                user_message=action,
                context=context,
            )

            try:
                record = await skill.run(skill_input)
                output = (
                    record.output.content
                    if record.output.success
                    else record.output.error
                )

                # Check gate
                if gate and not record.output.success:
                    return {
                        "step_id": step_id,
                        "status": "blocked",
                        "blocked": True,
                        "reason": f"门控未通过: {gate}",
                        "output": output,
                    }

                return {
                    "step_id": step_id,
                    "status": "completed",
                    "type": step_type,
                    "skill_id": skill_id,
                    "output": output,
                    "execution_time_ms": record.execution_time_ms,
                }
            except Exception as e:
                return {
                    "step_id": step_id,
                    "status": "error",
                    "reason": str(e),
                    "output": None,
                }

        # No skill — just a descriptive step
        return {
            "step_id": step_id,
            "status": "completed",
            "type": step_type,
            "role": role,
            "action": action,
            "output": action,
        }

    @staticmethod
    def _evaluate_condition(condition: str, context: dict) -> bool:
        """Simple condition evaluation.

        Supports: "key == 'value'" style conditions against context.
        """
        try:
            # Very basic: check if condition references a context key
            for key, value in context.items():
                if key in condition and str(value) in condition:
                    return True
            # Default: condition not met
            return False
        except Exception:
            return True  # If we can't evaluate, proceed
