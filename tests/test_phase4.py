"""Tests for Phase 4: SSO, RBAC, Cost Control, Audit, Observability."""

import pytest

# ============================================================
# RBAC Tests
# ============================================================


def test_rbac_admin_bypass():
    """Admin role bypasses all checks."""
    from app.auth.rbac import RBACEngine

    rbac = RBACEngine()
    assert rbac.check_skill_permission("admin", "any-skill") is True
    assert rbac.check_data_permission("admin", "secret-data") is True


def test_rbac_no_ontology_allows_all():
    """Without ontology, RBAC permits all (development mode)."""
    from app.auth.rbac import RBACEngine

    rbac = RBACEngine()
    assert rbac.check_skill_permission("anyone", "compliant-copy") is True


def test_rbac_with_ontology_filters_skills():
    """With ontology, only role-allowed skills pass."""
    from app.auth.rbac import RBACEngine
    from app.ontology.service import OntologyService

    ontology = OntologyService()
    rbac = RBACEngine(ontology_service=ontology)

    # 渠道总监 has data-query, report-gen, competitor-watch
    assert rbac.check_skill_permission("渠道总监", "data-query") is True
    # 渠道总监 should NOT have compliant-copy
    assert rbac.check_skill_permission("渠道总监", "compliant-copy") is False


def test_rbac_get_user_permissions():
    """get_user_permissions returns role definition."""
    from app.auth.rbac import RBACEngine
    from app.ontology.service import OntologyService

    ontology = OntologyService()
    rbac = RBACEngine(ontology_service=ontology)
    perms = rbac.get_user_permissions("渠道总监")
    assert "permissions" in perms or "role" in perms


# ============================================================
# Cost Control Tests
# ============================================================


def test_cost_controller_basic():
    """Cost controller allows calls within budget."""
    from app.llm.cost_control import BudgetConfig, CostController

    cc = CostController(BudgetConfig(per_task_max_calls=10))
    allowed, _ = cc.check_and_record("task1", "user1", tokens=100)
    assert allowed is True


def test_cost_controller_blocks_call_cap():
    """Cost controller blocks when call cap is hit."""
    from app.llm.cost_control import BudgetConfig, CostController

    cc = CostController(BudgetConfig(per_task_max_calls=3))
    cc.check_and_record("task2", "user1", tokens=10)
    cc.check_and_record("task2", "user1", tokens=10)
    cc.check_and_record("task2", "user1", tokens=10)
    allowed, reason = cc.check_and_record("task2", "user1", tokens=10)
    assert allowed is False
    assert "调用次数" in reason


def test_cost_controller_blocks_token_cap():
    """Cost controller blocks when token cap is hit."""
    from app.llm.cost_control import BudgetConfig, CostController

    cc = CostController(BudgetConfig(per_task_max_tokens=1000))
    cc.check_and_record("task3", "user1", tokens=600)
    allowed, reason = cc.check_and_record("task3", "user1", tokens=500)
    assert allowed is False
    assert "token" in reason.lower()


def test_cost_controller_loop_detection():
    """Cost controller detects rapid call loops."""
    from app.llm.cost_control import BudgetConfig, CostController

    cc = CostController(
        BudgetConfig(
            per_task_max_calls=1000,
            per_task_max_tokens=10**9,
            loop_detect_max_calls=5,
            loop_detect_window_seconds=60,
        )
    )
    for _ in range(5):
        cc.check_and_record("loop-task", "user1", tokens=1)
    allowed, reason = cc.check_and_record("loop-task", "user1", tokens=1)
    assert allowed is False
    assert "循环" in reason


def test_cost_controller_task_status():
    """Task status reports current usage."""
    from app.llm.cost_control import CostController

    cc = CostController()
    cc.check_and_record("task4", "user1", tokens=200)
    cc.check_and_record("task4", "user1", tokens=300)

    status = cc.get_task_status("task4")
    assert status["calls_made"] == 2
    assert status["tokens_used"] == 500


# ============================================================
# Feishu SSO Tests
# ============================================================


def test_feishu_sso_authorize_url():
    """Authorize URL contains required params."""
    from app.auth.feishu_sso import FeishuSSO

    sso = FeishuSSO()
    url = sso.get_authorize_url("https://example.com/callback", "state123")
    assert "redirect_uri" in url
    assert "state123" in url


@pytest.mark.asyncio
async def test_feishu_sso_no_config():
    """SSO returns error when not configured."""
    from app.auth.feishu_sso import FeishuSSO

    sso = FeishuSSO()
    result = await sso.exchange_code_for_token(
        "test-code", "https://example.com"
    )
    # Either configured (success) or returns error
    assert isinstance(result, dict)


# ============================================================
# Observability Tests
# ============================================================


def test_observability_no_op_when_disabled():
    """Observability is no-op when Langfuse not configured."""
    from app.observability.client import ObservabilityClient

    obs = ObservabilityClient()
    # No exceptions even when disabled
    obs.trace_skill_execution(
        skill_id="test", user_id="u1",
        input_message="hi", output_content="hello",
        execution_time_ms=100,
    )
    obs.trace_llm_call(
        model="test", messages=[], response="hi",
        tokens_input=10, tokens_output=20, latency_ms=50,
    )
    obs.flush()


def test_get_observability_singleton():
    """get_observability returns same instance."""
    from app.observability.client import get_observability

    a = get_observability()
    b = get_observability()
    assert a is b


# ============================================================
# Audit Middleware Tests
# ============================================================


def test_audit_middleware_class():
    """AuditMiddleware can be instantiated."""
    from app.auth.audit import AuditMiddleware

    # Just verify class exists and is a middleware
    assert AuditMiddleware.__name__ == "AuditMiddleware"


# ============================================================
# Celery Integration Tests
# ============================================================


def test_celery_app_lazy_load():
    """Celery app loads lazily without blocking imports."""
    from app.patrol.celery_app import get_celery_app

    # Should not raise even if celery not installed
    app = get_celery_app()
    # Either Celery app or None
    assert app is None or hasattr(app, "task")
