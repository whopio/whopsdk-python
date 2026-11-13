import time

import pytest

jwt = pytest.importorskip("jwt")

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

from whop_sdk.lib.verify_user_token import verify_user_token


def signing_key():
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key().public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode()
    return private_key, public_key


def test_user_token_extra_supports_es256_verification():
    private_key, public_key = signing_key()
    token = jwt.encode(
        {"iss": "urn:whopcom:exp-proxy", "sub": "user_test", "aud": "app_test", "exp": int(time.time()) + 300},
        private_key,
        algorithm="ES256",
    )
    payload = verify_user_token(token, app_id="app_test", public_key=public_key)
    assert payload.user_id == "user_test"
    assert payload.app_id == "app_test"
    with pytest.raises(ValueError, match="Invalid app id"):
        verify_user_token(token, app_id="app_other", public_key=public_key)


def test_user_token_extra_rejects_an_unsigned_token():
    _, public_key = signing_key()
    token = jwt.encode(
        {"iss": "urn:whopcom:exp-proxy", "sub": "user_test", "aud": "app_test", "exp": int(time.time()) + 300},
        key="",
        algorithm="none",
    )
    with pytest.raises(ValueError, match="Invalid user token"):
        verify_user_token(token, app_id="app_test", public_key=public_key)
