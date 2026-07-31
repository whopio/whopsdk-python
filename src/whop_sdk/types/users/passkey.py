# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Passkey"]


class Passkey(BaseModel):
    id: str
    """Passkey ID, prefixed `wcred_`. Use it to delete the passkey."""

    created_at: str
    """When the user registered this passkey, as an ISO 8601 timestamp."""

    credential_id: str
    """The WebAuthn credential ID as a base64url string.

    Pass it in `allowCredentials` when you run a ceremony against this specific
    passkey.
    """

    last_used_at: Optional[str] = None
    """
    When this passkey last completed a WebAuthn ceremony, as an ISO 8601 timestamp,
    or `null` if it never has.
    """

    nickname: str
    """The name the user gave this passkey, usually the device it lives on."""
