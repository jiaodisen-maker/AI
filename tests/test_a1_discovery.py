"""A1 Discovery 通道路由 + feature flag 测试（不实际抓取）。"""

import pytest

from worker.discovery import discover
from worker.discovery.poc_crawler import _check_feature_flag


def test_unknown_channel_raises():
    with pytest.raises(ValueError):
        discover("kuaishou", "氨糖", n=2)


def test_poc_disabled_by_default(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv("POC_CRAWLED_ENABLED", raising=False)
    with pytest.raises(PermissionError):
        _check_feature_flag()


def test_poc_enabled_passes(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("POC_CRAWLED_ENABLED", "true")
    _check_feature_flag()  # should not raise


def test_poc_enabled_seed_dev(monkeypatch: pytest.MonkeyPatch, tmp_path):
    monkeypatch.setenv("POC_CRAWLED_ENABLED", "true")
    monkeypatch.setenv("POC_AUDIT_LOG", str(tmp_path / "audit.log"))
    cases = discover("poc", "氨糖", n=3)
    # 没装 mediacrawler 时走 seed 路径，返回 3 个占位 case
    assert len(cases) == 3
    for c in cases:
        assert c["data_lineage"] == "poc_crawled"
        assert "url" in c
    # audit log 应该写了
    log = (tmp_path / "audit.log").read_text(encoding="utf-8")
    assert "discover_request" in log
    assert "discover_result" in log


def test_oauth_no_creds_returns_empty(monkeypatch: pytest.MonkeyPatch):
    for k in ("DOUYIN_OAUTH_CLIENT_ID", "DOUYIN_OAUTH_CLIENT_SECRET"):
        monkeypatch.delenv(k, raising=False)
    cases = discover("prod", "氨糖", n=5)
    assert cases == []
