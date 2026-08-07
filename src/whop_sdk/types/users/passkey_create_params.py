# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PasskeyCreateParams"]


class PasskeyCreateParams(TypedDict, total=False):
    attestation_object: Required[str]
    """
    The `attestationObject` from the WebAuthn attestation response,
    base64url-encoded.
    """

    client_data_json: Required[str]
    """The `clientDataJSON` from the WebAuthn attestation response, base64url-encoded."""

    credential_id: Required[str]
    """The WebAuthn credential ID the authenticator returned, base64url-encoded."""

    nickname: Required[str]
    """A name for this passkey, usually the device it lives on.

    255 characters or fewer.
    """
