# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Ad", "Issue"]


class Issue(BaseModel):
    """Open issues affecting this ad. Empty when there are none."""

    id: str
    """Unique identifier for the issue."""

    category: Optional[Literal["policy_rejection", "creative_media", "audience_targeting", "ad_volume_limit"]] = None
    """The kind of problem the issue represents."""

    resource_id: Optional[str] = None
    """The ID of the campaign, ad group, or ad the issue is attached to."""

    resource_type: Literal["ad_campaign", "ad_group", "ad"]
    """The type of resource the issue is attached to."""


class Ad(BaseModel):
    id: str
    """Unique identifier for the ad."""

    ad_campaign: object
    """The ad campaign this ad belongs to, an object with an id."""

    ad_group: object
    """The ad group this ad belongs to, an object with an id."""

    added_to_carts: float
    """Whop pixel-attributed add-to-cart events, last-click."""

    call_to_action: Optional[
        Literal[
            "learn_more",
            "shop_now",
            "sign_up",
            "subscribe",
            "get_started",
            "book_now",
            "apply_now",
            "contact_us",
            "download",
            "order_now",
            "buy_now",
            "get_quote",
            "message_page",
            "whatsapp_message",
            "instagram_message",
            "call_now",
            "get_directions",
            "send_updates",
            "get_offer",
            "watch_more",
            "listen_now",
            "play_game",
            "open_link",
            "no_button",
            "get_offer_view",
            "get_event_tickets",
            "see_menu",
            "request_time",
            "event_rsvp",
            "see_details",
            "view_instagram_profile",
        ]
    ] = None
    """The call-to-action button shown on the ad."""

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
    """When the ad was created, as an ISO 8601 timestamp."""

    creatives: List[object]

    custom_conversions: float
    """
    Whop pixel-attributed custom (merchant-defined) conversion events, last-click,
    across all custom event names.
    """

    descriptions: List[str]

    frequency: Optional[float] = None
    """Platform-reported impressions divided by reach."""

    headlines: List[str]

    impressions: float
    """The number of impressions."""

    issues: List[Issue]

    lead_form: Optional[object] = None
    """
    The instant lead form on the ad (Meta lead ads), or null when the ad group's
    conversion_location is not an instant-form destination. An object with name,
    form_type (more_volume or higher_intent), an optional intro, questions, a
    privacy_policy, an optional completion screen, and phone_verification.
    """

    leads: float
    """Whop pixel-attributed leads, last-click."""

    messaging_config: Optional[object] = None
    """
    The click-to-message welcome copy, an object with message and keyword, or null
    when the ad has none.
    """

    multi_advertiser_ads: bool
    """Whether the ad can appear alongside other advertisers' ads in the same unit.

    Defaults to true.
    """

    post_id: Optional[str] = None
    """
    The existing post this ad promotes (a Facebook post or Instagram media), or null
    when it uses uploaded creatives.
    """

    primary_texts: List[str]

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

    social_accounts: List[object]

    spend: float
    """The amount charged, in spend_currency."""

    spend_currency: Optional[str] = None
    """The ISO 4217 currency code of all monetary metrics."""

    status: Literal["active", "paused", "in_review", "rejected"]
    """The delivery status of the ad."""

    submitted_applications: float
    """Whop pixel-attributed submit-application events, last-click."""

    title: Optional[str] = None
    """The display title of the ad. Falls back to the creative set caption when unset."""

    unique_click_through_rate: Optional[float] = None
    """Unique clicks divided by impressions, between 0 and 1."""

    unique_clicks: float
    """The number of unique clicks."""

    updated_at: str
    """When the ad was last updated, as an ISO 8601 timestamp."""

    url: Optional[str] = None
    """The URL the ad links to."""

    url_parameters: object
    """Query parameters appended to the URL, as a string-to-string map."""

    viewed_contents: float
    """Whop pixel-attributed view-content events, last-click."""
