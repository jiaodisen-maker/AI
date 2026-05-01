"""客服库 PII 脱敏测试 — PIPL §28 合规护栏。"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.import_userpain import scrub  # noqa: E402


def test_phone_scrubbed():
    assert "[PHONE]" in scrub("我手机号是 13812345678 请加微信")
    assert "13812345678" not in scrub("我手机号是 13812345678 请加微信")


def test_email_scrubbed():
    assert "[EMAIL]" in scrub("我的邮箱 user.name+test@example.com 谢谢")


def test_idcard_scrubbed():
    assert "[IDCARD]" in scrub("身份证 110101199001011234")


def test_order_id_scrubbed():
    assert "[ORDER_ID]" in scrub("我的订单是 1234567890123")


def test_ip_scrubbed():
    assert "[IP]" in scrub("访问 IP 192.168.1.100")


def test_card_number_scrubbed():
    assert "[CARD]" in scrub("银行卡 6228480402564890018 转账")


def test_chinese_name_scrubbed():
    out = scrub("张明先生反馈失眠")
    assert "[NAME]" in out
    out2 = scrub("李小芳同学说效果不错")
    assert "[NAME]" in out2


def test_clean_text_unchanged():
    text = "凌晨 2 点醒来后睡不着"
    assert scrub(text) == text


def test_no_overscrubbing_of_ages():
    """40 岁这种短数字不应该被当订单号"""
    out = scrub("我今年 45 岁")
    assert "45" in out
