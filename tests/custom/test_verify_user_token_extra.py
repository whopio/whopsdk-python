import base64
import importlib
import json
import time
import urllib.request

import pytest

jwt = pytest.importorskip("jwt")

serialization = importlib.import_module("cryptography.hazmat.primitives.serialization")
ec = importlib.import_module("cryptography.hazmat.primitives.asymmetric.ec")
jwt_algorithms = importlib.import_module("jwt.algorithms")

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


def segment(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def nested(depth: int) -> bytes:
    return b"[" * depth + b"]" * depth


def test_user_token_extra_rejects_a_deeply_nested_header():
    _, public_key = signing_key()
    header = b'{"alg":"ES256","x":' + nested(100_000) + b"}"
    payload = b'{"sub":"user_test","aud":"app_test"}'
    token = ".".join([segment(header), segment(payload), segment(bytes(64))])
    with pytest.raises(ValueError):
        verify_user_token(token, app_id="app_test", public_key=public_key)


def test_user_token_extra_rejects_a_deeply_nested_payload():
    # PyJWT parses the payload only after the signature verifies, so the token must be signed.
    private_key, public_key = signing_key()
    header = segment(b'{"alg":"ES256","typ":"JWT"}')
    payload = segment(b'{"sub":"user_test","x":' + nested(100_000) + b"}")
    signing_input = f"{header}.{payload}".encode()
    signature = jwt_algorithms.ECAlgorithm(jwt_algorithms.ECAlgorithm.SHA256).sign(signing_input, private_key)
    token = f"{header}.{payload}.{segment(signature)}"
    with pytest.raises(ValueError):
        verify_user_token(token, app_id="app_test", public_key=public_key)


class JwksResponse:
    status = 200

    def __init__(self, body: bytes) -> None:
        self.body = body

    def read(self) -> bytes:
        return self.body

    def __enter__(self) -> "JwksResponse":
        return self

    def __exit__(self, *exc: object) -> None:
        return None


def test_user_token_extra_skips_a_malformed_key_in_the_jwks(monkeypatch: pytest.MonkeyPatch):
    private_key, _ = signing_key()
    usable = json.loads(jwt_algorithms.ECAlgorithm.to_jwk(private_key.public_key()))
    usable["kid"] = "usable"
    malformed = {"kty": "EC", "crv": "P-256", "x": 1, "y": 2, "kid": "malformed"}
    body = json.dumps({"keys": [malformed, usable]}).encode()
    monkeypatch.setattr(urllib.request, "urlopen", lambda request, timeout: JwksResponse(body))
    token = jwt.encode(
        {"iss": "urn:whopcom:exp-proxy", "sub": "user_test", "aud": "app_test", "exp": int(time.time()) + 300},
        private_key,
        algorithm="ES256",
        headers={"kid": "usable"},
    )
    payload = verify_user_token(token, app_id="app_test", jwks_url="https://jwks.test/malformed-member")
    assert payload.user_id == "user_test"
