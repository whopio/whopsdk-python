# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardAccountUpdateParams"]


class CardAccountUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """The business or user account ID that owns the card account."""

    auto_topup_enabled: bool
    """Whether auto-topup is enabled."""

    auto_topup_target_usd: str
    """Target balance (USD) to top up to. Must exceed the threshold by at least $10."""

    auto_topup_threshold_usd: str
    """Balance threshold (USD) that triggers an auto-topup. Required when enabling."""
