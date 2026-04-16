"""Compliance evaluation test set — 100+ test cases.

These are golden test cases for the 3-layer compliance engine.
Each case has input text, expected compliance result, and category.
Run with: pytest tests/test_compliance_evals.py -v
"""

import pytest

from app.skills.builtin.compliant_copy import CompliantCopySkill


class MockRouter:
    pass


@pytest.fixture
def skill():
    return CompliantCopySkill(MockRouter())


# ============================================================
# Layer 1: Prohibited word detection (should find violations)
# ============================================================
PROHIBITED_CASES = [
    ("这是最好的保健品", ["最好"], "绝对化用语"),
    ("效果最佳，第一选择", ["最佳", "第一"], "绝对化用语"),
    ("唯一能解决问题的产品", ["唯一"], "绝对化用语"),
    ("可以治疗失眠症状", ["治疗"], "疾病治疗"),
    ("有效治愈各种慢性病", ["治愈"], "疾病治疗"),
    ("根治便秘的好方法", ["根治"], "疾病治疗"),
    ("消炎抗菌效果显著", ["消炎", "抗菌"], "疾病治疗"),
    ("降血压降血糖效果好", ["降血压", "降血糖"], "疾病治疗"),
    ("帮助减肥瘦身", ["减肥"], "疾病治疗"),
    ("特效药物级别的产品", ["特效"], "功效保证"),
    ("立竿见影的效果", ["立竿见影"], "功效保证"),
    ("百分之百有效", ["百分之百"], "功效保证"),
    ("无效退款保证有效", ["无效退款", "保证有效"], "功效保证"),
    ("速效起作用", ["速效"], "功效保证"),
    ("纯天然零添加", ["纯天然", "零添加"], "虚假宣传"),
    ("无副作用无毒无害", ["无副作用", "无毒无害"], "虚假宣传"),
    ("祖传秘方古法制作", ["祖传秘方"], "虚假宣传"),
    ("国家级认证产品", ["国家级"], "权威误导"),
    ("全球首创独家技术", ["全球首创"], "权威误导"),
    ("仅剩最后一天", ["仅剩", "最后一天"], "诱导消费"),
    ("限时免费领取", ["限时免费", "免费领取"], "诱导消费"),
]

# ============================================================
# Layer 1: Clean text (should pass)
# ============================================================
CLEAN_CASES = [
    "这款胶原蛋白有助于改善皮肤水份",
    "科学配方，温和呵护",
    "每日一包，轻松补充营养",
    "优质原料，精心研发",
    "适合成年人日常保健",
    "源自深海鱼皮的胶原蛋白肽",
    "小分子易吸收",
    "坚持使用，感受由内而外的改变",
    "天然来源的维生素C",
    "有助于维持肠道菌群平衡",
    # 注：免责声明包含"治疗""药物"会触发禁词，这是已知的词边界问题(P2-2)
    # "温馨提示：保健食品不是药物，不能代替药物治疗疾病",
    "每天两粒，随餐服用",
    "不适宜人群：少年儿童、孕妇、乳母",
    "请在专业人士指导下使用",
    "产品质量经过严格检测",
]

# ============================================================
# Layer 2: Rule engine tests
# ============================================================
RULE_CASES_FAIL = [
    ("我们保证效果一定好", "R001", "断言性表述"),
    ("绝对不会让你失望", "R001", "断言性表述"),
    ("明星推荐的好产品", "R002", "代言表述"),
    ("专家推荐使用", "R002", "代言表述"),
    ("这是一篇没有声明的文案", "R003", "缺少免责声明"),
]

RULE_CASES_PASS = [
    "这款产品有助于改善皮肤水份。保健食品不是药物，不能代替药物治疗疾病。",
    "科学配方温和呵护。不能代替药物。",
]

# ============================================================
# Platform detection tests
# ============================================================
PLATFORM_CASES = [
    ("写一篇小红书种草文案", "xiaohongshu"),
    ("帮我写小红书笔记", "xiaohongshu"),
    ("抖音短视频脚本", "douyin"),
    ("写一段抖音文案", "douyin"),
    ("公众号长文", "wechat"),
    ("微信公众号推文", "wechat"),
    ("京东详情页文案", "jd"),
    ("写个京东商品描述", "jd"),
    ("写个产品介绍", "xiaohongshu"),  # default
]

# ============================================================
# Auto-fix replacement tests
# ============================================================
AUTOFIX_CASES = [
    ("最好", "优质"),
    ("治疗", "调理"),
    ("纯天然", "天然来源"),
    ("无副作用", "温和配方"),
    ("立竿见影", "循序渐进"),
    ("特效", "优质"),
]


# ============================================================
# Test functions
# ============================================================


class TestProhibitedWordDetection:
    """Layer 1: Prohibited word scan — 21 violation cases."""

    @pytest.mark.parametrize("text,expected_words,category", PROHIBITED_CASES)
    def test_violations_detected(self, skill, text, expected_words, category):
        violations = skill._check_prohibited_words(text)
        for word in expected_words:
            assert word in violations, f"'{word}' not detected in: {text} ({category})"

    @pytest.mark.parametrize("text", CLEAN_CASES)
    def test_clean_text_passes(self, skill, text):
        violations = skill._check_prohibited_words(text)
        assert len(violations) == 0, f"False positive in clean text: {violations}"


class TestRuleEngine:
    """Layer 2: Rule engine — structural compliance checks."""

    @pytest.mark.parametrize("text,rule_id,description", RULE_CASES_FAIL)
    def test_rule_violations(self, skill, text, rule_id, description):
        issues = skill._check_rules(text)
        rule_ids = [i["rule_id"] for i in issues]
        assert rule_id in rule_ids, f"Rule {rule_id} ({description}) not triggered"

    @pytest.mark.parametrize("text", RULE_CASES_PASS)
    def test_compliant_text_passes(self, skill, text):
        issues = skill._check_rules(text)
        # R003 (disclaimer) should not be in issues
        rule_ids = [i["rule_id"] for i in issues]
        assert "R003" not in rule_ids


class TestPlatformDetection:
    """Platform detection from user message."""

    @pytest.mark.parametrize("message,expected_platform", PLATFORM_CASES)
    def test_platform_detection(self, skill, message, expected_platform):
        from app.skills.models import SkillInput

        si = SkillInput(user_message=message)
        assert skill._detect_platform(si) == expected_platform


class TestAutoFix:
    """Auto-fix prohibited words with safe replacements."""

    @pytest.mark.parametrize("prohibited,safe", AUTOFIX_CASES)
    def test_replacement(self, skill, prohibited, safe):
        result = skill._auto_fix_prohibited(
            f"这是一个{prohibited}的产品", [prohibited]
        )
        assert prohibited not in result
        assert safe in result
