import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Optional, Union

import pytest
from standardwebhooks import Webhook, WebhookVerificationError

from whop_sdk.lib.verify_webhook import unwrap

KEY = "whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw"
OTHER_KEY = "whsec_C2FVsBQIhrscChlQIMV+b5sSYspob7oD"
PAYLOAD = '{"id":"evt_123","event":"payment.succeeded","data":{"id":"pay_123"}}'


def signed_headers(
    payload: str = PAYLOAD,
    key: str = KEY,
    msg_id: str = "msg_2Xa9",
    timestamp: Optional[datetime] = None,
) -> Dict[str, str]:
    at = timestamp if timestamp is not None else datetime.now(tz=timezone.utc)
    return {
        "webhook-id": msg_id,
        "webhook-timestamp": str(int(at.timestamp())),
        "webhook-signature": Webhook(key).sign(msg_id=msg_id, timestamp=at, data=payload),
    }


def test_returns_the_parsed_body_for_a_valid_signature() -> None:
    event = unwrap(PAYLOAD, headers=signed_headers(), key=KEY)

    assert event == {"id": "evt_123", "event": "payment.succeeded", "data": {"id": "pay_123"}}


def test_accepts_a_bytes_payload() -> None:
    assert unwrap(PAYLOAD.encode(), headers=signed_headers(), key=KEY)["id"] == "evt_123"


def test_accepts_headers_whose_names_are_capitalized() -> None:
    headers = {name.title(): value for name, value in signed_headers().items()}

    assert unwrap(PAYLOAD, headers=headers, key=KEY)["id"] == "evt_123"


def test_accepts_a_key_without_the_whsec_prefix() -> None:
    bare = KEY.removeprefix("whsec_")

    assert unwrap(PAYLOAD, headers=signed_headers(key=bare), key=bare)["id"] == "evt_123"


def test_rejects_a_tampered_payload() -> None:
    with pytest.raises(WebhookVerificationError):
        unwrap(PAYLOAD.replace("pay_123", "pay_456"), headers=signed_headers(), key=KEY)


def test_rejects_a_payload_reserialized_with_the_same_content() -> None:
    reserialized = json.dumps(json.loads(PAYLOAD), indent=2)

    assert reserialized != PAYLOAD
    assert json.loads(reserialized) == json.loads(PAYLOAD)
    with pytest.raises(WebhookVerificationError):
        unwrap(reserialized, headers=signed_headers(), key=KEY)


def test_rejects_a_signature_made_with_a_different_key() -> None:
    with pytest.raises(WebhookVerificationError):
        unwrap(PAYLOAD, headers=signed_headers(key=OTHER_KEY), key=KEY)


def test_rejects_a_signature_bound_to_a_different_message_id() -> None:
    headers = {**signed_headers(msg_id="msg_original"), "webhook-id": "msg_replaced"}

    with pytest.raises(WebhookVerificationError):
        unwrap(PAYLOAD, headers=headers, key=KEY)


def test_rejects_a_signature_bound_to_a_different_timestamp() -> None:
    now = datetime.now(tz=timezone.utc)
    headers = {**signed_headers(timestamp=now), "webhook-timestamp": str(int((now - timedelta(minutes=1)).timestamp()))}

    with pytest.raises(WebhookVerificationError):
        unwrap(PAYLOAD, headers=headers, key=KEY)


@pytest.mark.parametrize("offset", [timedelta(minutes=-10), timedelta(minutes=10)])
def test_rejects_a_timestamp_outside_the_tolerance_window(offset: timedelta) -> None:
    stale = datetime.now(tz=timezone.utc) + offset

    with pytest.raises(WebhookVerificationError):
        unwrap(PAYLOAD, headers=signed_headers(timestamp=stale), key=KEY)


@pytest.mark.parametrize("dropped", ["webhook-id", "webhook-timestamp", "webhook-signature"])
def test_rejects_each_missing_signature_header(dropped: str) -> None:
    headers = {name: value for name, value in signed_headers().items() if name != dropped}

    with pytest.raises(WebhookVerificationError):
        unwrap(PAYLOAD, headers=headers, key=KEY)


@pytest.mark.parametrize(
    "signature",
    ["not-a-signature", "v1,", "v1,!!!!", "v2,abc", "", "v1,a,b", "v1," + "A" * 44],
)
def test_rejects_a_malformed_signature_header(signature: str) -> None:
    """standardwebhooks lets some of these escape as a bare ValueError; the helper
    normalizes every rejection onto WebhookVerificationError so callers catch one thing."""
    headers = {**signed_headers(), "webhook-signature": signature}

    with pytest.raises(WebhookVerificationError):
        unwrap(PAYLOAD, headers=headers, key=KEY)


@pytest.mark.parametrize("timestamp", ["not-a-timestamp", "", "1e999"])
def test_rejects_an_unparsable_timestamp(timestamp: str) -> None:
    headers = {**signed_headers(), "webhook-timestamp": timestamp}

    with pytest.raises(WebhookVerificationError):
        unwrap(PAYLOAD, headers=headers, key=KEY)


@pytest.mark.parametrize("key", [None, "", b""])
def test_raises_a_clear_error_when_the_key_is_missing(key: Union[str, bytes, None]) -> None:
    with pytest.raises(ValueError, match="without a key"):
        unwrap(PAYLOAD, headers=signed_headers(), key=key)


def test_raises_before_verifying_when_the_key_is_missing() -> None:
    with pytest.raises(ValueError, match="without a key"):
        unwrap(PAYLOAD, headers={}, key=None)


def test_rejects_a_verified_body_that_is_not_a_json_object() -> None:
    payload = "[1, 2, 3]"

    with pytest.raises(ValueError, match="JSON object"):
        unwrap(payload, headers=signed_headers(payload=payload), key=KEY)


def test_pyproject_declares_standardwebhooks() -> None:
    """src/whop_sdk/lib is kept by .fernignore, but pyproject.toml is generated: the
    dependency is re-declared from extra_dependencies in the python config in
    whop-monorepo sdks/fern/generators.yml. Without it, importing this helper from a
    clean install raises ImportError."""
    # tomllib is 3.11+ and this SDK supports 3.10, so read the section by hand.
    pyproject = (Path(__file__).resolve().parents[2] / "pyproject.toml").read_text()
    section = re.search(r"^\[tool\.poetry\.dependencies\]\n(.*?)(?=^\[)", pyproject, re.S | re.M)

    assert section is not None, "pyproject.toml has no [tool.poetry.dependencies] section"
    assert re.search(r"^standardwebhooks\s*=", section.group(1), re.M), (
        "pyproject.toml must declare standardwebhooks. It is generated, so .fernignore "
        "does not preserve the declaration: set extra_dependencies in the python config "
        "in whop-monorepo sdks/fern/generators.yml."
    )
