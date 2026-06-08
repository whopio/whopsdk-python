# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CardCreateParams"]


class CardCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The business or user account ID to issue the card for."""

    name: str
    """Display name for the card."""

    spend_limit: str
    """Recurring spend limit in dollars (requires spend_limit_frequency)."""

    spend_limit_frequency: Literal["daily", "weekly", "monthly", "one_time"]

    transaction_limit: str
    """Per-authorization limit in dollars (mutually exclusive with spend_limit)."""
