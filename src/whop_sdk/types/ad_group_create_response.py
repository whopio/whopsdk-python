# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "AdGroupCreateResponse",
    "AdCampaign",
    "Config",
    "ConfigTargeting",
    "PlatformConfig",
    "PlatformConfigMetaAdGroupPlatformConfigType",
    "PlatformConfigTiktokAdGroupPlatformConfigType",
]


class AdCampaign(BaseModel):
    """The parent ad campaign"""

    id: str
    """The unique identifier for the ad campaign."""

    platform: Optional[Literal["meta", "tiktok"]] = None
    """The platforms where an ad campaign can run."""

    status: Literal[
        "active", "paused", "inactive", "stale", "pending_refund", "payment_failed", "draft", "in_review", "flagged"
    ]
    """Current status of the campaign (active, paused, or inactive)"""

    title: str
    """The title of the ad campaign"""


class ConfigTargeting(BaseModel):
    """Audience targeting settings (demographics, geo, interests, audiences, devices)."""

    age_max: Optional[int] = None
    """Maximum age for demographic targeting."""

    age_min: Optional[int] = None
    """Minimum age for demographic targeting."""

    countries: Optional[List[str]] = None
    """ISO 3166-1 alpha-2 country codes targeted."""

    device_platforms: Optional[List[Literal["mobile", "desktop"]]] = None
    """Device platforms targeted."""

    exclude_audience_ids: Optional[List[str]] = None
    """Platform audience IDs excluded."""

    genders: Optional[List[Literal["male", "female", "all"]]] = None
    """Genders targeted."""

    include_audience_ids: Optional[List[str]] = None
    """Platform audience IDs included."""

    interest_ids: Optional[List[str]] = None
    """Platform-specific interest IDs targeted."""

    languages: Optional[List[str]] = None
    """Language codes targeted."""

    placement_type: Optional[Literal["automatic", "manual"]] = None
    """Placement strategy for ad delivery."""


class Config(BaseModel):
    """Unified ad group configuration (platform-agnostic)"""

    bid_amount: Optional[int] = None
    """Bid cap amount in cents. Used when bid_strategy is bid_cap or cost_cap."""

    bid_strategy: Optional[Literal["lowest_cost", "bid_cap", "cost_cap"]] = None
    """Bid strategy: lowest_cost, bid_cap, or cost_cap."""

    billing_event: Optional[Literal["impressions", "clicks", "optimized_cpm", "video_views"]] = None
    """How you are billed (e.g., impressions, clicks)."""

    end_time: Optional[str] = None
    """Scheduled end time (ISO8601). Required for lifetime budgets."""

    frequency_cap: Optional[int] = None
    """Maximum number of times to show ads to each person in the frequency interval."""

    frequency_cap_interval_days: Optional[int] = None
    """Number of days for the frequency cap interval."""

    optimization_goal: Optional[
        Literal[
            "conversions",
            "link_clicks",
            "landing_page_views",
            "reach",
            "impressions",
            "app_installs",
            "video_views",
            "lead_generation",
            "value",
            "page_likes",
            "conversations",
            "ad_recall_lift",
            "two_second_continuous_video_views",
            "post_engagement",
            "event_responses",
            "reminders_set",
            "quality_lead",
        ]
    ] = None
    """What the ad group optimizes for (e.g., conversions, link_clicks, reach)."""

    pacing: Optional[Literal["standard", "accelerated"]] = None
    """Budget pacing: standard (even) or accelerated (fast)."""

    start_time: Optional[str] = None
    """Scheduled start time (ISO8601)."""

    targeting: Optional[ConfigTargeting] = None
    """Audience targeting settings (demographics, geo, interests, audiences, devices)."""


class PlatformConfigMetaAdGroupPlatformConfigType(BaseModel):
    """Meta (Facebook/Instagram) ad set configuration."""

    attribution_spec: Optional[List[Dict[str, object]]] = None

    bid_amount: Optional[int] = None
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    bid_strategy: Optional[
        Literal["LOWEST_COST_WITHOUT_CAP", "LOWEST_COST_WITH_BID_CAP", "COST_CAP", "LOWEST_COST_WITH_MIN_ROAS"]
    ] = None

    billing_event: Optional[
        Literal[
            "APP_INSTALLS",
            "CLICKS",
            "IMPRESSIONS",
            "LINK_CLICKS",
            "NONE",
            "OFFER_CLAIMS",
            "PAGE_LIKES",
            "POST_ENGAGEMENT",
            "THRUPLAY",
            "PURCHASE",
            "LISTING_INTERACTION",
        ]
    ] = None

    daily_budget: Optional[int] = None
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    destination_type: Optional[
        Literal[
            "UNDEFINED",
            "WEBSITE",
            "APP",
            "FACEBOOK",
            "MESSENGER",
            "WHATSAPP",
            "INSTAGRAM_DIRECT",
            "INSTAGRAM_PROFILE",
            "PHONE_CALL",
            "SHOP_AUTOMATIC",
            "APPLINKS_AUTOMATIC",
            "ON_AD",
            "ON_POST",
            "ON_VIDEO",
            "ON_PAGE",
            "ON_EVENT",
            "MESSAGING_MESSENGER_WHATSAPP",
            "MESSAGING_INSTAGRAM_DIRECT_MESSENGER",
            "MESSAGING_INSTAGRAM_DIRECT_WHATSAPP",
            "MESSAGING_INSTAGRAM_DIRECT_MESSENGER_WHATSAPP",
            "INSTAGRAM_PROFILE_AND_FACEBOOK_PAGE",
            "FACEBOOK_PAGE",
            "INSTAGRAM_LIVE",
            "FACEBOOK_LIVE",
            "IMAGINE",
            "LEAD_FROM_IG_DIRECT",
            "LEAD_FROM_MESSENGER",
            "WEBSITE_AND_LEAD_FORM",
            "WEBSITE_AND_PHONE_CALL",
            "BROADCAST_CHANNEL",
        ]
    ] = None

    end_time: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    excluded_geo_locations: Optional[Dict[str, object]] = None
    """Represents untyped JSON"""

    facebook_positions: Optional[List[str]] = None

    geo_locations: Optional[Dict[str, object]] = None
    """Represents untyped JSON"""

    instagram_actor_id: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    instagram_positions: Optional[List[str]] = None

    lifetime_budget: Optional[int] = None
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    optimization_goal: Optional[
        Literal[
            "NONE",
            "APP_INSTALLS",
            "AD_RECALL_LIFT",
            "ENGAGED_USERS",
            "EVENT_RESPONSES",
            "IMPRESSIONS",
            "LEAD_GENERATION",
            "QUALITY_LEAD",
            "LINK_CLICKS",
            "OFFSITE_CONVERSIONS",
            "PAGE_LIKES",
            "POST_ENGAGEMENT",
            "QUALITY_CALL",
            "REACH",
            "LANDING_PAGE_VIEWS",
            "VISIT_INSTAGRAM_PROFILE",
            "VALUE",
            "THRUPLAY",
            "DERIVED_EVENTS",
            "APP_INSTALLS_AND_OFFSITE_CONVERSIONS",
            "CONVERSATIONS",
            "IN_APP_VALUE",
            "MESSAGING_PURCHASE_CONVERSION",
            "SUBSCRIBERS",
            "REMINDERS_SET",
            "MEANINGFUL_CALL_ATTEMPT",
            "PROFILE_VISIT",
            "PROFILE_AND_PAGE_ENGAGEMENT",
            "TWO_SECOND_CONTINUOUS_VIDEO_VIEWS",
            "ENGAGED_REACH",
            "ENGAGED_PAGE_VIEWS",
            "MESSAGING_DEEP_CONVERSATION_AND_FOLLOW",
            "ADVERTISER_SILOED_VALUE",
            "AUTOMATIC_OBJECTIVE",
            "MESSAGING_APPOINTMENT_CONVERSION",
        ]
    ] = None

    page_id: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    platform: Literal["meta", "tiktok"]
    """The ad platform (meta, tiktok)."""

    promoted_object: Optional[Dict[str, object]] = None
    """Represents untyped JSON"""

    publisher_platforms: Optional[List[str]] = None

    status: Optional[Literal["ACTIVE", "PAUSED"]] = None

    targeting_automation: Optional[Dict[str, object]] = None
    """Represents untyped JSON"""

    typename: Literal["MetaAdGroupPlatformConfigType"]
    """The typename of this object"""


class PlatformConfigTiktokAdGroupPlatformConfigType(BaseModel):
    """TikTok ad group configuration."""

    bid_price: Optional[float] = None
    """
    Represents signed double-precision fractional values as specified by
    [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).
    """

    bid_type: Optional[Literal["BID_TYPE_NO_BID", "BID_TYPE_CUSTOM"]] = None

    billing_event: Optional[Literal["CPC", "CPM", "OCPM", "CPV"]] = None

    budget_mode: Optional[Literal["BUDGET_MODE_DAY", "BUDGET_MODE_TOTAL", "BUDGET_MODE_DYNAMIC_DAILY_BUDGET"]] = None

    conversion_bid_price: Optional[float] = None
    """
    Represents signed double-precision fractional values as specified by
    [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).
    """

    identity_id: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    identity_type: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    operation_status: Optional[Literal["ENABLE", "DISABLE"]] = None

    optimization_event: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    optimization_goal: Optional[
        Literal[
            "CLICK",
            "CONVERT",
            "INSTALL",
            "IN_APP_EVENT",
            "REACH",
            "SHOW",
            "VIDEO_VIEW",
            "ENGAGED_VIEW",
            "ENGAGED_VIEW_FIFTEEN",
            "LEAD_GENERATION",
            "PREFERRED_LEAD",
            "CONVERSATION",
            "FOLLOWERS",
            "PROFILE_VIEWS",
            "PAGE_VISIT",
            "VALUE",
            "AUTOMATIC_VALUE_OPTIMIZATION",
            "TRAFFIC_LANDING_PAGE_VIEW",
            "DESTINATION_VISIT",
            "MT_LIVE_ROOM",
            "PRODUCT_CLICK_IN_LIVE",
        ]
    ] = None

    pacing: Optional[Literal["PACING_MODE_SMOOTH", "PACING_MODE_FAST"]] = None

    pixel_id: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    placement_type: Optional[Literal["PLACEMENT_TYPE_AUTOMATIC", "PLACEMENT_TYPE_NORMAL"]] = None

    placements: Optional[List[str]] = None

    platform: Literal["meta", "tiktok"]
    """The ad platform (meta, tiktok)."""

    schedule_end_time: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    schedule_start_time: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    schedule_type: Optional[Literal["SCHEDULE_START_END", "SCHEDULE_FROM_NOW"]] = None

    typename: Literal["TiktokAdGroupPlatformConfigType"]
    """The typename of this object"""


PlatformConfig: TypeAlias = Annotated[
    Union[
        Optional[PlatformConfigMetaAdGroupPlatformConfigType], Optional[PlatformConfigTiktokAdGroupPlatformConfigType]
    ],
    PropertyInfo(discriminator="typename"),
]


class AdGroupCreateResponse(BaseModel):
    """An external ad group (ad set) belonging to an ad campaign"""

    id: str
    """The unique identifier for the external ad group."""

    ad_campaign: AdCampaign
    """The parent ad campaign"""

    config: Optional[Config] = None
    """Unified ad group configuration (platform-agnostic)"""

    created_at: datetime
    """The datetime the external ad group was created."""

    daily_budget: Optional[float] = None
    """Daily budget in dollars (nil for lifetime budgets)"""

    name: Optional[str] = None
    """Human-readable ad group name"""

    platform_config: PlatformConfig
    """Typed platform-specific configuration.

    Use inline fragments (... on MetaAdGroupPlatformConfigType).
    """

    status: Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]
    """Current operational status of the ad group"""

    updated_at: datetime
    """The datetime the external ad group was last updated."""
