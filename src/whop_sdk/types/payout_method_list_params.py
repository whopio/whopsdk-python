# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PayoutMethodListParams"]


class PayoutMethodListParams(TypedDict, total=False):
    account_id: Required[str]
    """The business or user account ID whose payout methods should be returned."""

    page: int
    """Page number (default: 1)."""

    per: int
    """Records per page (default: 10, max: 50)."""
