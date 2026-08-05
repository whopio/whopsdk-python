# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "AdGroup",
    "AdCampaign",
    "Audiences",
    "Demographics",
    "Issue",
    "DetailedTargeting",
    "DetailedTargetingBehavior",
    "DetailedTargetingDemographic",
    "DetailedTargetingInterest",
    "Devices",
    "DevicesOperatingSystem",
    "FrequencyCap",
    "Placement",
    "Regions",
    "RegionsExclude",
    "RegionsExcludeCity",
    "RegionsExcludeCustomLocation",
    "RegionsInclude",
    "RegionsIncludeCity",
    "RegionsIncludeCustomLocation",
]


class AdCampaign(BaseModel):
    """The ad campaign this ad group belongs to."""

    id: str
    """The referenced entity's id."""


class Audiences(BaseModel):
    """Saved audiences this ad group delivers to or excludes."""

    exclude: List[str]

    include: List[str]


class Demographics(BaseModel):
    """Age, gender, and automatic-audience targeting."""

    automatic: bool
    """Whether automatic audience targeting is on (Advantage+ on Meta).

    When `true`, the platform can deliver beyond the ages, genders, and detailed
    targeting you set, treating them as suggestions.
    """

    gender: Literal["all", "male", "female"]
    """Gender targeted."""

    maximum_age: Optional[float] = None
    """Oldest age targeted. `null` when no maximum is set."""

    minimum_age: Optional[float] = None
    """Youngest age targeted. `null` when no minimum is set."""


class Issue(BaseModel):
    """Open issues affecting this ad group and its ads. Empty when there are none."""

    id: str
    """Unique identifier for the issue."""

    message: str
    """A description of what the issue is and how it can be resolved."""

    resource_id: Optional[str] = None
    """The ID of the campaign, ad group, or ad the issue is attached to."""

    resource_type: Literal["ad_campaign", "ad_group", "ad"]
    """The type of resource the issue is attached to."""


class DetailedTargetingBehavior(BaseModel):
    """Behavior categories targeted, such as frequent travelers."""

    id: str
    """The ad platform's ID for the category in its targeting taxonomy."""

    name: Optional[str] = None
    """Category name, such as `Movies`."""


class DetailedTargetingDemographic(BaseModel):
    """Demographic categories targeted, such as life events or industries."""

    id: str
    """The ad platform's ID for the category in its targeting taxonomy."""

    type: Literal["life_events", "industries", "income", "family_statuses"]
    """Kind of demographic the category belongs to."""

    name: Optional[str] = None
    """Category name, such as `Recently moved`."""


class DetailedTargetingInterest(BaseModel):
    """Interest categories targeted, such as an interest in movies."""

    id: str
    """The ad platform's ID for the category in its targeting taxonomy."""

    name: Optional[str] = None
    """Category name, such as `Movies`."""


class DetailedTargeting(BaseModel):
    """
    Interest, behavior, and demographic targeting, using categories from the ad platform's targeting taxonomy. Can't be combined with automatic audience targeting, and unavailable to campaigns with special_ad_categories.
    """

    behaviors: List[DetailedTargetingBehavior]

    demographics: List[DetailedTargetingDemographic]

    interests: List[DetailedTargetingInterest]


class DevicesOperatingSystem(BaseModel):
    """Operating systems targeted. Empty targets all operating systems."""

    os: Literal["ios", "android"]
    """Operating system targeted."""

    minimum_version: Optional[str] = None
    """Lowest OS version targeted, such as `18.0`. Absent when any version qualifies."""


class Devices(BaseModel):
    """Device platforms and operating systems targeted."""

    operating_systems: List[DevicesOperatingSystem]

    platforms: List[Literal["mobile", "desktop"]]


class FrequencyCap(BaseModel):
    """Cap on how often one person sees ads from this ad group.

    Only available on campaigns with the `awareness` objective; `null` when uncapped.
    """

    maximum_impressions: float
    """Most times one person can be shown ads from this ad group within the window."""

    per_days: Optional[float] = None
    """Length of the rolling window, in days."""


class Placement(BaseModel):
    """Where ads can appear, per platform.

    Empty when placements are chosen automatically.
    """

    platform: Literal["facebook", "instagram", "messenger", "audience_network", "threads", "whatsapp"]
    """Publisher platform where the ad is eligible to appear."""

    positions: List[str]


class RegionsExcludeCity(BaseModel):
    """Cities, keyed by the ad platform's location taxonomy."""

    key: str
    """The ad platform's key for the city in its location taxonomy."""

    name: Optional[str] = None
    """City name, such as `Austin`. Absent when the platform doesn't return one."""


class RegionsExcludeCustomLocation(BaseModel):
    """Circular areas, each a coordinate plus a radius."""

    distance_unit: Literal["mile", "kilometer"]
    """Unit for `radius`."""

    latitude: float
    """Latitude of the center point."""

    longitude: float
    """Longitude of the center point."""

    radius: float
    """Radius around the center point, in `distance_unit`."""

    name: Optional[str] = None
    """Label for the location, such as a city or address.

    Absent when the location has no label.
    """


class RegionsExclude(BaseModel):
    """Locations excluded from targeting. Country groups can't be excluded."""

    cities: List[RegionsExcludeCity]

    countries: List[str]

    country_groups: List[str]

    custom_locations: List[RegionsExcludeCustomLocation]

    regions: List[str]

    zips: List[str]


class RegionsIncludeCity(BaseModel):
    """Cities, keyed by the ad platform's location taxonomy."""

    key: str
    """The ad platform's key for the city in its location taxonomy."""

    name: Optional[str] = None
    """City name, such as `Austin`. Absent when the platform doesn't return one."""


class RegionsIncludeCustomLocation(BaseModel):
    """Circular areas, each a coordinate plus a radius."""

    distance_unit: Literal["mile", "kilometer"]
    """Unit for `radius`."""

    latitude: float
    """Latitude of the center point."""

    longitude: float
    """Longitude of the center point."""

    radius: float
    """Radius around the center point, in `distance_unit`."""

    name: Optional[str] = None
    """Label for the location, such as a city or address.

    Absent when the location has no label.
    """


class RegionsInclude(BaseModel):
    """Locations the ad group targets."""

    cities: List[RegionsIncludeCity]

    countries: List[str]

    country_groups: List[str]

    custom_locations: List[RegionsIncludeCustomLocation]

    regions: List[str]

    zips: List[str]


class Regions(BaseModel):
    """Locations targeted and excluded."""

    exclude: RegionsExclude
    """Locations excluded from targeting. Country groups can't be excluded."""

    include: RegionsInclude
    """Locations the ad group targets."""


class AdGroup(BaseModel):
    id: str
    """Unique identifier for the ad group, prefixed `adgrp_`."""

    ad_campaign: AdCampaign
    """The ad campaign this ad group belongs to."""

    added_to_cart_value: float
    """USD value attributed to add-to-cart events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    added_to_carts: float
    """Whop pixel-attributed add-to-cart events, last-click."""

    audiences: Audiences
    """Saved audiences this ad group delivers to or excludes."""

    bid_type: Optional[Literal["minimum_cost", "average_target", "maximum_target"]] = None
    """How delivery bids are set in the ad auction.

    Target-based strategies use `desired_cost_per_result`.
    """

    budget_amount: Optional[float] = None
    """This ad group's budget, in the ad account's currency.

    `null` when the budget is set on the campaign instead.
    """

    budget_type: Optional[Literal["daily", "lifetime"]] = None
    """
    Whether `budget_amount` is spent per day (`daily`) or over the ad group's full
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
    """When the ad group was created, as an ISO 8601 timestamp."""

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
        "all_ads_rejected",
        "rejected",
        "draft",
        "no_ads",
        "campaign_paused",
        "paused",
        "processing",
        "issues",
        "scheduled",
        "completed",
        "ads_off",
        "learning_limited",
        "learning",
        "active",
    ]
    """Whether ads in this ad group are delivering right now, and if not, why.

    When several states apply at once, the highest-precedence one is returned.
    """

    demographics: Demographics
    """Age, gender, and automatic-audience targeting."""

    desired_cost_per_result: Optional[float] = None
    """Cost per result to aim for (`average_target`) or never exceed
    (`maximum_target`).

    `null` for `minimum_cost` bidding.
    """

    ends_at: Optional[str] = None
    """When the ad group stops delivering, as an ISO 8601 timestamp.

    `null` when it runs until paused.
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

    optimization_goal: Optional[
        Literal[
            "conversions",
            "link_clicks",
            "landing_page_views",
            "reach",
            "impressions",
            "engagement",
            "conversations",
            "video_views",
            "two_second_views",
            "page_likes",
            "social_profile",
            "ad_recall_lift",
            "event_responses",
            "reminders_set",
            "lead_generation",
            "quality_lead",
            "value",
            "profile_and_page_engagement",
        ]
    ] = None
    """The result the ad group's delivery is optimized to get the most of."""

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

    spend: float
    """The amount charged, in spend_currency."""

    spend_currency: Optional[str] = None
    """The ISO 4217 currency code of all monetary metrics."""

    starts_at: Optional[str] = None
    """When the ad group starts delivering, as an ISO 8601 timestamp.

    `null` when it starts as soon as it's active.
    """

    status: Literal["active", "paused", "rejected", "duplicating"]
    """Whether the ad group is enabled.

    `active` and `paused` are set by you; `rejected` means it failed ad review;
    `duplicating` is a copy still being filled in.
    """

    submitted_application_value: float
    """USD value attributed to submit-application events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    submitted_applications: float
    """Whop pixel-attributed submit-application events, last-click."""

    title: Optional[str] = None
    """Display name of the ad group."""

    unique_click_through_rate: Optional[float] = None
    """Unique clicks divided by impressions, between 0 and 1."""

    unique_clicks: float
    """People who clicked, reported by the Whop pixel, counted once per person."""

    updated_at: str
    """When the ad group was last updated, as an ISO 8601 timestamp."""

    viewed_content_value: float
    """USD value attributed to view-content events.

    Sums the value sent with each event, normalized to USD; events without a value
    contribute 0.
    """

    viewed_contents: float
    """Whop pixel-attributed view-content events, last-click."""

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
            "instagram_and_facebook",
            "instagram_profile",
            "messaging",
            "on_ad",
            "instant_forms",
            "instant_forms_and_messenger",
            "website_and_instant_forms",
        ]
    ] = None
    """
    Where the outcome being optimized for occurs, such as a website visit,
    social-profile visit, messaging conversation, ad interaction, or lead-form
    submission.
    """

    detailed_targeting: Optional[DetailedTargeting] = None
    """
    Interest, behavior, and demographic targeting, using categories from the ad
    platform's targeting taxonomy. Can't be combined with automatic audience
    targeting, and unavailable to campaigns with special_ad_categories.
    """

    devices: Optional[Devices] = None
    """Device platforms and operating systems targeted."""

    dynamic_creative: Optional[bool] = None
    """
    Whether the ad platform automatically mixes and matches this ad group's
    creatives and copy to find the best-performing combinations.
    """

    frequency_cap: Optional[FrequencyCap] = None
    """Cap on how often one person sees ads from this ad group.

    Only available on campaigns with the `awareness` objective; `null` when
    uncapped.
    """

    languages: Optional[List[str]] = None

    message_apps: Optional[List[Literal["messenger", "instagram", "whatsapp"]]] = None

    minimum_daily_spend: Optional[float] = None
    """Minimum the ad group tries to spend each day. `null` when no floor is set."""

    placements: Optional[List[Placement]] = None

    regions: Optional[Regions] = None
    """Locations targeted and excluded."""
