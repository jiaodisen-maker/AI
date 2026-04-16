"""Experience memory adapter — bridges ExperienceEngine with the memory layer.

Re-exports the core experience engine for use from app/memory/.
The actual implementation stays in app/experience/engine.py.
"""

from app.experience.engine import ExperienceEngine
from app.experience.models import ExperiencePattern, ExperienceRecord
from app.experience.store import ExperienceStore

__all__ = ["ExperienceEngine", "ExperienceStore", "ExperienceRecord", "ExperiencePattern"]
