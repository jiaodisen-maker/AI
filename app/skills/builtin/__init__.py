"""Built-in skills shipped with the platform."""

from app.skills.builtin.competitor_watch import CompetitorWatchSkill
from app.skills.builtin.compliant_copy import CompliantCopySkill
from app.skills.builtin.content_adapt import ContentAdaptSkill
from app.skills.builtin.data_query import DataQuerySkill
from app.skills.builtin.report_gen import ReportGenSkill
from app.skills.builtin.web_search import WebSearchSkill

__all__ = [
    "CompliantCopySkill",
    "CompetitorWatchSkill",
    "ContentAdaptSkill",
    "DataQuerySkill",
    "ReportGenSkill",
    "WebSearchSkill",
]
