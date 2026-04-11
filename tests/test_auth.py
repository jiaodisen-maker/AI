"""Tests for the authentication module."""

import pytest

from app.auth.jwt import create_token, decode_token


def test_create_and_decode_token():
    token = create_token(user_id="test-user", role="admin")
    payload = decode_token(token)
    assert payload["sub"] == "test-user"
    assert payload["role"] == "admin"


def test_token_with_extra_claims():
    token = create_token(user_id="u1", extra={"department": "content"})
    payload = decode_token(token)
    assert payload["department"] == "content"


def test_invalid_token_raises():
    with pytest.raises(Exception):
        decode_token("invalid.token.here")


def test_expired_token_raises():
    token = create_token(user_id="u1", expire_hours=-1)
    with pytest.raises(Exception):
        decode_token(token)
