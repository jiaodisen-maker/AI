"""飞书安全模块测试：签名验证 + 加密事件解密"""
import base64
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

# 直接从 lark-bot 路径加载模块（避免和 agent-router 的 app 冲突）
ROOT = Path(__file__).parent.parent
LARK_SEC_PATH = ROOT / "services" / "lark-bot" / "app" / "lark_security.py"

spec = importlib.util.spec_from_file_location("lark_security", LARK_SEC_PATH)
lark_security = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lark_security)

LarkSecurityError = lark_security.LarkSecurityError
decrypt_event = lark_security.decrypt_event
parse_event_body = lark_security.parse_event_body
verify_signature = lark_security.verify_signature


def test_verify_signature_no_key_passthrough():
    """没配置 encrypt_key 时跳过验证"""
    assert verify_signature("ts", "nonce", b"body", "fake_sig", "")


def test_verify_signature_correct():
    encrypt_key = "test_key"
    timestamp = "1700000000"
    nonce = "abc"
    body = b'{"hello":"world"}'

    msg = (timestamp + nonce + encrypt_key).encode("utf-8") + body
    expected = hashlib.sha256(msg).hexdigest()

    assert verify_signature(timestamp, nonce, body, expected, encrypt_key)


def test_verify_signature_wrong():
    assert not verify_signature(
        "ts", "nonce", b"body", "wrong_sig", "real_key"
    )


def test_decrypt_roundtrip():
    """加密 → 解密能拿回原文"""
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    import os

    encrypt_key = "my_secret_key"
    payload = {"event": "test", "msg": "hello 世界"}
    plaintext = json.dumps(payload).encode("utf-8")

    pad_len = 16 - (len(plaintext) % 16)
    padded = plaintext + bytes([pad_len]) * pad_len

    key = hashlib.sha256(encrypt_key.encode()).digest()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded) + encryptor.finalize()

    encrypted_b64 = base64.b64encode(iv + ciphertext).decode()

    decrypted = decrypt_event(encrypted_b64, encrypt_key)
    assert decrypted == payload


def test_decrypt_invalid_base64():
    with pytest.raises(LarkSecurityError):
        decrypt_event("!!not_base64!!", "key")


def test_parse_event_body_unencrypted():
    body = {"event": "test", "data": 1}
    result = parse_event_body(body, "")
    assert result == body


def test_parse_event_body_encrypted_no_key():
    with pytest.raises(LarkSecurityError):
        parse_event_body({"encrypt": "xxx"}, "")
