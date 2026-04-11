"""Tests for the compliant copywriting skill's compliance checks."""

from app.skills.builtin.compliant_copy import CompliantCopySkill

# We can't instantiate CompliantCopySkill without a ModelRouter,
# but we can test the static compliance methods directly.


def _make_skill():
    """Create a skill with a mock model router."""
    class MockRouter:
        pass
    return CompliantCopySkill(MockRouter())


def test_prohibited_words_detected():
    skill = _make_skill()
    violations = skill._check_prohibited_words("这个产品有特效，可以治疗各种疾病")
    assert "特效" in violations
    assert "治疗" in violations


def test_clean_text_no_violations():
    skill = _make_skill()
    violations = skill._check_prohibited_words("这款胶原蛋白有助于改善皮肤水份")
    assert len(violations) == 0


def test_auto_fix_replaces_words():
    skill = _make_skill()
    fixed = skill._auto_fix_prohibited(
        "这是最好的治疗方案，立竿见影",
        ["最好", "治疗", "立竿见影"],
    )
    assert "最好" not in fixed
    assert "治疗" not in fixed
    assert "立竿见影" not in fixed
    assert "优质" in fixed
    assert "调理" in fixed
    assert "循序渐进" in fixed


def test_rule_check_missing_disclaimer():
    skill = _make_skill()
    issues = skill._check_rules("这是一篇很好的文案")
    rule_ids = [i["rule_id"] for i in issues]
    assert "R003" in rule_ids  # Missing disclaimer


def test_rule_check_has_disclaimer():
    skill = _make_skill()
    issues = skill._check_rules("这是一篇好文案。保健食品不是药物，不能代替药物治疗疾病。")
    rule_ids = [i["rule_id"] for i in issues]
    assert "R003" not in rule_ids


def test_rule_check_assertion_words():
    skill = _make_skill()
    issues = skill._check_rules("我们保证效果，绝对有效")
    rule_ids = [i["rule_id"] for i in issues]
    assert "R001" in rule_ids


def test_platform_detection():
    skill = _make_skill()
    from app.skills.models import SkillInput

    input_xhs = SkillInput(user_message="写一篇小红书种草文案")
    assert skill._detect_platform(input_xhs) == "xiaohongshu"

    input_dy = SkillInput(user_message="写抖音短视频脚本")
    assert skill._detect_platform(input_dy) == "douyin"

    input_wx = SkillInput(user_message="写公众号文章")
    assert skill._detect_platform(input_wx) == "wechat"

    input_jd = SkillInput(user_message="写京东详情页")
    assert skill._detect_platform(input_jd) == "jd"
