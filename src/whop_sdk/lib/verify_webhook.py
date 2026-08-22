"""Verify the Standard Webhooks signature Whop sends on every webhook delivery.

This is the verification half of the ``client.webhooks.unwrap`` the Stainless-generated
SDK shipped through 0.0.41. Fern generates from OpenAPI paths and ``unwrap`` was never a
path, so the generated client has no equivalent. It lives here, beside
``verify_user_token``, rather than on the client so that nothing generated has to be
patched: it depends only on the standard library and ``standardwebhooks``, never on
generated client code, so it survives the client being replaced.

    from whop_sdk.lib.verify_webhook import unwrap

    event = unwrap(request.body, headers=request.headers, key=WHOP_WEBHOOK_SECRET)

What it does NOT do, and the Stainless version did: coerce the parsed body into one of
42 typed event models. Fern generates no webhook event models — ``whop_sdk.WebhookEvent``
is the enum of event *names* a webhook subscribes to, not a payload type — so there is
nothing to coerce into. The parsed body is returned as a plain dict.
"""

from __future__ import annotations

import json
from typing import Any, Dict, Mapping, Union

from standardwebhooks import Webhook, WebhookVerificationError

__all__ = ["unwrap", "WebhookVerificationError"]

MISSING_KEY_MESSAGE = "Cannot verify a webhook without a key. Pass the endpoint's signing secret as `key`."


def unwrap(
    payload: Union[str, bytes],
    *,
    headers: Mapping[str, str],
    key: Union[str, bytes, None],
) -> Dict[str, Any]:
    """Verify ``payload`` against the signature headers and return the parsed body.

    Args:
        payload: The raw, unmodified request body. Verifying a re-serialized body fails:
            the signature covers the exact bytes sent.
        headers: The request headers. Only ``webhook-id``, ``webhook-timestamp`` and
            ``webhook-signature`` are read, and the lookup is case-insensitive.
        key: The endpoint's signing secret, with or without the ``whsec_`` prefix.

    Returns:
        The parsed body.

    Raises:
        ValueError: when ``key`` is missing or empty, or the verified body is not a
            JSON object.
        WebhookVerificationError: when a signature header is missing or malformed, the
            timestamp is outside the tolerance window, or no signature matches.
    """
    if not key:
        raise ValueError(MISSING_KEY_MESSAGE)

    try:
        Webhook(key).verify(payload, dict(headers), json_parse=False)
    except WebhookVerificationError:
        raise
    except Exception as error:
        # standardwebhooks lets a malformed webhook-signature header escape as a bare
        # ValueError or binascii.Error rather than a WebhookVerificationError, and that
        # header is attacker-controlled. Rejecting is right; the exception type is not,
        # so callers can catch one thing.
        raise WebhookVerificationError(f"Invalid signature headers: {error}") from error

    event = json.loads(payload)
    if not isinstance(event, dict):
        raise ValueError(f"Expected the webhook body to be a JSON object, got {type(event).__name__}")
    return event
