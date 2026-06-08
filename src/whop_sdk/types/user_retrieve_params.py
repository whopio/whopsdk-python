# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserRetrieveParams"]


class UserRetrieveParams(TypedDict, total=False):
    account_id: str
    """
    When set, returns the user's account-specific profile overrides for this
    account.
    """
