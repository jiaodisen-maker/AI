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


def test_v01_false_positive_now_fixed_in_v02():
    """v0.1 '第一' 会误命中 '第一件事'；v0.2 加了 negative lookahead，修了。"""
    hits = _scan_text("早起第一件事是喝水")
    cats = _categories_hit(hits)
    assert "03_absolute" not in cats  # v0.2 修复


def test_efficacy_v02_extended_patterns():
    """v0.2 扩充后能命中更多疗效宣称变体。"""
    hits = _scan_text("本品可以预防糖尿病并发症，抑制肿瘤生长")
    cats = _categories_hit(hits)
    assert "01_efficacy" in cats


def test_promise_v02_立竿见影():
    hits = _scan_text("吃一盒立竿见影，绝对管用")
    cats = _categories_hit(hits)
    assert "02_promise" in cats


def test_absolute_v02_完美无敌():
    hits = _scan_text("完美的氨糖配方，宇宙领先科技")
    cats = _categories_hit(hits)
    assert "03_absolute" in cats


def test_comparison_v02_kills_competitors():
    hits = _scan_text("效果是普通氨糖的 5 倍，市面上很多牌子都比不上")
    cats = _categories_hit(hits)
    assert "04_comparison" in cats


def test_medical_device_v02_drug_substitute():
    hits = _scan_text("相当于胰岛素针剂，可以代替药品")
    cats = _categories_hit(hits)
    assert "05_medical_device" in cats


def test_extreme_v02_no_side_effects():
    hits = _scan_text("独家神奇配方 0 副作用")
    cats = _categories_hit(hits)
    assert "06_extreme_words" in cats


def test_tcm_v02_meridian():
    hits = _scan_text("打通经络，疏通脉络")
    cats = _categories_hit(hits)
    assert "08_tcm_efficacy" in cats


def test_data_fabrication_v02_harvard():
    hits = _scan_text("哈佛大学认证配方，中科院院士推荐")
    cats = _categories_hit(hits)
    assert "11_data_fabrication" in cats


def test_pseudoscience_v02_alkaline():
    hits = _scan_text("调节酸碱体质，激活细胞线粒体再生")
    cats = _categories_hit(hits)
    assert "12_pseudoscience" in cats


def test_pseudoscience_v02_energy_field():
    hits = _scan_text("产品蕴含宇宙能量场，开光加持")
    cats = _categories_hit(hits)
    assert "12_pseudoscience" in cats


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
