"""Role-Based Access Control driven by ontology.

Permissions come from the organization ontology (organization.yaml).
Each role defines: permissions, tools, data_scope.
RBAC checks if a user's role has permission to call a Skill or access data.
"""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


class RBACEngine:
    """Permission checker driven by ontology role definitions."""

    def __init__(self, ontology_service: Any = None) -> None:
        self.ontology_service = ontology_service

    def check_skill_permission(
        self, user_role: str, skill_id: str
    ) -> bool:
        """Check if a role has permission to use a skill.

        Args:
            user_role: Role name from user JWT (e.g. "渠道总监")
            skill_id: Skill ID to check (e.g. "compliant-copy")

        Returns:
            True if allowed, False otherwise.

        Special: "admin" role bypasses all checks.
        """
        if user_role == "admin":
            return True

        if not self.ontology_service:
            return True  # No ontology = no restrictions

        role_def = self.ontology_service.query_role(user_role)
        if "error" in role_def:
            return False

        allowed_tools = role_def.get("tools", [])
        return skill_id in allowed_tools

    def check_data_permission(
        self, user_role: str, data_scope: str
    ) -> bool:
        """Check if a role has permission to access data.

        data_scope is a string like "渠道数据", "全部文案"
        """
        if user_role == "admin":
            return True

        if not self.ontology_service:
            return True

        role_def = self.ontology_service.query_role(user_role)
        if "error" in role_def:
            return False

        allowed_scopes = role_def.get("data_scope", [])
        # Match if any allowed scope is contained in or contains the requested scope
        for scope in allowed_scopes:
            if scope in data_scope or data_scope in scope or scope == "所有渠道数据":
                return True
        return False

    def get_user_permissions(self, user_role: str) -> dict[str, Any]:
        """Return all permissions for a role."""
        if user_role == "admin":
            return {
                "role": "admin",
                "permissions": ["*"],
                "tools": ["*"],
                "data_scope": ["*"],
            }

        if not self.ontology_service:
            return {"role": user_role, "permissions": [], "tools": [], "data_scope": []}

        return self.ontology_service.query_role(user_role)
