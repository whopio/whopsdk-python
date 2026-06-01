# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .ad_budget_type import AdBudgetType
from .ad_group_status import AdGroupStatus

__all__ = [
    "AdGroupUpdateParams",
    "Config",
    "ConfigTargeting",
    "PlatformConfig",
    "PlatformConfigMeta",
    "PlatformConfigMetaAttributionSpec",
    "PlatformConfigMetaExcludedGeoLocations",
    "PlatformConfigMetaExcludedGeoLocationsCity",
    "PlatformConfigMetaExcludedGeoLocationsRegion",
    "PlatformConfigMetaExcludedGeoLocationsZip",
    "PlatformConfigMetaGeoCity",
    "PlatformConfigMetaGeoLocations",
    "PlatformConfigMetaGeoLocationsCity",
    "PlatformConfigMetaGeoLocationsRegion",
    "PlatformConfigMetaGeoLocationsZip",
    "PlatformConfigMetaGeoRegion",
    "PlatformConfigMetaLeadFormConfig",
    "PlatformConfigMetaLeadFormConfigQuestion",
    "PlatformConfigMetaLeadFormConfigQuestionDependentConditionalQuestion",
    "PlatformConfigMetaLeadFormConfigQuestionDependentConditionalQuestionOption",
    "PlatformConfigMetaLeadFormConfigQuestionDependentConditionalQuestionOptionLogic",
    "PlatformConfigMetaLeadFormConfigQuestionOption",
    "PlatformConfigMetaLeadFormConfigQuestionOptionLogic",
    "PlatformConfigMetaLeadFormConfigCustomDisclaimerCheckbox",
    "PlatformConfigMetaLeadFormConfigThankYouPage",
    "PlatformConfigMetaPromotedObject",
    "PlatformConfigMetaTargetingAutomation",
    "PlatformConfigTiktok",
    "PlatformConfigTiktokAction",
    "PlatformConfigTiktokInstantFormConfig",
    "PlatformConfigTiktokInstantFormConfigQuestion",
]


class AdGroupUpdateParams(TypedDict, total=False):
    budget: Optional[float]
    """Budget amount in dollars."""

    budget_type: Optional[AdBudgetType]
    """The budget type for an ad campaign or ad group."""

    config: Optional[Config]
    """Unified ad group configuration (bidding, optimization, targeting)."""

    daily_budget: Optional[float]
    """Daily budget in dollars."""

    name: Optional[str]
    """Human-readable ad group name."""

    platform_config: Optional[PlatformConfig]
    """Platform-specific ad group configuration."""

    status: Optional[AdGroupStatus]
    """The status of an external ad group."""


class ConfigTargeting(TypedDict, total=False):
    """Audience targeting settings (demographics, geo, interests, audiences, devices)."""

    age_max: Optional[int]
    """Maximum age for demographic targeting."""

    age_min: Optional[int]
    """Minimum age for demographic targeting."""

    countries: Optional[SequenceNotStr[str]]
    """ISO 3166-1 alpha-2 country codes to target."""

    device_platforms: Optional[List[Literal["mobile", "desktop"]]]
    """Device platforms to target."""

    exclude_audience_ids: Optional[SequenceNotStr[str]]
    """Platform audience IDs to exclude."""

    genders: Optional[List[Literal["male", "female", "all"]]]
    """Genders to target."""

    include_audience_ids: Optional[SequenceNotStr[str]]
    """Platform audience IDs to include."""

    interest_ids: Optional[SequenceNotStr[str]]
    """Platform-specific interest IDs to target."""

    languages: Optional[SequenceNotStr[str]]
    """Language codes to target."""

    placement_type: Optional[Literal["automatic", "manual"]]
    """Placement strategy for ad delivery."""


class Config(TypedDict, total=False):
    """Unified ad group configuration (bidding, optimization, targeting)."""

    bid_amount: Optional[int]
    """Bid cap amount in cents. Used when bid_strategy is bid_cap or cost_cap."""

    bid_strategy: Optional[Literal["lowest_cost", "bid_cap", "cost_cap"]]
    """Bid strategy: lowest_cost, bid_cap, or cost_cap."""

    billing_event: Optional[Literal["impressions", "clicks", "optimized_cpm", "video_views"]]
    """How you are billed (e.g., impressions, clicks)."""

    end_time: Optional[str]
    """Scheduled end time (ISO8601). Required for lifetime budgets."""

    frequency_cap: Optional[int]
    """Maximum number of times to show ads to each person in the frequency interval."""

    frequency_cap_interval_days: Optional[int]
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
    ]
    """What the ad group optimizes for (e.g., conversions, link_clicks, reach)."""

    pacing: Optional[Literal["standard", "accelerated"]]
    """Budget pacing: standard (even) or accelerated (fast)."""

    start_time: Optional[str]
    """Scheduled start time (ISO8601)."""

    targeting: Optional[ConfigTargeting]
    """Audience targeting settings (demographics, geo, interests, audiences, devices)."""


class PlatformConfigMetaAttributionSpec(TypedDict, total=False):
    """Meta conversion attribution window."""

    event_type: Required[str]
    """Attribution event type (e.g., CLICK_THROUGH, VIEW_THROUGH)."""

    window_days: Required[int]
    """Attribution window in days (1, 7, 28)."""


class PlatformConfigMetaExcludedGeoLocationsCity(TypedDict, total=False):
    """A Meta geo target entry (region, city, or zip)."""

    key: Required[str]
    """Meta geo target key/ID."""

    country: Optional[str]
    """Country code for this entry."""

    name: Optional[str]
    """Display name."""

    radius: Optional[int]
    """Radius in miles (cities only)."""


class PlatformConfigMetaExcludedGeoLocationsRegion(TypedDict, total=False):
    """A Meta geo target entry (region, city, or zip)."""

    key: Required[str]
    """Meta geo target key/ID."""

    country: Optional[str]
    """Country code for this entry."""

    name: Optional[str]
    """Display name."""

    radius: Optional[int]
    """Radius in miles (cities only)."""


class PlatformConfigMetaExcludedGeoLocationsZip(TypedDict, total=False):
    """A Meta geo target entry (region, city, or zip)."""

    key: Required[str]
    """Meta geo target key/ID."""

    country: Optional[str]
    """Country code for this entry."""

    name: Optional[str]
    """Display name."""

    radius: Optional[int]
    """Radius in miles (cities only)."""


class PlatformConfigMetaExcludedGeoLocations(TypedDict, total=False):
    """Geo locations to exclude."""

    cities: Optional[Iterable[PlatformConfigMetaExcludedGeoLocationsCity]]
    """City targets."""

    countries: Optional[SequenceNotStr[str]]
    """ISO 3166-1 alpha-2 country codes."""

    location_types: Optional[SequenceNotStr[str]]
    """Location types (home, recent, travel_in)."""

    regions: Optional[Iterable[PlatformConfigMetaExcludedGeoLocationsRegion]]
    """Region/state targets."""

    zips: Optional[Iterable[PlatformConfigMetaExcludedGeoLocationsZip]]
    """Zip/postal code targets."""


class PlatformConfigMetaGeoCity(TypedDict, total=False):
    """A Meta geo target entry (region, city, or zip)."""

    key: Required[str]
    """Meta geo target key/ID."""

    country: Optional[str]
    """Country code for this entry."""

    name: Optional[str]
    """Display name."""

    radius: Optional[int]
    """Radius in miles (cities only)."""


class PlatformConfigMetaGeoLocationsCity(TypedDict, total=False):
    """A Meta geo target entry (region, city, or zip)."""

    key: Required[str]
    """Meta geo target key/ID."""

    country: Optional[str]
    """Country code for this entry."""

    name: Optional[str]
    """Display name."""

    radius: Optional[int]
    """Radius in miles (cities only)."""


class PlatformConfigMetaGeoLocationsRegion(TypedDict, total=False):
    """A Meta geo target entry (region, city, or zip)."""

    key: Required[str]
    """Meta geo target key/ID."""

    country: Optional[str]
    """Country code for this entry."""

    name: Optional[str]
    """Display name."""

    radius: Optional[int]
    """Radius in miles (cities only)."""


class PlatformConfigMetaGeoLocationsZip(TypedDict, total=False):
    """A Meta geo target entry (region, city, or zip)."""

    key: Required[str]
    """Meta geo target key/ID."""

    country: Optional[str]
    """Country code for this entry."""

    name: Optional[str]
    """Display name."""

    radius: Optional[int]
    """Radius in miles (cities only)."""


class PlatformConfigMetaGeoLocations(TypedDict, total=False):
    """Geo targeting (countries, regions, cities, zips)."""

    cities: Optional[Iterable[PlatformConfigMetaGeoLocationsCity]]
    """City targets."""

    countries: Optional[SequenceNotStr[str]]
    """ISO 3166-1 alpha-2 country codes."""

    location_types: Optional[SequenceNotStr[str]]
    """Location types (home, recent, travel_in)."""

    regions: Optional[Iterable[PlatformConfigMetaGeoLocationsRegion]]
    """Region/state targets."""

    zips: Optional[Iterable[PlatformConfigMetaGeoLocationsZip]]
    """Zip/postal code targets."""


class PlatformConfigMetaGeoRegion(TypedDict, total=False):
    """A Meta geo target entry (region, city, or zip)."""

    key: Required[str]
    """Meta geo target key/ID."""

    country: Optional[str]
    """Country code for this entry."""

    name: Optional[str]
    """Display name."""

    radius: Optional[int]
    """Radius in miles (cities only)."""


class PlatformConfigMetaLeadFormConfigQuestionDependentConditionalQuestionOptionLogic(TypedDict, total=False):
    """Conditional logic routing for this answer option."""

    type: Required[str]
    """Logic type: go_to_question, submit_form, or close_form."""

    target_end_page_index: Optional[int]
    """Index of the end page to route to (for submit_form type)."""

    target_question_index: Optional[int]
    """Index of the question to route to (for go_to_question type)."""


class PlatformConfigMetaLeadFormConfigQuestionDependentConditionalQuestionOption(TypedDict, total=False):
    """An answer option for a multiple choice lead form question."""

    key: Required[str]
    """Unique key for this option."""

    value: Required[str]
    """Display text for this option."""

    logic: Optional[PlatformConfigMetaLeadFormConfigQuestionDependentConditionalQuestionOptionLogic]
    """Conditional logic routing for this answer option."""


class PlatformConfigMetaLeadFormConfigQuestionDependentConditionalQuestion(TypedDict, total=False):
    """A dependent conditional question (non-recursive to avoid schema recursion)."""

    type: Required[str]
    """Question type (EMAIL, FULL_NAME, PHONE, CUSTOM, DATE_TIME, etc.)."""

    inline_context: Optional[str]
    """Helper text shown below the question."""

    key: Optional[str]
    """Unique key for this question."""

    label: Optional[str]
    """Custom label for CUSTOM questions."""

    options: Optional[Iterable[PlatformConfigMetaLeadFormConfigQuestionDependentConditionalQuestionOption]]
    """Answer options for multiple choice questions."""


class PlatformConfigMetaLeadFormConfigQuestionOptionLogic(TypedDict, total=False):
    """Conditional logic routing for this answer option."""

    type: Required[str]
    """Logic type: go_to_question, submit_form, or close_form."""

    target_end_page_index: Optional[int]
    """Index of the end page to route to (for submit_form type)."""

    target_question_index: Optional[int]
    """Index of the question to route to (for go_to_question type)."""


class PlatformConfigMetaLeadFormConfigQuestionOption(TypedDict, total=False):
    """An answer option for a multiple choice lead form question."""

    key: Required[str]
    """Unique key for this option."""

    value: Required[str]
    """Display text for this option."""

    logic: Optional[PlatformConfigMetaLeadFormConfigQuestionOptionLogic]
    """Conditional logic routing for this answer option."""


class PlatformConfigMetaLeadFormConfigQuestion(TypedDict, total=False):
    """A question on a Meta lead gen form."""

    type: Required[str]
    """Question type (EMAIL, FULL_NAME, PHONE, CUSTOM, DATE_TIME, etc.)."""

    conditional_questions_group_id: Optional[str]
    """Group ID for conditional question routing."""

    dependent_conditional_questions: Optional[
        Iterable[PlatformConfigMetaLeadFormConfigQuestionDependentConditionalQuestion]
    ]
    """Questions shown conditionally based on this question's answer."""

    inline_context: Optional[str]
    """Helper text shown below the question."""

    key: Optional[str]
    """Unique key for this question."""

    label: Optional[str]
    """Custom label for CUSTOM questions."""

    options: Optional[Iterable[PlatformConfigMetaLeadFormConfigQuestionOption]]
    """Answer options for multiple choice CUSTOM questions."""

    question_format: Optional[str]
    """UI hint: short_answer, multiple_choice, or appointment."""


class PlatformConfigMetaLeadFormConfigCustomDisclaimerCheckbox(TypedDict, total=False):
    """A consent checkbox for the custom disclaimer section."""

    key: Required[str]
    """Unique key for this checkbox."""

    text: Required[str]
    """Label text for the checkbox."""

    is_checked_by_default: Optional[bool]
    """Whether the checkbox is checked by default."""

    is_required: Optional[bool]
    """Whether the checkbox must be checked to submit."""


class PlatformConfigMetaLeadFormConfigThankYouPage(TypedDict, total=False):
    """A thank-you / ending page for a Meta lead gen form."""

    body: Optional[str]
    """Body text for this ending page."""

    business_phone: Optional[str]
    """Business phone number for call CTA."""

    button_text: Optional[str]
    """Custom button text."""

    button_type: Optional[str]
    """CTA button type: VIEW_WEBSITE, CALL_BUSINESS, DOWNLOAD."""

    conditional_question_group_id: Optional[str]
    """Question group ID for conditional routing to this page."""

    enable_messenger: Optional[bool]
    """Enable Messenger follow-up."""

    gated_file_url: Optional[str]
    """Uploaded file URL for gated content download."""

    link: Optional[str]
    """URL the button links to."""

    name: Optional[str]
    """Internal name for this ending page."""

    title: Optional[str]
    """Headline for this ending page."""


class PlatformConfigMetaLeadFormConfig(TypedDict, total=False):
    """Configuration for a Meta lead gen instant form."""

    name: Required[str]
    """Name of the lead form."""

    privacy_policy_url: Required[str]
    """URL to your privacy policy. Required by Meta."""

    questions: Required[Iterable[PlatformConfigMetaLeadFormConfigQuestion]]
    """Questions to ask on the form."""

    background_image_source: Optional[str]
    """Background image source: from_ad or custom."""

    background_image_url: Optional[str]
    """URL of custom background image."""

    conditional_logic_enabled: Optional[bool]
    """Whether conditional logic is enabled for questions."""

    context_card_button_text: Optional[str]
    """CTA button text on the greeting card."""

    context_card_content: Optional[SequenceNotStr[str]]
    """Optional greeting card bullet points."""

    context_card_style: Optional[str]
    """Greeting layout: PARAGRAPH_STYLE or LIST_STYLE."""

    context_card_title: Optional[str]
    """Optional greeting card title."""

    custom_disclaimer_body: Optional[str]
    """Custom disclaimer body text."""

    custom_disclaimer_checkboxes: Optional[Iterable[PlatformConfigMetaLeadFormConfigCustomDisclaimerCheckbox]]
    """Consent checkboxes for the custom disclaimer."""

    custom_disclaimer_title: Optional[str]
    """Custom disclaimer section title."""

    form_type: Optional[str]
    """Form type: more_volume, higher_intent, or rich_creative."""

    messenger_enabled: Optional[bool]
    """Enable Messenger follow-up after form submission."""

    phone_verification_enabled: Optional[bool]
    """Require phone number verification via OTP (higher_intent only)."""

    privacy_policy_link_text: Optional[str]
    """Custom link text for privacy policy (max 70 chars)."""

    question_page_custom_headline: Optional[str]
    """Custom headline for the questions page."""

    rich_creative_headline: Optional[str]
    """Headline for rich creative form intro."""

    rich_creative_overview: Optional[str]
    """Overview description for rich creative form intro."""

    rich_creative_url: Optional[str]
    """Uploaded image URL for rich creative form type."""

    thank_you_pages: Optional[Iterable[PlatformConfigMetaLeadFormConfigThankYouPage]]
    """Thank you / ending pages (supports multiple for conditional routing)."""


class PlatformConfigMetaPromotedObject(TypedDict, total=False):
    """The object this ad set promotes (pixel, page, etc.)."""

    custom_conversion_id: Optional[str]
    """Custom conversion rule ID (numeric, from Meta Events Manager)."""

    custom_event_str: Optional[str]
    """Pixel event name, used when custom_event_type is OTHER."""

    custom_event_type: Optional[str]
    """Custom event type (e.g., PURCHASE, COMPLETE_REGISTRATION, OTHER)."""

    page_id: Optional[str]
    """Facebook Page ID."""

    pixel_id: Optional[str]
    """Meta Pixel ID for conversion tracking."""

    whatsapp_phone_number: Optional[str]
    """WhatsApp phone number for messaging campaigns."""


class PlatformConfigMetaTargetingAutomation(TypedDict, total=False):
    """Advantage+ audience expansion settings."""

    advantage_audience: Optional[int]
    """0 = off (use exact targeting), 1 = on (let Meta expand audience)."""


class PlatformConfigMeta(TypedDict, total=False):
    """Meta (Facebook/Instagram) ad set configuration."""

    android_devices: Optional[SequenceNotStr[str]]

    attribution_setting: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    attribution_spec: Optional[Iterable[PlatformConfigMetaAttributionSpec]]
    """Conversion attribution windows."""

    audience_network_positions: Optional[SequenceNotStr[str]]

    audience_type: Optional[str]
    """Audience type for retargeting."""

    bid_amount: Optional[int]
    """Bid amount in cents."""

    bid_strategy: Optional[
        Literal["LOWEST_COST_WITHOUT_CAP", "LOWEST_COST_WITH_BID_CAP", "COST_CAP", "LOWEST_COST_WITH_MIN_ROAS"]
    ]
    """Meta bid strategy."""

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
    ]
    """How you are billed on Meta."""

    brand_safety_content_filter_levels: Optional[SequenceNotStr[str]]

    budget_remaining: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    cost_per_result_goal: Optional[float]
    """
    Represents signed double-precision fractional values as specified by
    [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).
    """

    created_time: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    daily_budget: Optional[int]
    """Daily budget in cents."""

    daily_min_spend_target: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    daily_spend_cap: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
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
            "LEAD_FORM_MESSENGER",
            "WEBSITE_AND_LEAD_FORM",
            "WEBSITE_AND_PHONE_CALL",
            "BROADCAST_CHANNEL",
        ]
    ]
    """Where ads in this ad set direct people."""

    dsa_beneficiary: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    dsa_payor: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    end_time: Optional[str]
    """End time (ISO8601). Required for lifetime budgets."""

    excluded_geo_locations: Optional[PlatformConfigMetaExcludedGeoLocations]
    """Geo locations to exclude."""

    facebook_positions: Optional[SequenceNotStr[str]]
    """Facebook ad placements (feed, reels, stories, etc.)."""

    frequency_control_count: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    frequency_control_days: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    frequency_control_type: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    geo_cities: Optional[Iterable[PlatformConfigMetaGeoCity]]

    geo_locations: Optional[PlatformConfigMetaGeoLocations]
    """Geo targeting (countries, regions, cities, zips)."""

    geo_regions: Optional[Iterable[PlatformConfigMetaGeoRegion]]

    geo_zips: Optional[SequenceNotStr[str]]

    instagram_actor_id: Optional[str]
    """Instagram account ID for this ad set."""

    instagram_positions: Optional[SequenceNotStr[str]]
    """Instagram ad placements (stream, story, reels, etc.)."""

    ios_devices: Optional[SequenceNotStr[str]]

    is_dynamic_creative: Optional[bool]
    """Represents `true` or `false` values."""

    lead_conversion_location: Optional[
        Literal["website", "instant_forms", "website_and_instant_forms", "messenger", "instagram", "calls", "app"]
    ]

    lead_form_config: Optional[PlatformConfigMetaLeadFormConfig]
    """Configuration for a Meta lead gen instant form."""

    lead_gen_form_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    lifetime_budget: Optional[int]
    """Lifetime budget in cents."""

    lifetime_min_spend_target: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    lifetime_spend_cap: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    location_types: Optional[SequenceNotStr[str]]

    messenger_positions: Optional[SequenceNotStr[str]]

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
    ]
    """What this ad set optimizes for on Meta."""

    page_id: Optional[str]
    """Facebook Page ID for this ad set."""

    pixel_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    promoted_object: Optional[PlatformConfigMetaPromotedObject]
    """The object this ad set promotes (pixel, page, etc.)."""

    publisher_platforms: Optional[SequenceNotStr[str]]
    """Platforms to publish on (facebook, instagram, messenger, audience_network)."""

    source_adset_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    start_time: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    status: Optional[Literal["ACTIVE", "PAUSED"]]

    targeting_automation: Optional[PlatformConfigMetaTargetingAutomation]
    """Advantage+ audience expansion settings."""

    threads_positions: Optional[SequenceNotStr[str]]

    updated_time: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    user_device: Optional[SequenceNotStr[str]]

    user_os: Optional[SequenceNotStr[str]]

    whatsapp_phone_number: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    whatsapp_positions: Optional[SequenceNotStr[str]]


class PlatformConfigTiktokAction(TypedDict, total=False):
    """A single TikTok behavioral targeting entry.

    One category of past user behavior (what they did, over what window, on which kind of content). See docs/tiktok_api/ad_group.md § actions.
    """

    action_category_ids: Optional[SequenceNotStr[str]]
    """Behavioral category IDs. Use /tool/action_category/ to list them."""

    action_period: Optional[int]
    """Lookback window in days. TikTok accepts 7, 15, 30, 60, 90, or 180."""

    action_scene: Optional[Literal["VIDEO_RELATED", "CREATOR_RELATED", "HASHTAG_RELATED", "LIVE_RELATED"]]
    """The category of TikTok content a behavioral targeting rule applies to.

    See docs/tiktok_api/ad_group.md § actions.
    """

    video_user_actions: Optional[
        List[Literal["WATCHED_TO_END", "LIKED", "COMMENTED", "SHARED", "FOLLOWED", "PROFILE_VISITED"]]
    ]
    """
    Specific video interactions (WATCHED_TO_END, LIKED, COMMENTED, SHARED, FOLLOWED,
    PROFILE_VISITED).
    """


class PlatformConfigTiktokInstantFormConfigQuestion(TypedDict, total=False):
    """A question for a TikTok instant form."""

    field_type: Required[str]
    """Question type (EMAIL, PHONE_NUMBER, NAME, CUSTOM)."""

    label: Optional[str]
    """Custom label for the question."""


class PlatformConfigTiktokInstantFormConfig(TypedDict, total=False):
    """Instant form configuration for lead generation campaigns."""

    privacy_policy_url: Required[str]
    """URL to your privacy policy."""

    questions: Required[Iterable[PlatformConfigTiktokInstantFormConfigQuestion]]
    """Form questions (at least one required)."""

    button_text: Optional[str]
    """Submit button text."""

    greeting: Optional[str]
    """Greeting text shown at the top of the form."""

    name: Optional[str]
    """Form name. Auto-generated if omitted."""


class PlatformConfigTiktok(TypedDict, total=False):
    """TikTok ad group configuration."""

    actions: Optional[Iterable[PlatformConfigTiktokAction]]

    age_groups: Optional[List[Literal["AGE_13_17", "AGE_18_24", "AGE_25_34", "AGE_35_44", "AGE_45_54", "AGE_55_100"]]]

    app_id: Optional[str]
    """App ID for app promotion campaigns."""

    attribution_event_count: Optional[Literal["UNSET", "EVERY", "ONCE"]]

    audience_ids: Optional[SequenceNotStr[str]]

    audience_rule: Optional[Dict[str, object]]
    """Represents untyped JSON"""

    audience_type: Optional[Literal["NORMAL", "SMART_INTERESTS_BEHAVIORS"]]

    bid_price: Optional[float]
    """Bid price (cost per result for Cost Cap)."""

    bid_type: Optional[Literal["BID_TYPE_NO_BID", "BID_TYPE_CUSTOM"]]
    """Bidding strategy (BID_TYPE_NO_BID, BID_TYPE_CUSTOM)."""

    billing_event: Optional[Literal["CPC", "CPM", "OCPM", "CPV"]]
    """How you are billed on TikTok (CPC, CPM, OCPM, CPV)."""

    brand_safety_type: Optional[
        Literal["NO_BRAND_SAFETY", "STANDARD_INVENTORY", "LIMITED_INVENTORY", "FULL_INVENTORY", "EXPANDED_INVENTORY"]
    ]

    budget_mode: Optional[Literal["BUDGET_MODE_DAY", "BUDGET_MODE_TOTAL", "BUDGET_MODE_DYNAMIC_DAILY_BUDGET"]]
    """
    Budget mode (BUDGET_MODE_DAY, BUDGET_MODE_TOTAL,
    BUDGET_MODE_DYNAMIC_DAILY_BUDGET).
    """

    carrier_ids: Optional[SequenceNotStr[str]]

    category_exclusion_ids: Optional[SequenceNotStr[str]]

    click_attribution_window: Optional[Literal["OFF", "ONE_DAY", "SEVEN_DAYS", "FOURTEEN_DAYS", "TWENTY_EIGHT_DAYS"]]

    comment_disabled: Optional[bool]
    """Represents `true` or `false` values."""

    contextual_tag_ids: Optional[SequenceNotStr[str]]

    conversion_bid_price: Optional[float]
    """Target cost per conversion for oCPM."""

    creative_material_mode: Optional[str]
    """Creative delivery strategy."""

    dayparting: Optional[str]
    """Ad delivery schedule (48x7 character string)."""

    deep_funnel_event_source: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    deep_funnel_event_source_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    deep_funnel_optimization_status: Optional[Literal["ON", "OFF"]]

    device_model_ids: Optional[SequenceNotStr[str]]

    device_price_ranges: Optional[SequenceNotStr[str]]

    engaged_view_attribution_window: Optional[Literal["OFF", "ONE_DAY", "SEVEN_DAYS"]]

    excluded_audience_ids: Optional[SequenceNotStr[str]]

    excluded_location_ids: Optional[SequenceNotStr[str]]
    """TikTok location/region IDs to exclude."""

    frequency: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    frequency_schedule: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    gender: Optional[Literal["GENDER_UNLIMITED", "GENDER_MALE", "GENDER_FEMALE"]]

    identity_authorized_bc_id: Optional[str]
    """Business Center ID for BC_AUTH_TT identity."""

    identity_id: Optional[str]
    """TikTok identity ID for the ad group."""

    identity_type: Optional[str]
    """Identity type (AUTH_CODE, TT_USER, BC_AUTH_TT)."""

    instant_form_config: Optional[PlatformConfigTiktokInstantFormConfig]
    """Instant form configuration for lead generation campaigns."""

    instant_form_id: Optional[str]
    """
    TikTok instant form ID (set automatically when instant_form_config is provided).
    """

    interest_category_ids: Optional[SequenceNotStr[str]]

    interest_keyword_ids: Optional[SequenceNotStr[str]]

    inventory_filter_enabled: Optional[bool]
    """Represents `true` or `false` values."""

    ios14_targeting: Optional[Literal["UNSET", "IOS14_MINUS", "IOS14_PLUS", "ALL"]]

    isp_ids: Optional[SequenceNotStr[str]]

    languages: Optional[SequenceNotStr[str]]

    location_ids: Optional[SequenceNotStr[str]]
    """TikTok location/region IDs for geo targeting."""

    min_android_version: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    min_ios_version: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    network_types: Optional[SequenceNotStr[str]]

    operating_systems: Optional[List[Literal["ANDROID", "IOS"]]]

    operation_status: Optional[Literal["ENABLE", "DISABLE"]]
    """Initial status (ENABLE, DISABLE)."""

    optimization_event: Optional[str]
    """Conversion event (e.g., COMPLETE_PAYMENT)."""

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
    ]
    """What this ad group optimizes for on TikTok."""

    pacing: Optional[Literal["PACING_MODE_SMOOTH", "PACING_MODE_FAST"]]
    """Budget pacing (PACING_MODE_SMOOTH, PACING_MODE_FAST)."""

    pangle_audience_package_exclude_ids: Optional[SequenceNotStr[str]]

    pangle_audience_package_include_ids: Optional[SequenceNotStr[str]]

    pangle_block_app_ids: Optional[SequenceNotStr[str]]

    pixel_id: Optional[str]
    """TikTok Pixel ID for conversion tracking."""

    placement_type: Optional[Literal["PLACEMENT_TYPE_AUTOMATIC", "PLACEMENT_TYPE_NORMAL"]]
    """Placement strategy (PLACEMENT_TYPE_AUTOMATIC, PLACEMENT_TYPE_NORMAL)."""

    placements: Optional[SequenceNotStr[str]]
    """Placements (PLACEMENT_TIKTOK, PLACEMENT_PANGLE, etc.)."""

    product_set_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    product_source: Optional[Literal["CATALOG", "STORE", "SHOWCASE"]]

    promotion_type: Optional[str]
    """Promotion type (optimization location)."""

    schedule_end_time: Optional[str]
    """Schedule end time (UTC, YYYY-MM-DD HH:MM:SS)."""

    schedule_start_time: Optional[str]
    """Schedule start time (UTC, YYYY-MM-DD HH:MM:SS)."""

    schedule_type: Optional[Literal["SCHEDULE_START_END", "SCHEDULE_FROM_NOW"]]
    """Schedule type (SCHEDULE_START_END, SCHEDULE_FROM_NOW)."""

    secondary_optimization_event: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    shopping_ads_retargeting_actions_days: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    shopping_ads_retargeting_type: Optional[Literal["OFF", "LAB1", "LAB2", "LAB3", "LAB4", "LAB5"]]

    spending_power: Optional[Literal["ALL", "HIGH"]]

    tiktok_subplacements: Optional[SequenceNotStr[str]]
    """TikTok subplacements (IN_FEED, SEARCH_FEED, etc.)."""

    vertical_sensitivity_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    video_download_disabled: Optional[bool]
    """Represents `true` or `false` values."""

    video_user_actions: Optional[SequenceNotStr[str]]

    view_attribution_window: Optional[Literal["OFF", "ONE_DAY", "SEVEN_DAYS"]]


class PlatformConfig(TypedDict, total=False):
    """Platform-specific ad group configuration."""

    meta: Optional[PlatformConfigMeta]
    """Meta (Facebook/Instagram) ad set configuration."""

    tiktok: Optional[PlatformConfigTiktok]
    """TikTok ad group configuration."""
