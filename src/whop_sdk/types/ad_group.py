# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AdGroup", "Issue"]


class Issue(BaseModel):
    """Open issues affecting this ad group. Empty when there are none."""

    id: str
    """Unique identifier for the issue."""

    category: Optional[Literal["policy_rejection", "creative_media", "audience_targeting", "ad_volume_limit"]] = None
    """The kind of problem the issue represents."""

    resource_id: Optional[str] = None
    """The ID of the campaign, ad group, or ad the issue is attached to."""

    resource_type: Literal["ad_campaign", "ad_group", "ad"]
    """The type of resource the issue is attached to."""


class AdGroup(BaseModel):
    id: str
    """Unique identifier for the ad group."""

    ad_campaign: object
    """The ad campaign this ad group belongs to, an object with an id."""

    audience: object
    """Demographic targeting: automatic (Advantage+), age range, gender."""

    bid_type: Optional[Literal["minimum_cost", "average_target", "maximum_target"]] = None
    """Bid strategy."""

    budget_amount: Optional[float] = None
    """Ad-set budget; null when the campaign owns budget (CBO)."""

    budget_type: Optional[Literal["daily", "lifetime"]] = None
    """Whether the budget is daily or lifetime."""

    click_through_rate: float
    """Clicks divided by impressions, between 0 and 1."""

    clicks: float
    """The number of clicks."""

    conversion_event: Union[
        Literal[
            "purchase",
            "add_to_cart",
            "initiated_checkout",
            "add_payment_info",
            "complete_registration",
            "lead",
            "content_view",
            "search",
            "contact",
            "customize_product",
            "donate",
            "find_location",
            "schedule",
            "start_trial",
            "submit_application",
            "subscribe",
        ],
        str,
        None,
    ] = None
    """The pixel event optimized for.

    A standard event, or any custom pixel event name.
    """

    conversion_location: Optional[Literal["website"]] = None
    """Where conversions happen."""

    cost_per_click: float
    """Spend divided by clicks; 0 when there are no clicks."""

    cost_per_lead: Optional[float] = None
    """
    Spend divided by attributed leads; null when leads are not a goal and none are
    attributed.
    """

    cost_per_mille: float
    """Spend per 1,000 impressions; 0 when there are no impressions."""

    cost_per_purchase: Optional[float] = None
    """
    Spend divided by attributed purchases; null when purchases are not a goal and
    none are attributed.
    """

    created_at: str
    """When the ad group was created, ISO 8601."""

    desired_cost_per_result: Optional[float] = None
    """Target/cap cost for average_target / maximum_target."""

    devices: object
    """Device targeting: platforms and operating systems."""

    ends_at: Optional[str] = None
    """Schedule end, ISO 8601."""

    frequency: Optional[float] = None
    """Platform-reported impressions divided by reach."""

    frequency_cap: Optional[object] = None
    """Impression cap; only valid for reach optimization."""

    impressions: float
    """The number of impressions."""

    issues: List[Issue]

    leads: float
    """Whop pixel-attributed leads, last-click."""

    minimum_daily_spend: Optional[float] = None
    """Daily spend floor within the budget."""

    optimization_goal: Optional[str] = None
    """What the ad group optimizes for."""

    placements: List[object]

    purchase_value: float
    """USD value of pixel-attributed purchases."""

    purchases: float
    """Whop pixel-attributed purchases, last-click."""

    reach: float
    """The number of unique people who saw this."""

    regions: object
    """Geo targeting: include/exclude countries, cities, zips."""

    return_on_ad_spend: float
    """Purchase value divided by spend; 0 when there is no spend."""

    spend: float
    """The amount charged, in spend_currency."""

    spend_currency: Optional[str] = None
    """The ISO 4217 currency code of all monetary metrics."""

    starts_at: Optional[str] = None
    """Schedule start, ISO 8601."""

    status: Literal["active", "paused", "rejected"]
    """Delivery status of the ad group."""

    title: Optional[str] = None
    """The display title of the ad group."""

    unique_click_through_rate: Optional[float] = None
    """Unique clicks divided by impressions, between 0 and 1."""

    unique_clicks: float
    """The number of unique clicks."""

    updated_at: str
    """When the ad group was last updated, ISO 8601."""
