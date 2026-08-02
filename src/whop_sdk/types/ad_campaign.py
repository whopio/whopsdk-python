# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AdCampaign", "Issue"]


class Issue(BaseModel):
    """Open issues affecting the campaign and its descendant ad groups and ads."""

    id: str
    """Unique identifier for the issue."""

    message: str
    """A description of what the issue is and how it can be resolved."""

    resource_id: Optional[str] = None
    """The ID of the campaign, ad group, or ad the issue is attached to."""

    resource_type: Literal["ad_campaign", "ad_group", "ad"]
    """The type of resource the issue is attached to."""


class AdCampaign(BaseModel):
    id: str
    """Unique identifier for the ad campaign, prefixed `adcamp_`."""

    added_to_cart_value: float
    """USD value attributed to add-to-cart events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    added_to_carts: float
    """Whop pixel-attributed add-to-cart events, last-click."""

    budget_amount: Optional[float] = None
    """The campaign's budget, in the ad account's currency.

    `null` when each ad group sets its own budget instead.
    """

    budget_optimization: Optional[Literal["ad_campaign", "ad_group"]] = None
    """
    Which level owns the budget: the whole campaign (`ad_campaign`) or each ad group
    individually (`ad_group`).
    """

    budget_type: Optional[Literal["daily", "lifetime"]] = None
    """
    Whether `budget_amount` is spent per day (`daily`) or over the campaign's full
    run (`lifetime`).
    """

    click_through_rate: float
    """Clicks divided by impressions, between 0 and 1."""

    clicks: float
    """The number of clicks."""

    completed_registration_value: float
    """USD value attributed to complete-registration events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    completed_registrations: float
    """Whop pixel-attributed complete-registration events, last-click."""

    contact_value: float
    """USD value attributed to contact events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    contacts: float
    """Whop pixel-attributed contact events, last-click."""

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

    cost_per_result: Optional[float] = None
    """
    Spend divided by Whop pixel-attributed results; null when nothing
    Whop-attributable is being optimized for.
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

    cost_per_unique_click: Optional[float] = None
    """Spend divided by unique clicks; null when there are no unique clicks."""

    cost_per_viewed_content: Optional[float] = None
    """
    Spend divided by attributed view-content events; null when they are not the goal
    and none are attributed.
    """

    created_at: str
    """When the campaign was created, as an ISO 8601 timestamp."""

    custom_conversions: float
    """
    Whop pixel-attributed custom (merchant-defined) conversion events, last-click,
    across all custom event names.
    """

    custom_event_counts: object
    """
    Whop pixel-attributed custom conversions, keyed by your event name with its
    last-click count as the value. Empty when no named custom events are attributed.
    Custom events fired without a name are counted in custom_conversions but omitted
    here, so these values sum to at most custom_conversions.
    """

    custom_event_values: object
    """
    Conversion value attributed to each custom event, keyed by event name like
    custom_event_counts. Sums the value passed to whop.track, normalized to USD;
    events fired without a value contribute 0.
    """

    delivery_status: Literal[
        "payment_failed",
        "all_ads_rejected",
        "draft",
        "no_ad_groups",
        "no_ads",
        "paused",
        "processing",
        "issues",
        "scheduled",
        "completed",
        "ad_groups_off",
        "active",
    ]
    """Whether the campaign's ads are delivering right now, and if not, why.

    When several states apply at once, the highest-precedence one is returned.
    """

    frequency: Optional[float] = None
    """Platform-reported impressions divided by reach."""

    impressions: float
    """The number of impressions."""

    issues: List[Issue]

    lead_value: float
    """USD value attributed to lead events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    leads: float
    """Whop pixel-attributed leads, last-click."""

    objective: Optional[Literal["awareness", "traffic", "engagement", "leads", "sales"]] = None
    """The goal the campaign optimizes toward."""

    optimization_goal: Optional[str] = None
    """The event the campaign optimizes for when a single goal is set campaign-wide.

    `null` when each ad group sets its own optimization_goal.
    """

    platform: Literal["meta", "tiktok"]
    """The ad network the campaign runs on."""

    purchase_value: float
    """USD value of pixel-attributed purchases."""

    purchases: float
    """Whop pixel-attributed purchases, last-click."""

    reach: float
    """The number of unique people who saw this."""

    result_event: Optional[
        Literal[
            "purchase",
            "lead",
            "schedule",
            "submit_application",
            "contact",
            "complete_registration",
            "view_content",
            "add_to_cart",
            "custom",
        ]
    ] = None
    """
    The Whop pixel conversion event whose attributed count represents results — the
    optimization goal, or the highest-volume attributed event for campaigns that
    budget per ad group. Null when the goal isn't a Whop-attributed event.
    """

    result_event_name: Optional[str] = None
    """
    The merchant-defined event name when result_event is custom; null for the
    standard events.
    """

    results: Optional[float] = None
    """The Whop pixel-attributed count behind result_event.

    When a campaign's ad groups optimize different goals there is no single
    result_event (it is null), and this is instead the sum of each ad group's own
    attributed results. Null when nothing Whop-attributable is being optimized for.
    """

    return_on_ad_spend: float
    """
    Purchase value divided by spend, both in USD (a currency-neutral ratio); 0 when
    there is no spend.
    """

    schedule_value: float
    """USD value attributed to schedule events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    schedules: float
    """Whop pixel-attributed schedule events, last-click."""

    special_ad_categories: List[Literal["housing", "employment", "financial_products", "politics"]]

    spend: float
    """The amount charged, in spend_currency."""

    spend_currency: Optional[str] = None
    """The ISO 4217 currency code of all monetary metrics."""

    status: Literal[
        "active",
        "paused",
        "inactive",
        "stale",
        "pending_refund",
        "payment_failed",
        "draft",
        "in_review",
        "flagged",
        "importing",
        "imported",
        "duplicating",
    ]
    """The lifecycle status of the ad campaign."""

    submitted_application_value: float
    """USD value attributed to submit-application events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    submitted_applications: float
    """Whop pixel-attributed submit-application events, last-click."""

    title: str
    """Display name of the ad campaign."""

    unique_click_through_rate: Optional[float] = None
    """Unique clicks divided by impressions, between 0 and 1."""

    unique_clicks: float
    """People who clicked, reported by the Whop pixel, counted once per person."""

    updated_at: str
    """When the campaign was last updated, as an ISO 8601 timestamp."""

    viewed_content_value: float
    """USD value attributed to view-content events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    viewed_contents: float
    """Whop pixel-attributed view-content events, last-click."""

    bid_type: Optional[Literal["minimum_cost", "average_target", "maximum_target"]] = None
    """
    How delivery bids in the ad auction: `minimum_cost` gets the most results for
    the budget, `average_target` holds an average cost per result, and
    `maximum_target` never bids above a cap.
    """
