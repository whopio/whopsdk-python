# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AdCampaignUpdatedWebhookEvent", "Data", "DataIssue"]


class DataIssue(BaseModel):
    """Open issues affecting the campaign and its descendant ad groups and ads."""

    id: str
    """Unique identifier for the issue."""

    message: str
    """A description of what the issue is and how it can be resolved."""

    resource_id: Optional[str] = None
    """The ID of the campaign, ad group, or ad the issue is attached to."""

    resource_type: Literal["ad_campaign", "ad_group", "ad"]
    """The type of resource the issue is attached to."""


class Data(BaseModel):
    id: str
    """Unique identifier for the ad campaign, prefixed `adcamp_`."""

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

    created_at: str
    """When the campaign was created, as an ISO 8601 timestamp."""

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

    issues: List[DataIssue]

    objective: Optional[Literal["awareness", "traffic", "engagement", "leads", "sales"]] = None
    """The goal the campaign optimizes toward."""

    optimization_goal: Optional[str] = None
    """The event the campaign optimizes for when a single goal is set campaign-wide.

    `null` when each ad group sets its own optimization_goal.
    """

    platform: Literal["meta", "tiktok"]
    """The ad network the campaign runs on."""

    special_ad_categories: List[Literal["housing", "employment", "financial_products", "politics"]]

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

    title: str
    """Display name of the ad campaign."""

    updated_at: str
    """When the campaign was last updated, as an ISO 8601 timestamp."""

    bid_type: Optional[Literal["minimum_cost", "average_target", "maximum_target"]] = None
    """
    How delivery bids in the ad auction: `minimum_cost` gets the most results for
    the budget, `average_target` holds an average cost per result, and
    `maximum_target` never bids above a cap.
    """


class AdCampaignUpdatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    api_version_date: Optional[str] = None
    """The dated API version (Api-Version-Date) the payload is serialized to"""

    data: Data

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["ad_campaign.updated"]
    """The webhook event type"""

    account_id: Optional[str] = None
    """The account ID that this webhook event is associated with"""

    previous_attributes: Optional[object] = None
    """
    For some `.updated` events, the old values of the payload fields that changed,
    keyed by field name. Omitted when no capture is available for the event
    """
