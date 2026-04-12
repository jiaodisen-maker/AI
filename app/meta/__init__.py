"""Meta-learning: cross-skill pattern extraction and self-optimization."""

from app.meta.analyzer import MetaAnalyzer
from app.meta.healing import HealingDetector
from app.meta.optimizer import SkillOptimizer

__all__ = ["MetaAnalyzer", "SkillOptimizer", "HealingDetector"]
