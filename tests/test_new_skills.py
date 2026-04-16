"""Tests for the 5 new built-in Skills."""

from app.skills.builtin.competitor_watch import CompetitorWatchSkill
from app.skills.builtin.content_adapt import ContentAdaptSkill
from app.skills.builtin.data_query import DataQuerySkill
from app.skills.builtin.report_gen import ReportGenSkill
from app.skills.builtin.web_search import WebSearchSkill
from app.skills.registry import SkillRegistry


class MockRouter:
    pass


def test_data_query_meta():
    skill = DataQuerySkill(MockRouter())
    meta = skill.meta()
    assert meta.id == "data-query"
    assert "查数据" in meta.triggers
    assert meta.category == "data"


def test_data_query_ontology_needs():
    skill = DataQuerySkill(MockRouter())
    needs = skill.ontology_needs()
    assert "data_definitions" in needs


def test_report_gen_meta():
    skill = ReportGenSkill(MockRouter())
    meta = skill.meta()
    assert meta.id == "report-gen"
    assert "写报告" in meta.triggers or "周报" in meta.triggers


def test_report_gen_ontology_needs():
    skill = ReportGenSkill(MockRouter())
    needs = skill.ontology_needs()
    assert "data_definitions" in needs
    assert "goals" in needs


def test_web_search_meta():
    skill = WebSearchSkill(MockRouter())
    meta = skill.meta()
    assert meta.id == "web-search"
    assert "搜索" in meta.triggers


def test_competitor_watch_meta():
    skill = CompetitorWatchSkill(MockRouter())
    meta = skill.meta()
    assert meta.id == "competitor-watch"
    assert "竞品" in meta.triggers


def test_competitor_watch_ontology_needs():
    skill = CompetitorWatchSkill(MockRouter())
    assert "health_supplements" in skill.ontology_needs()


def test_content_adapt_meta():
    skill = ContentAdaptSkill(MockRouter())
    meta = skill.meta()
    assert meta.id == "content-adapt"
    assert "适配" in meta.triggers or "多平台" in meta.triggers


def test_all_skills_register():
    """All 6 skills can register in the registry without conflict."""
    registry = SkillRegistry()
    router = MockRouter()
    from app.skills.builtin.compliant_copy import CompliantCopySkill

    registry.register(CompliantCopySkill(router))
    registry.register(DataQuerySkill(router))
    registry.register(ReportGenSkill(router))
    registry.register(WebSearchSkill(router))
    registry.register(CompetitorWatchSkill(router))
    registry.register(ContentAdaptSkill(router))

    assert registry.count == 6

    # Each has unique ID
    ids = [m.id for m in registry.list_all()]
    assert len(set(ids)) == 6


def test_trigger_routing_no_conflicts():
    """Different skills should not have overlapping trigger words."""
    registry = SkillRegistry()
    router = MockRouter()
    from app.skills.builtin.compliant_copy import CompliantCopySkill

    registry.register(CompliantCopySkill(router))
    registry.register(DataQuerySkill(router))
    registry.register(ReportGenSkill(router))
    registry.register(WebSearchSkill(router))
    registry.register(CompetitorWatchSkill(router))
    registry.register(ContentAdaptSkill(router))

    # Each trigger phrase should map to a specific skill
    assert registry.find_by_trigger("写文案").meta().id == "compliant-copy"
    assert registry.find_by_trigger("查数据").meta().id == "data-query"
    assert registry.find_by_trigger("写报告").meta().id == "report-gen"
    assert registry.find_by_trigger("搜索最新").meta().id == "web-search"
    assert registry.find_by_trigger("竞品分析").meta().id == "competitor-watch"
    assert registry.find_by_trigger("适配多平台").meta().id == "content-adapt"
