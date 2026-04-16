"""Cross-organization MCP federation.

Allows multiple AI 中台 instances (parent + subsidiaries) to share
Skills via MCP protocol. Each instance exposes its Skills as MCP tools,
remote instances can discover and call them.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

import httpx

logger = logging.getLogger(__name__)


@dataclass
class FederatedPeer:
    """A peer AI 中台 instance in the federation."""

    name: str
    url: str
    api_key: str = ""
    trust_level: str = "read"  # read / write / full
    available_skills: list[str] = field(default_factory=list)


class MCPFederation:
    """Manages federation with peer AI 中台 instances."""

    def __init__(self) -> None:
        self._peers: dict[str, FederatedPeer] = {}
        self._http = httpx.AsyncClient(timeout=10)

    def add_peer(self, peer: FederatedPeer) -> None:
        """Register a federated peer."""
        self._peers[peer.name] = peer
        logger.info("Federated peer added: %s @ %s", peer.name, peer.url)

    async def discover_peer_skills(self, peer_name: str) -> list[dict]:
        """Query a peer's available Skills via MCP."""
        peer = self._peers.get(peer_name)
        if not peer:
            return []
        try:
            resp = await self._http.get(
                f"{peer.url}/api/skills/",
                headers={"Authorization": f"Bearer {peer.api_key}"} if peer.api_key else {},
            )
            data = resp.json()
            skills = data.get("skills", [])
            peer.available_skills = [s["id"] for s in skills]
            return skills
        except Exception as e:
            logger.warning("Failed to discover skills from %s: %s", peer_name, e)
            return []

    async def call_peer_skill(
        self,
        peer_name: str,
        skill_id: str,
        message: str,
    ) -> dict[str, Any]:
        """Execute a skill on a remote peer."""
        peer = self._peers.get(peer_name)
        if not peer:
            return {"error": f"Peer {peer_name} not found"}

        if peer.trust_level == "read":
            return {"error": f"Peer {peer_name} is read-only"}

        try:
            resp = await self._http.post(
                f"{peer.url}/api/skills/{skill_id}/execute",
                json={"message": message},
                headers={"Authorization": f"Bearer {peer.api_key}"} if peer.api_key else {},
            )
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    async def federated_search(
        self, message: str, exclude_local: bool = False
    ) -> list[dict[str, Any]]:
        """Find peers with skills matching the message and call them."""
        results = []
        for peer_name in self._peers:
            try:
                skills = await self.discover_peer_skills(peer_name)
                # Naive matching: any skill triggers
                for skill in skills:
                    triggers = skill.get("triggers", [])
                    if any(t in message for t in triggers):
                        result = await self.call_peer_skill(
                            peer_name, skill["id"], message
                        )
                        results.append({
                            "peer": peer_name,
                            "skill_id": skill["id"],
                            "result": result,
                        })
                        break
            except Exception as e:
                logger.warning("Federated search peer %s failed: %s", peer_name, e)
        return results

    async def close(self) -> None:
        await self._http.aclose()

    @property
    def peer_count(self) -> int:
        return len(self._peers)
