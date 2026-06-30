# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AdCampaignUpdateParams"]


class AdCampaignUpdateParams(TypedDict, total=False):
    budget_amount: float
    """The campaign budget, in the account's currency.

    Interpreted as daily or lifetime per the campaign's existing budget type.
    """

    ends_at: str
    """Campaign schedule end (ISO 8601). CBO only."""

    starts_at: str
    """Campaign schedule start (ISO 8601). CBO only."""

    title: str
    """The name of the campaign."""
