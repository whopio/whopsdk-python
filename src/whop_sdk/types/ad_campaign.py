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
    """Unique identifier for the ad campaign."""

    added_to_carts: float
    """Whop pixel-attributed add-to-cart events, last-click."""

    bid_type: Optional[Literal["minimum_cost", "average_target", "maximum_target"]] = None
    """The bidding strategy the campaign uses."""

    budget_amount: Optional[float] = None
    """The campaign budget in USD.

    Null when budget is set at the ad group level (ABO).
    """

    budget_optimization: Optional[Literal["ad_campaign", "ad_group"]] = None
    """Which level owns the budget — the campaign (CBO) or each ad group (ABO)."""

    budget_type: Optional[Literal["daily", "lifetime"]] = None
    """Whether the budget is spent per day or over the campaign's lifetime."""

    click_through_rate: float
    """Clicks divided by impressions, between 0 and 1."""

    clicks: float
    """The number of clicks."""

    completed_registrations: float
    """Whop pixel-attributed complete-registration events, last-click."""

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

    frequency: Optional[float] = None
    """Platform-reported impressions divided by reach."""

    impressions: float
    """The number of impressions."""

    issues: List[Issue]

    leads: float
    """Whop pixel-attributed leads, last-click."""

    objective: Optional[Literal["awareness", "traffic", "engagement", "leads", "sales"]] = None
    """The goal the campaign optimizes toward."""

    optimization_goal: Optional[str] = None
    """The specific event the campaign optimizes for.

    If the campaign is CBO, then all ad groups will have the same optimization goal,
    which will be returned here.
    """

    platform: Literal["meta"]
    """The ad network the campaign runs on."""

    purchase_value: float
    """USD value of pixel-attributed purchases."""

    purchases: float
    """Whop pixel-attributed purchases, last-click."""

    reach: float
    """The number of unique people who saw this."""

    return_on_ad_spend: float
    """Purchase value divided by spend; 0 when there is no spend."""

    schedules: float
    """Whop pixel-attributed schedule events, last-click."""

    special_ad_categories: List[Literal["housing", "employment", "financial_products", "politics"]]

    spend: float
    """The amount charged, in spend_currency."""

    spend_currency: Optional[str] = None
    """The ISO 4217 currency code of all monetary metrics."""

    status: Literal["draft", "active", "paused", "payment_failed"]
    """The lifecycle status of the ad campaign."""

    submitted_applications: float
    """Whop pixel-attributed submit-application events, last-click."""

    title: str
    """The title of the ad campaign."""

    unique_click_through_rate: Optional[float] = None
    """Unique clicks divided by impressions, between 0 and 1."""

    unique_clicks: float
    """The number of unique clicks."""

    updated_at: str
    """When the campaign was last updated, as an ISO 8601 timestamp."""

    viewed_contents: float
    """Whop pixel-attributed view-content events, last-click."""
