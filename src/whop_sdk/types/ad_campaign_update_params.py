# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["AdCampaignUpdateParams", "Config"]


class AdCampaignUpdateParams(TypedDict, total=False):
    ad_creative_set_ids: Optional[SequenceNotStr[str]]
    """Array of creative set IDs to link to this campaign."""

    budget: Optional[float]
    """Budget amount in dollars."""

    budget_type: Optional[Literal["daily", "lifetime"]]
    """The budget type for an ad campaign or ad group."""

    config: Optional[Config]
    """Unified campaign configuration (conversion goal, budget, bidding, etc.)."""

    daily_budget: Optional[float]
    """Daily budget in dollars (minimum $5)."""

    product_id: Optional[str]
    """The unique identifier of the product (access pass) to promote."""

    target_country_codes: Optional[SequenceNotStr[str]]
    """Array of ISO3166 country codes for territory targeting."""

    title: Optional[str]
    """The title of the ad campaign. Must be max 100 characters."""


class Config(TypedDict, total=False):
    """Unified campaign configuration (conversion goal, budget, bidding, etc.)."""

    bid_amount: Optional[int]
    """Bid cap amount in cents. Only used when bid_strategy is bid_cap."""

    bid_strategy: Optional[Literal["lowest_cost", "bid_cap", "cost_cap"]]
    """The bidding strategy used to optimize spend for this campaign."""

    budget_optimization: Optional[bool]
    """
    Whether campaign budget optimization (CBO) is enabled, allowing the platform to
    distribute budget across ad groups.
    """

    end_time: Optional[str]
    """The scheduled end time of the campaign (ISO8601)."""

    lifetime_budget: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    objective: Optional[Literal["awareness", "traffic", "engagement", "leads", "sales"]]
    """The campaign objective that determines how Meta optimizes delivery."""

    special_categories: Optional[SequenceNotStr[str]]
    """
    Special ad categories required by the platform (e.g., housing, employment,
    credit).
    """

    start_time: Optional[str]
    """The scheduled start time of the campaign (ISO8601)."""

    status: Optional[Literal["active", "paused"]]
    """The campaign status as set by the advertiser (active or paused)."""
