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

    added_to_carts: float
    """Whop pixel-attributed add-to-cart events, last-click."""

    audiences: object
    """Saved-audience targeting: { include, exclude } arrays of audience IDs."""

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

    completed_registrations: float
    """Whop pixel-attributed complete-registration events, last-click."""

    contacts: float
    """Whop pixel-attributed contact events, last-click."""

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

    conversion_location: Optional[
        Literal[
            "website",
            "profile",
            "messaging",
            "on_ad",
            "instant_forms",
            "instant_forms_and_messenger",
            "website_and_instant_forms",
        ]
    ] = None
    """
    Where results happen: website, profile (IG/FB), messaging (DM), on_ad
    (engagement), or the lead destinations (instant_forms,
    instant_forms_and_messenger, website_and_instant_forms).
    """

    cost_per_added_to_cart: Optional[float] = None
    """
    Spend divided by attributed add-to-cart events; null when they are not the goal
    and none are attributed.
    """

    cost_per_click: float
    """Spend divided by clicks; 0 when there are no clicks."""

    cost_per_completed_registration: Optional[float] = None
    """
    Spend divided by attributed complete-registration events; null when they are not
    the goal and none are attributed.
    """

    cost_per_contact: Optional[float] = None
    """
    Spend divided by attributed contact events; null when contacts are not the goal
    and none are attributed.
    """

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

    cost_per_schedule: Optional[float] = None
    """
    Spend divided by attributed schedule events; null when schedules are not the
    goal and none are attributed.
    """

    cost_per_submitted_application: Optional[float] = None
    """
    Spend divided by attributed submit-application events; null when they are not
    the goal and none are attributed.
    """

    cost_per_viewed_content: Optional[float] = None
    """
    Spend divided by attributed view-content events; null when they are not the goal
    and none are attributed.
    """

    created_at: str
    """When the ad group was created, ISO 8601."""

    custom_conversions: float
    """
    Whop pixel-attributed custom (merchant-defined) conversion events, last-click,
    across all custom event names.
    """

    demographics: object
    """Demographic targeting: automatic (Advantage+), age range, gender."""

    desired_cost_per_result: Optional[float] = None
    """Target/cap cost for average_target / maximum_target."""

    devices: object
    """Device targeting: platforms and operating systems."""

    dynamic_creative: bool
    """
    Whether ads within this ad group have their creatives and copy dynamically AB
    tested.
    """

    ends_at: Optional[str] = None
    """Schedule end, ISO 8601."""

    frequency: Optional[float] = None
    """Platform-reported impressions divided by reach."""

    frequency_cap: Optional[object] = None
    """Impression cap; only valid for reach optimization."""

    impressions: float
    """The number of impressions."""

    issues: List[Issue]

    languages: List[str]

    leads: float
    """Whop pixel-attributed leads, last-click."""

    message_apps: List[str]

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
    """Geo targeting: include/exclude countries, regions (ISO 3166-2 states, e.g.

    US-CA), cities, zips.
    """

    return_on_ad_spend: float
    """Purchase value divided by spend; 0 when there is no spend."""

    schedules: float
    """Whop pixel-attributed schedule events, last-click."""

    spend: float
    """The amount charged, in spend_currency."""

    spend_currency: Optional[str] = None
    """The ISO 4217 currency code of all monetary metrics."""

    starts_at: Optional[str] = None
    """Schedule start, ISO 8601."""

    status: Literal["active", "paused", "rejected"]
    """Delivery status of the ad group."""

    submitted_applications: float
    """Whop pixel-attributed submit-application events, last-click."""

    title: Optional[str] = None
    """The display title of the ad group."""

    unique_click_through_rate: Optional[float] = None
    """Unique clicks divided by impressions, between 0 and 1."""

    unique_clicks: float
    """The number of unique clicks."""

    updated_at: str
    """When the ad group was last updated, ISO 8601."""

    viewed_contents: float
    """Whop pixel-attributed view-content events, last-click."""
