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

    budget_amount: float
    """The campaign budget, in USD.

    Required for CBO (budget_optimization: ad_campaign); omit for ABO.
    """

    budget_optimization: Literal["ad_campaign", "ad_group"]
    """Which level owns the budget — the campaign (CBO) or each ad group (ABO).

    Defaults to ad_group.
    """

    budget_type: Literal["daily", "lifetime"]
    """Whether the budget is spent per day or over the campaign's lifetime.

    Defaults to daily.
    """

    special_ad_categories: List[Literal["housing", "employment", "financial_products", "politics"]]
    """Regulated categories the campaign falls under.

    Ads in these categories are subject to extra targeting restrictions.
    """
