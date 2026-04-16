"""Skill Plugin Discovery System.

Auto-discovers Skills from:
  1. Built-in: app/skills/builtin/
  2. User plugins: app/skills/plugins/ (auto-loaded)
  3. External: ~/.zhongtai/skills/ (user-installed)
  4. YAML-defined: skills defined as YAML files (no Python required)
"""

from __future__ import annotations

import importlib.util
import inspect
import logging
from pathlib import Path
from typing import Any

from app.skills.base import BaseSkill
from app.skills.registry import SkillRegistry

logger = logging.getLogger(__name__)


class PluginDiscovery:
    """Discovers and loads Skill plugins from multiple sources."""

    def __init__(self, registry: SkillRegistry, model_router: Any = None) -> None:
        self.registry = registry
        self.model_router = model_router

    def discover_all(self) -> int:
        """Discover and register all Skills from all sources.

        Returns the number of newly discovered skills.
        """
        count = 0
        count += self.discover_builtin()
        count += self.discover_plugins()
        count += self.discover_yaml_skills()
        count += self.discover_external()
        return count

    def discover_builtin(self) -> int:
        """Built-in skills are registered in main.py, this just counts."""
        return 0  # Already registered

    def discover_plugins(self) -> int:
        """Discover Python skill plugins in app/skills/plugins/."""
        plugin_dir = Path(__file__).parent / "plugins"
        if not plugin_dir.exists():
            return 0
        return self._load_python_skills(plugin_dir)

    def discover_external(self) -> int:
        """Discover skills in user's ~/.zhongtai/skills/."""
        external_dir = Path.home() / ".zhongtai" / "skills"
        if not external_dir.exists():
            return 0
        return self._load_python_skills(external_dir)

    def discover_yaml_skills(self) -> int:
        """Discover YAML-defined skills (no Python code required).

        YAML format:
          id: my-skill
          name: 我的技能
          description: ...
          category: content
          triggers: [...]
          prompt_template: |
            你是...
            用户输入: {user_message}
        """
        yaml_dir = Path(__file__).parent / "yaml_skills"
        if not yaml_dir.exists():
            return 0

        import yaml as yaml_lib

        from app.skills.yaml_skill import YAMLSkill

        count = 0
        for yaml_file in yaml_dir.glob("*.yaml"):
            try:
                with open(yaml_file, encoding="utf-8") as f:
                    skill_def = yaml_lib.safe_load(f)
                if skill_def:
                    skill = YAMLSkill(skill_def, self.model_router)
                    self.registry.register(skill)
                    count += 1
            except Exception as e:
                logger.warning("Failed to load %s: %s", yaml_file, e)
        return count

    def _load_python_skills(self, directory: Path) -> int:
        """Load all *.py files in a directory, register BaseSkill subclasses."""
        count = 0
        for py_file in directory.glob("*.py"):
            if py_file.name.startswith("_"):
                continue
            try:
                spec = importlib.util.spec_from_file_location(
                    py_file.stem, py_file
                )
                if not spec or not spec.loader:
                    continue
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if (
                        issubclass(obj, BaseSkill)
                        and obj is not BaseSkill
                        and obj.__module__ == module.__name__
                    ):
                        try:
                            instance = obj(self.model_router)
                            self.registry.register(instance)
                            count += 1
                            logger.info("Loaded plugin skill: %s", name)
                        except Exception as e:
                            logger.warning("Failed to instantiate %s: %s", name, e)
            except Exception as e:
                logger.warning("Failed to load %s: %s", py_file, e)
        return count
