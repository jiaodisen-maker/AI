"""
SKILL.md 文件系统加载器

对齐 Anthropic 开放标准：
  ---
  name: skill-name
  description: ...
  triggers: [a, b, c]
  ---
  # Markdown 内容...

支持：
- 目录扫描（递归）
- YAML frontmatter 解析
- 缓存 + 文件 mtime 自动失效
"""
from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from pathlib import Path

import yaml

from ..ports import SkillPort
from ..types import Skill

logger = logging.getLogger(__name__)


# ============================================================
# 内部缓存项
# ============================================================
@dataclass
class _CachedSkill:
    skill: Skill
    file_mtime: float
    loaded_at: float


# ============================================================
# 加载器
# ============================================================
class FilesystemSkillLoader(SkillPort):
    """从本地目录加载 SKILL.md"""

    def __init__(self, default_dirs: list[Path] | None = None):
        self._cache: dict[str, _CachedSkill] = {}
        self._dirs: set[Path] = set()
        if default_dirs:
            for d in default_dirs:
                self._dirs.add(Path(d))

    async def load_skills(self, source: str) -> int:
        """从目录加载（source 是目录路径）"""
        path = Path(source)
        if not path.exists():
            logger.warning(f"Skill source does not exist: {source}")
            return 0
        self._dirs.add(path)

        loaded = 0
        for skill_md in path.rglob("SKILL.md"):
            try:
                skill = self._parse_skill_md(skill_md)
                if skill:
                    self._cache[skill.name] = _CachedSkill(
                        skill=skill,
                        file_mtime=skill_md.stat().st_mtime,
                        loaded_at=time.time(),
                    )
                    loaded += 1
            except Exception as e:
                logger.error(f"Failed to parse {skill_md}: {e}")

        logger.info(f"Loaded {loaded} skills from {source}")
        return loaded

    async def list_skills(self) -> list[Skill]:
        await self._refresh_changed()
        return [c.skill for c in self._cache.values()]

    async def get_skill(self, name: str) -> Skill | None:
        await self._refresh_changed()
        cached = self._cache.get(name)
        return cached.skill if cached else None

    async def get_skills_prompt(self, skill_names: list[str] | None = None) -> str:
        """生成 system prompt 注入"""
        await self._refresh_changed()
        if skill_names:
            skills = [self._cache[n].skill for n in skill_names if n in self._cache]
        else:
            skills = [c.skill for c in self._cache.values()]

        if not skills:
            return ""

        lines = ["可用的 Skill 列表："]
        for s in skills:
            triggers_str = ", ".join(s.triggers) if s.triggers else "（无）"
            lines.append(f"- {s.name}: {s.description} [触发词: {triggers_str}]")
        return "\n".join(lines)

    async def match_skill(self, msg: str) -> Skill | None:
        """触发词匹配（优先精确匹配）"""
        await self._refresh_changed()
        msg_lower = msg.lower()
        best: tuple[int, Skill] | None = None

        for cached in self._cache.values():
            skill = cached.skill
            score = 0
            for trigger in skill.triggers:
                if trigger.lower() in msg_lower:
                    score += len(trigger)  # 长触发词权重更高

            if score > 0 and (best is None or score > best[0]):
                best = (score, skill)

        return best[1] if best else None

    # ========================================================
    # 内部辅助
    # ========================================================
    async def _refresh_changed(self) -> None:
        """检查目录中文件 mtime 变化，自动重载"""
        for d in list(self._dirs):
            if not d.exists():
                continue
            for skill_md in d.rglob("SKILL.md"):
                try:
                    mtime = skill_md.stat().st_mtime
                except OSError:
                    continue
                # 解析名字
                name = self._extract_name(skill_md)
                if not name:
                    continue

                cached = self._cache.get(name)
                if cached is None or cached.file_mtime < mtime:
                    skill = self._parse_skill_md(skill_md)
                    if skill:
                        self._cache[skill.name] = _CachedSkill(
                            skill=skill,
                            file_mtime=mtime,
                            loaded_at=time.time(),
                        )

    @staticmethod
    def _extract_name(path: Path) -> str | None:
        """从 SKILL.md 文件提取 name 字段（不解析全部内容）"""
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            return None
        if not text.startswith("---"):
            return None
        try:
            _, frontmatter, _ = text.split("---", 2)
            data = yaml.safe_load(frontmatter)
            return data.get("name") if isinstance(data, dict) else None
        except Exception:
            return None

    @staticmethod
    def _parse_skill_md(path: Path) -> Skill | None:
        """解析单个 SKILL.md 文件"""
        text = path.read_text(encoding="utf-8")

        if not text.startswith("---"):
            logger.warning(f"{path} 没有 YAML frontmatter")
            return None

        try:
            parts = text.split("---", 2)
            if len(parts) < 3:
                return None
            _, frontmatter, body = parts
            data = yaml.safe_load(frontmatter) or {}
        except Exception as e:
            logger.error(f"YAML parse error in {path}: {e}")
            return None

        if not data.get("name"):
            return None

        return Skill(
            name=data["name"],
            description=data.get("description", ""),
            instructions=body.strip(),
            triggers=list(data.get("triggers") or []),
            parameters=data.get("parameters") or {},
            source_path=str(path),
            updated_at=path.stat().st_mtime,
        )
