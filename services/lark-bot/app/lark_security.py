"""
飞书事件订阅安全模块

支持：
- 签名验证（Signature header）
- AES 加密事件解密
- challenge/url_verification 协议

参考：https://open.feishu.cn/document/server-docs/event-subscription-guide/event-subscription-configure-/encrypt-key-encryption-configuration-case
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import logging
from typing import Any

from cryptography.hazmat.backends import default_backend  # noqa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

logger = logging.getLogger(__name__)


class LarkSecurityError(Exception):
    pass


def verify_signature(
    timestamp: str,
    nonce: str,
    body_raw: bytes,
    signature: str,
    encrypt_key: str,
) -> bool:
    """
    验证飞书事件签名（V2 协议）

    签名 = sha256(timestamp + nonce + encrypt_key + body)
    """
    if not encrypt_key:
        # 未配置加密 key 时跳过签名验证（开发模式）
        return True

    msg = (timestamp + nonce + encrypt_key).encode("utf-8") + body_raw
    expected = hashlib.sha256(msg).hexdigest()
    valid = hmac.compare_digest(expected, signature)
    if not valid:
        logger.warning(
            f"Signature verification failed: expected={expected[:10]}... "
            f"got={signature[:10]}..."
        )
    return valid


def decrypt_event(encrypted: str, encrypt_key: str) -> dict:
    """
    解密飞书加密事件

    加密格式：base64(AES-256-CBC(payload))
    Key 来自 encrypt_key 的 SHA256
    IV 是 ciphertext 的前 16 字节
    """
    if not encrypted or not encrypt_key:
        raise LarkSecurityError("encrypt or encrypt_key missing")

    # 派生 AES key
    key = hashlib.sha256(encrypt_key.encode("utf-8")).digest()

    # base64 解码
    try:
        data = base64.b64decode(encrypted)
    except Exception as e:
        raise LarkSecurityError(f"Invalid base64: {e}") from e

    if len(data) < 16:
        raise LarkSecurityError("Encrypted data too short")

    iv = data[:16]
    ciphertext = data[16:]

    cipher = Cipher(
        algorithms.AES(key), modes.CBC(iv), backend=default_backend()
    )
    decryptor = cipher.decryptor()
    padded = decryptor.update(ciphertext) + decryptor.finalize()

    # PKCS7 unpad
    pad_len = padded[-1]
    if pad_len < 1 or pad_len > 16:
        raise LarkSecurityError(f"Invalid PKCS7 padding: {pad_len}")
    plaintext = padded[:-pad_len]

    try:
        return json.loads(plaintext.decode("utf-8"))
    except Exception as e:
        raise LarkSecurityError(f"Decrypted payload is not JSON: {e}") from e


def parse_event_body(body: dict, encrypt_key: str = "") -> dict:
    """统一处理飞书事件体（自动判断是否加密）"""
    if "encrypt" in body:
        if not encrypt_key:
            raise LarkSecurityError("Event is encrypted but no encrypt_key configured")
        return decrypt_event(body["encrypt"], encrypt_key)
    return body
