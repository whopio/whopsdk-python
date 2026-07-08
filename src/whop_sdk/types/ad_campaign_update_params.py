# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AdCampaignUpdateParams"]


class AdCampaignUpdateParams(TypedDict, total=False):
    bid_type: Literal["minimum_cost", "average_target", "maximum_target"]
    """
    CBO bid strategy: minimum_cost (lowest cost), average_target (cost cap), or
    maximum_target (bid cap). Switching to minimum_cost clears the cap amounts
    stored on the campaign's ad groups. CBO only.
    """

    budget_amount: float
    """The campaign budget, in the account's currency.

    Interpreted as daily or lifetime per the campaign's existing budget type.
    """

    budget_optimization: Literal["ad_campaign", "ad_group"]
    """Which level owns the budget — the campaign (CBO) or each ad group (ABO).

    Only changeable before the campaign is live on Meta; switching to ad_campaign
    requires budget_amount in the same request, and switching to ad_group clears the
    campaign budget.
    """

    ends_at: str
    """Campaign schedule end (ISO 8601). CBO only."""

    starts_at: str
    """Campaign schedule start (ISO 8601). CBO only."""

    status: Literal["active"]
    """Set to active to launch a draft campaign (moderates and pushes it live).

    Live-campaign pause and resume use the pause and unpause actions.
    """

    title: str
    """The name of the campaign."""
