# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AdCampaignUpdateParams"]


class AdCampaignUpdateParams(TypedDict, total=False):
    bid_type: Literal["minimum_cost", "average_target", "maximum_target"]
    """
    How delivery bids in the ad auction: `minimum_cost` gets the most results for
    the budget, `average_target` holds an average cost per result, `maximum_target`
    never bids above a cap. Switching to `minimum_cost` clears the cap amounts
    stored on the campaign's ad groups. Only for campaigns that own the budget.
    """

    budget_amount: float
    """The campaign budget, in the account's currency.

    Interpreted as daily or lifetime per the campaign's budget type, including a
    budget_type sent in the same request.
    """

    budget_optimization: Literal["ad_campaign", "ad_group"]
    """
    Which level owns the budget: the whole campaign (`ad_campaign`) or each ad group
    individually (`ad_group`). Only changeable before the campaign is live on the ad
    network; switching to `ad_campaign` requires budget_amount in the same request,
    and switching to `ad_group` clears the campaign budget.
    """

    budget_type: Literal["daily", "lifetime"]
    """
    Whether `budget_amount` is spent per day (`daily`) or over the campaign's full
    run (`lifetime`). Only changeable while the campaign is a draft; send
    budget_amount in the same request so the amount lands on the new type.
    """

    ends_at: str
    """When the campaign stops delivering, as an ISO 8601 timestamp.

    Only for campaigns that own the budget.
    """

    special_ad_categories: List[Literal["housing", "employment", "financial_products", "politics"]]
    """Regulated categories the campaign falls under.

    Editable on any campaign, draft or launched; pass an empty array to clear.
    """

    starts_at: str
    """When the campaign starts delivering, as an ISO 8601 timestamp.

    Only for campaigns that own the budget.
    """

    status: Literal["active"]
    """Set to active to launch a draft campaign (moderates and pushes it live).

    Live-campaign pause and resume use the pause and unpause actions.
    """

    title: str
    """The name of the campaign."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
