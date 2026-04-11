"""Experience Engine: the core differentiator.

Records skill executions, extracts patterns from human corrections,
and injects accumulated experience into future skill runs.

This is what makes skills get better over time.
"""

from __future__ import annotations

import json
import logging
import uuid

from app.experience.models import ExperiencePattern, ExperienceRecord
from app.experience.store import ExperienceStore
from app.llm.models import ChatMessage, ChatRequest, Role
from app.llm.router import ModelRouter

logger = logging.getLogger(__name__)

DIFF_EXTRACTION_PROMPT = """\
你是一个经验提取引擎。比较 AI 原始输出和人工修改后的版本，提取可复用的规则。

AI 原始输出：
{ai_output}

人工修改后：
{human_edited}

请提取修改 pattern（可复用的规则），以 JSON 数组格式返回：
[
  {{
    "pattern": "简短描述这个规则",
    "description": "详细解释为什么要这样改",
    "example_before": "修改前的片段",
    "example_after": "修改后的片段"
  }}
]

只提取通用的、可复用的规则，不要提取内容相关的具体修改。
如果没有可提取的通用规则，返回空数组 []。"""


class ExperienceEngine:
    """The self-evolution engine.

    Core loop:
    1. record_execution() — save every skill run
    2. learn_from_correction() — when human edits AI output, extract patterns
    3. get_experience_prompt() — inject reliable patterns into future prompts
    4. Confidence management — patterns gain/lose trust based on outcomes
    """

    def __init__(self, store: ExperienceStore, model_router: ModelRouter) -> None:
        self.store = store
        self.model_router = model_router

    async def record_execution(
        self,
        skill_id: str,
        input_context: dict,
        ai_output: str,
        model_used: str = "",
    ) -> str:
        """Record a skill execution (before human review)."""
        record = ExperienceRecord(
            id=uuid.uuid4().hex,
            skill_id=skill_id,
            input_context=input_context,
            ai_output=ai_output,
            model_used=model_used,
        )
        return await self.store.add_record(record)

    async def learn_from_correction(
        self,
        record_id: str,
        skill_id: str,
        ai_output: str,
        human_edited: str,
        input_context: dict | None = None,
    ) -> list[ExperiencePattern]:
        """When a human corrects AI output, extract learnable patterns.

        This is the heart of the experience engine: turning human corrections
        into reusable knowledge.
        """
        if ai_output == human_edited:
            return []  # No correction, nothing to learn

        # Use LLM to extract patterns from the diff
        request = ChatRequest(
            messages=[
                ChatMessage(
                    role=Role.SYSTEM,
                    content=DIFF_EXTRACTION_PROMPT.format(
                        ai_output=ai_output[:2000],
                        human_edited=human_edited[:2000],
                    ),
                ),
            ],
            model_preference="local",
            temperature=0.1,
            max_tokens=1024,
        )

        try:
            response = await self.model_router.chat(request)
            raw_patterns = self._parse_patterns(response.content)
        except Exception as e:
            logger.error("Pattern extraction failed: %s", e)
            return []

        # Store extracted patterns, merging with existing similar patterns
        new_patterns = []
        for raw in raw_patterns:
            existing = self._find_similar_pattern(skill_id, raw["pattern"])
            if existing:
                # Reinforce existing pattern
                existing.usage_count += 1
                existing.confidence = min(1.0, existing.confidence + 0.1)
                existing.examples.append({
                    "before": raw.get("example_before", ""),
                    "after": raw.get("example_after", ""),
                })
                # Keep only last 10 examples
                existing.examples = existing.examples[-10:]
                await self.store.update_pattern(existing)
                new_patterns.append(existing)
            else:
                # Create new pattern
                pattern = ExperiencePattern(
                    id=uuid.uuid4().hex,
                    skill_id=skill_id,
                    pattern=raw["pattern"],
                    description=raw.get("description", ""),
                    examples=[{
                        "before": raw.get("example_before", ""),
                        "after": raw.get("example_after", ""),
                    }],
                    confidence=0.3,
                )
                await self.store.add_pattern(pattern)
                new_patterns.append(pattern)

        # Update the original record
        record = ExperienceRecord(
            id=record_id,
            skill_id=skill_id,
            input_context=input_context or {},
            ai_output=ai_output,
            human_edited_output=human_edited,
            extracted_patterns=[p.pattern for p in new_patterns],
        )
        await self.store.add_record(record)

        return new_patterns

    def get_experience_prompt(self, skill_id: str) -> str:
        """Generate a prompt supplement with reliable experience patterns.

        Only injects patterns with confidence >= 0.7.
        This is what makes the AI output improve over time.
        """
        patterns = self.store.get_reliable_patterns(skill_id)
        if not patterns:
            return ""

        lines = ["基于历史经验，请注意以下规则："]
        for p in patterns:
            lines.append(f"- {p.pattern}")
            if p.description:
                lines.append(f"  说明：{p.description}")
            if p.examples:
                latest = p.examples[-1]
                if latest.get("before") and latest.get("after"):
                    lines.append(f"  例：「{latest['before']}」→「{latest['after']}」")

        return "\n".join(lines)

    def get_stats(self, skill_id: str) -> dict:
        """Get experience statistics for a skill."""
        all_patterns = self.store.get_all_patterns(skill_id)
        reliable = [p for p in all_patterns if p.is_reliable]
        records = self.store.get_records(skill_id, limit=1000)
        edited = [r for r in records if r.was_edited]

        return {
            "total_executions": len(records),
            "human_corrections": len(edited),
            "correction_rate": len(edited) / len(records) if records else 0,
            "total_patterns": len(all_patterns),
            "reliable_patterns": len(reliable),
            "experience_prompt_length": len(self.get_experience_prompt(skill_id)),
        }

    def _find_similar_pattern(self, skill_id: str, pattern_text: str) -> ExperiencePattern | None:
        """Find an existing pattern that's similar to the new one."""
        # Simple text similarity: if >60% of words overlap, consider similar
        new_words = set(pattern_text.lower().split())
        for existing in self.store.get_all_patterns(skill_id):
            existing_words = set(existing.pattern.lower().split())
            if not new_words or not existing_words:
                continue
            overlap = len(new_words & existing_words) / max(len(new_words), len(existing_words))
            if overlap > 0.6:
                return existing
        return None

    def _parse_patterns(self, content: str) -> list[dict]:
        """Parse LLM response into pattern dicts."""
        content = content.strip()
        if content.startswith("```"):
            content = content.split("\n", 1)[-1]
        if content.endswith("```"):
            content = content.rsplit("```", 1)[0]
        content = content.strip()

        try:
            data = json.loads(content)
            if isinstance(data, list):
                return data
        except (json.JSONDecodeError, TypeError) as e:
            logger.warning("Failed to parse patterns: %s", e)

        return []
