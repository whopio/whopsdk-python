# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["AccountCreateParams"]


class AccountCreateParams(TypedDict, total=False):
    email: str
    """The email address of the account owner.

    Required for business account API key requests.
    """

    metadata: Dict[str, object]
    """Arbitrary key/value metadata to store on the account."""
