# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PasskeyDeleteParams"]


class PasskeyDeleteParams(TypedDict, total=False):
    authenticator_data: Required[str]
    """The `authenticatorData` from the WebAuthn assertion, base64url-encoded."""

    client_data_json: Required[str]
    """The `clientDataJSON` from the WebAuthn assertion, base64url-encoded."""

    signature: Required[str]
    """The `signature` from the WebAuthn assertion, base64url-encoded."""
