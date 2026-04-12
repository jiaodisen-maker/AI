"""Experience Graph: time-series knowledge graph of skill execution patterns.

Inspired by Graphiti/Zep — every experience pattern is a node in a graph
with temporal validity. Patterns can be related (similar, contradicts, refines).
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class ExperienceNode:
    """A node in the experience graph (typically a learned pattern)."""

    id: str
    skill_id: str
    pattern: str
    confidence: float
    valid_from: datetime
    valid_until: datetime | None = None  # None = currently valid
    superseded_by: str | None = None
    tags: list[str] = field(default_factory=list)


@dataclass
class ExperienceEdge:
    """An edge between experience nodes."""

    source_id: str
    target_id: str
    edge_type: str  # similar / contradicts / refines / supersedes
    weight: float = 1.0


class ExperienceGraph:
    """In-memory experience graph with temporal validity tracking.

    Phase 5 implementation: in-memory.
    Phase 6+ migration: Neo4j with Graphiti-style temporal model.
    """

    def __init__(self) -> None:
        self._nodes: dict[str, ExperienceNode] = {}
        self._edges: list[ExperienceEdge] = []

    def add_node(self, node: ExperienceNode) -> None:
        self._nodes[node.id] = node
        logger.info("Experience node added: %s [%s]", node.id, node.skill_id)

    def supersede(self, old_id: str, new_id: str) -> None:
        """Mark an old pattern as superseded by a new one."""
        old = self._nodes.get(old_id)
        if old:
            old.valid_until = datetime.now()
            old.superseded_by = new_id
            self._edges.append(
                ExperienceEdge(
                    source_id=new_id, target_id=old_id, edge_type="supersedes"
                )
            )

    def get_active_patterns(self, skill_id: str) -> list[ExperienceNode]:
        """Get currently valid patterns for a skill."""
        return [
            n
            for n in self._nodes.values()
            if n.skill_id == skill_id and n.valid_until is None
        ]

    def get_history(self, skill_id: str) -> list[ExperienceNode]:
        """Get full history (including superseded) for a skill."""
        return sorted(
            [n for n in self._nodes.values() if n.skill_id == skill_id],
            key=lambda n: n.valid_from,
        )

    def find_related(self, node_id: str) -> list[tuple[ExperienceNode, str]]:
        """Find nodes related to a given node."""
        related = []
        for edge in self._edges:
            if edge.source_id == node_id:
                target = self._nodes.get(edge.target_id)
                if target:
                    related.append((target, edge.edge_type))
            elif edge.target_id == node_id:
                source = self._nodes.get(edge.source_id)
                if source:
                    related.append((source, f"reverse_{edge.edge_type}"))
        return related

    def stats(self) -> dict[str, Any]:
        active = sum(1 for n in self._nodes.values() if n.valid_until is None)
        return {
            "total_nodes": len(self._nodes),
            "active_nodes": active,
            "superseded_nodes": len(self._nodes) - active,
            "edges": len(self._edges),
        }
