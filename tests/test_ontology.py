"""Tests for the Enterprise Ontology module."""

from app.ontology.loader import OntologyLoader
from app.ontology.service import OntologyService


def test_loader_loads_yaml_files():
    loader = OntologyLoader()
    data = loader.load_all()
    assert len(data) > 0
    assert "health_supplements" in loader.dimensions


def test_loader_get_dimension():
    loader = OntologyLoader()
    loader.load_all()
    domain = loader.get("health_supplements")
    assert "product_categories" in domain
    assert "channels" in domain


def test_loader_reload():
    loader = OntologyLoader()
    loader.load_all()
    data = loader.reload()
    assert len(data) > 0


def test_service_query_product():
    service = OntologyService()
    result = service.query_product("胶原蛋白")
    assert "category" in result
    assert result["category"] == "胶原蛋白"
    assert "approved_claims" in result
    assert "prohibited_claims" in result


def test_service_query_product_not_found():
    service = OntologyService()
    result = service.query_product("不存在的产品")
    assert "error" in result


def test_service_query_metric():
    service = OntologyService()
    result = service.query_metric("GMV")
    assert "metric" in result
    assert result["metric"] == "GMV"
    assert "formula" in result


def test_service_query_compliance():
    service = OntologyService()
    result = service.query_compliance("胶原蛋白")
    assert "approved_claims" in result
    assert "prohibited_claims" in result
    assert "美白" in result["prohibited_claims"]


def test_service_query_role():
    service = OntologyService()
    result = service.query_role("渠道总监")
    assert "role" in result
    assert "permissions" in result


def test_service_query_workflow():
    service = OntologyService()
    result = service.query_workflow("新品上市文案流程")
    assert "workflow" in result
    assert "steps" in result


def test_service_query_capability():
    service = OntologyService()
    result = service.query_capability("文案撰写")
    assert "name" in result
    assert result["name"] == "文案撰写"
    assert "automation_coverage" in result


def test_service_list_dimensions():
    service = OntologyService()
    dims = service.list_dimensions()
    assert len(dims) >= 10  # 12 dimensions defined
    assert "health_supplements" in dims
    assert "organization" in dims
    assert "capabilities" in dims
