# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AdCampaignCreateParams"]


class AdCampaignCreateParams(TypedDict, total=False):
    objective: Required[Literal["awareness", "traffic", "engagement", "leads", "sales"]]
    """The goal the campaign optimizes toward."""

    platform: Required[Literal["meta"]]
    """The ad network the campaign runs on."""

    title: Required[str]
    """The title of the campaign."""

    account_id: str
    """The account to create the campaign under.

    Defaults to the account-scoped key's own account.
    """

    bid_type: Literal["minimum_cost", "average_target", "maximum_target"]
    """
    How delivery bids in the ad auction: `minimum_cost` gets the most results for
    the budget, `average_target` holds an average cost per result, `maximum_target`
    never bids above a cap. Only for campaigns that own the budget.
    """

    budget_amount: float
    """The campaign's budget, in the ad account's currency.

    Required when budget_optimization is `ad_campaign`; omit when each ad group sets
    its own budget.
    """

    budget_optimization: Literal["ad_campaign", "ad_group"]
    """
    Which level owns the budget: the whole campaign (`ad_campaign`) or each ad group
    individually (`ad_group`). Defaults to `ad_group`.
    """

    budget_type: Literal["daily", "lifetime"]
    """
    Whether the budget is spent per day (`daily`) or over the campaign's full run
    (`lifetime`). Defaults to `daily`.
    """

    desired_cost_per_result: float
    """Cost per result to aim for (`average_target`) or never exceed
    (`maximum_target`).

    Only for campaigns that own the budget.
    """

    ends_at: str
    """When the campaign stops delivering, as an ISO 8601 timestamp.

    Only for campaigns that own the budget.
    """

    special_ad_categories: List[Literal["housing", "employment", "financial_products", "politics"]]
    """Regulated categories the campaign falls under.

    Ads in these categories are subject to extra targeting restrictions.
    """

    starts_at: str
    """When the campaign starts delivering, as an ISO 8601 timestamp.

    Only for campaigns that own the budget.
    """
