# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PayoutRetrieveParams"]


class PayoutRetrieveParams(TypedDict, total=False):
    account_id: str
    """The owning account ID (a biz\\__ identifier). Provide this or user_id."""

    user_id: str
    """The owning user ID (a user\\__ identifier). Provide this or account_id."""
