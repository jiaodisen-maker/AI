"""Tests for Phase 5-10."""

import pytest

# ============================================================
# Phase 5: Plugin Discovery + A2A + Experience Graph
# ============================================================


def test_plugin_discovery():
    from app.skills.discovery import PluginDiscovery
    from app.skills.registry import SkillRegistry

    registry = SkillRegistry()
    discovery = PluginDiscovery(registry)
    count = discovery.discover_all()
    assert count >= 0


def test_yaml_skill():
    from app.skills.yaml_skill import YAMLSkill

    skill_def = {
        "id": "test-yaml",
        "name": "Test YAML",
        "description": "test",
        "category": "content",
        "triggers": ["yaml-test"],
        "prompt_template": "Test: {user_message}",
    }
    skill = YAMLSkill(skill_def)
    assert skill.meta().id == "test-yaml"
    assert "yaml-test" in skill.meta().triggers


def test_experience_graph():
    from datetime import datetime

    from app.experience.graph import ExperienceGraph, ExperienceNode

    graph = ExperienceGraph()
    node = ExperienceNode(
        id="n1", skill_id="test", pattern="test pattern",
        confidence=0.8, valid_from=datetime.now(),
    )
    graph.add_node(node)

    active = graph.get_active_patterns("test")
    assert len(active) == 1
    assert graph.stats()["active_nodes"] == 1


# ============================================================
# Phase 6: Skill Factory + Eval Set + A/B Test
# ============================================================


def test_skill_factory_templates():
    from app.skills.factory import SkillFactory

    templates = SkillFactory.list_templates()
    assert "content_writer" in templates
    assert "data_analyst" in templates


def test_skill_factory_from_template():
    from app.skills.factory import SkillFactory

    factory = SkillFactory()
    skill = factory.from_template(
        skill_id="custom-writer",
        name="Custom Writer",
        description="A custom writer",
        template="content_writer",
        params={
            "role": "营销文案专家",
            "instructions": "写吸引人的营销文案",
            "output_format": "200字以内",
        },
        triggers=["写营销文案"],
    )
    assert skill.meta().id == "custom-writer"
    assert skill.meta().category == "content"


def test_skill_factory_from_examples():
    from app.skills.factory import SkillFactory

    factory = SkillFactory()
    skill = factory.from_examples(
        skill_id="few-shot",
        name="Few Shot",
        description="few-shot learning",
        examples=[
            {"input": "苹果", "output": "水果"},
            {"input": "胡萝卜", "output": "蔬菜"},
        ],
        triggers=["分类"],
    )
    assert skill.meta().id == "few-shot"


def test_eval_set():
    from app.evals import EvalCase, EvalSet

    eval_set = EvalSet(name="test", skill_id="test-skill")
    case = EvalCase(
        id="c1",
        input_message="hello",
        expected_contains=["hi"],
    )
    eval_set.add_case(case)
    assert len(eval_set.cases) == 1


def test_ab_test_sticky_assignment():
    from app.experiments import ABTest, Variant

    test = ABTest(
        test_id="t1",
        skill_id="test",
        variants=[
            Variant(id="A", name="A", weight=0.5),
            Variant(id="B", name="B", weight=0.5),
        ],
    )

    # Same user always gets same variant
    v1 = test.get_variant_for_user("user1")
    v2 = test.get_variant_for_user("user1")
    assert v1.id == v2.id


def test_ab_test_metrics():
    from app.experiments import ABTest, Variant

    test = ABTest(
        test_id="t1", skill_id="test",
        variants=[Variant(id="A", name="A"), Variant(id="B", name="B")],
    )
    test.record_result("A", "u1", success=True)
    test.record_result("A", "u2", success=True)
    test.record_result("B", "u3", success=False)

    metrics = test.get_metrics()
    assert metrics["variants"]["A"]["success_rate"] == 1.0
    assert metrics["variants"]["B"]["success_rate"] == 0.0


# ============================================================
# Phase 7: Meta-learning + Optimizer + Healing
# ============================================================


def test_meta_analyzer():
    from app.meta.analyzer import MetaAnalyzer

    analyzer = MetaAnalyzer()
    sequences = analyzer.analyze_skill_sequences()
    assert isinstance(sequences, list)


def test_skill_optimizer():
    from app.meta.optimizer import SkillOptimizer

    optimizer = SkillOptimizer()
    health = optimizer.analyze_skill_health("any-skill")
    # No store → returns error, that's OK
    assert "error" in health or "skill_id" in health


def test_healing_detector():
    from app.meta.healing import HealingDetector

    detector = HealingDetector()

    # Healthy skill
    for _ in range(10):
        detector.record("skill-a", success=True, latency_ms=100)
    assert detector.is_skill_available("skill-a") is True
    assert detector.get_status("skill-a")["status"] == "healthy"

    # Failing skill
    for _ in range(5):
        detector.record("skill-b", success=False, latency_ms=100)
    assert detector.is_skill_available("skill-b") is False
    assert detector.get_status("skill-b")["status"] == "disabled"


# ============================================================
# Phase 8: Multimodal
# ============================================================


@pytest.mark.asyncio
async def test_image_processor():
    from app.multimodal import ImageProcessor

    proc = ImageProcessor()
    result = await proc.describe("/tmp/nonexistent.jpg")
    assert "失败" in result or "待" in result


@pytest.mark.asyncio
async def test_document_processor():
    from app.multimodal import DocumentProcessor

    result = await DocumentProcessor.parse_pdf("/tmp/nonexistent.pdf")
    assert "PDF" in result or "失败" in result


def test_visual_qa_meta():
    from app.skills.builtin.visual_qa import VisualQASkill

    class MockRouter:
        pass

    skill = VisualQASkill(MockRouter())
    assert skill.meta().id == "visual-qa"


# ============================================================
# Phase 9: Multi-tenant + Federation
# ============================================================


def test_tenant_manager():
    from app.federation import TenantManager

    tm = TenantManager()
    # Default tenant exists
    default = tm.get_tenant("default")
    assert default is not None
    assert default.name == "默认租户"


def test_create_tenant():
    from app.federation import TenantManager

    tm = TenantManager()
    tenant = tm.create_tenant("acme", "Acme Corp")
    assert tenant.id == "acme"
    assert tm.get_tenant("acme") is not None


def test_tenant_skill_enabled():
    from app.federation import TenantManager

    tm = TenantManager()
    tm.create_tenant(
        "limited",
        "Limited",
        enabled_skills=["compliant-copy"],
    )
    assert tm.is_skill_enabled("limited", "compliant-copy") is True
    assert tm.is_skill_enabled("limited", "data-query") is False
    # Default tenant: all enabled
    assert tm.is_skill_enabled("default", "any-skill") is True


def test_namespaced_keys():
    from app.federation import TenantManager

    tm = TenantManager()
    key = tm.get_namespaced_key("acme", "session:123")
    assert key.startswith("tenant:acme:")


def test_mcp_federation():
    from app.federation import MCPFederation
    from app.federation.mcp_federation import FederatedPeer

    fed = MCPFederation()
    peer = FederatedPeer(
        name="subsidiary-1",
        url="http://10.0.0.5:8080",
        api_key="key123",
        trust_level="read",
    )
    fed.add_peer(peer)
    assert fed.peer_count == 1


# ============================================================
# Phase 10: AutoML + RL + Self-Improve
# ============================================================


def test_rl_feedback():
    from app.evolution.rl_feedback import RLFeedback

    rl = RLFeedback()
    rl.record_feedback("test-skill", "u1", "output", edited_output=None)
    rl.record_feedback("test-skill", "u2", "output", rejected=True)

    avg = rl.get_skill_reward_avg("test-skill")
    assert avg == 0.0  # +1.0 + -1.0 = 0


def test_rl_feedback_edit():
    from app.evolution.rl_feedback import RLFeedback

    rl = RLFeedback()
    output = "这是一篇胶原蛋白小红书文案"
    # Identical (None means no edit, treat as accepted) → +1.0
    r1 = rl.record_feedback("test", "u1", output, edited_output=output)
    assert r1 == 1.0
    # Different content → negative reward
    r2 = rl.record_feedback("test", "u2", output, edited_output="完全不同的内容")
    assert r2 < 1.0


def test_rl_top_skills():
    from app.evolution.rl_feedback import RLFeedback

    rl = RLFeedback()
    rl.record_feedback("good-skill", "u1", "out")
    rl.record_feedback("bad-skill", "u1", "out", rejected=True)

    top = rl.get_top_skills(n=2)
    assert top[0][0] == "good-skill"


@pytest.mark.asyncio
async def test_self_improve_loop():
    from app.evolution.self_improve import SelfImproveLoop

    loop = SelfImproveLoop()
    report = await loop.run_cycle()
    assert report.timestamp is not None
    # No registry → 0 analyzed
    assert report.skills_analyzed == 0
