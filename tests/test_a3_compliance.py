"""A3 Compliance regex scanner — 纯函数测试，无 DB / 无 LLM 依赖。"""
from worker.agents.a3_compliance import _scan_text, _verdict_from_hits


def _categories_hit(hits: list[dict]) -> set[str]:
    return {h["category_id"] for h in hits}


def test_efficacy_red():
    hits = _scan_text("本品能治愈失眠，三盒根治高血压")
    assert "01_efficacy" in _categories_hit(hits)
    assert _verdict_from_hits(hits) == "red"


def test_promise_red():
    hits = _scan_text("30 天见效，无效退款，包治百病")
    cats = _categories_hit(hits)
    assert "02_promise" in cats
    assert _verdict_from_hits(hits) == "red"


def test_absolute_red():
    hits = _scan_text("我们是全国销量第一的氨糖品牌，最有效")
    cats = _categories_hit(hits)
    assert "03_absolute" in cats


def test_extreme_words_yellow():
    hits = _scan_text("史上最强护肝配方，独家专利")
    cats = _categories_hit(hits)
    assert "06_extreme_words" in cats


def test_pseudoscience_red():
    hits = _scan_text("采用量子能量场调理身体")
    cats = _categories_hit(hits)
    assert "12_pseudoscience" in cats


def test_data_fabrication_red():
    hits = _scan_text("全网好评率 99%，复购率 80%")
    cats = _categories_hit(hits)
    assert "11_data_fabrication" in cats


def test_clean_text_green():
    hits = _scan_text("每天早起后按推荐量饮用即可，搭配均衡饮食效果更好。")
    assert _verdict_from_hits(hits) == "green"


def test_known_false_positive_documents_regex_limitation():
    """v0.1 词库 '第一' 会误命中 '第一件事'。文档此限制——A3 LLM 双验阶段会写
    hitl_alert(compliance_edge) 让人介入修订。"""
    hits = _scan_text("早起第一件事是喝水")
    cats = _categories_hit(hits)
    assert "03_absolute" in cats  # 已知误报，留作后续 hitl 案例


def test_tcm_yellow():
    hits = _scan_text("本品有助于补肝护肾，调和阴阳")
    assert "08_tcm_efficacy" in _categories_hit(hits)


def test_medical_institution_red():
    hits = _scan_text("某三甲医院推荐使用，医保定点")
    cats = _categories_hit(hits)
    assert "13_medical_institution" in cats


def test_special_groups_red():
    hits = _scan_text("孕妇可服，糖尿病患者适合长期使用")
    cats = _categories_hit(hits)
    assert "14_special_groups" in cats
