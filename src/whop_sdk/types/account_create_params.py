# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["AccountCreateParams"]


class AccountCreateParams(TypedDict, total=False):
    country: str
    """The ISO 3166-1 alpha-2 country code where the account's business is located
    (e.g.

    `US`). Defaults to the parent account's country for connected accounts.
    """

    email: str
    """The email address of the account owner. Required for Account API key requests."""

    metadata: Dict[str, object]
    """Arbitrary key/value metadata to store on the account."""

    title: str
    """The display name of the account.

    Defaults to `metadata.external_id` or the owner's email when omitted.
    """
