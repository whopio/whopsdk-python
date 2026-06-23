# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AdCampaignUpdateParams"]


class AdCampaignUpdateParams(TypedDict, total=False):
    budget_amount: float
    """The campaign budget, in the account's currency."""

    title: str
    """The name of the campaign."""
