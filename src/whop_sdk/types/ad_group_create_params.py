# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "AdGroupCreateParams",
    "Audiences",
    "Demographics",
    "DetailedTargeting",
    "DetailedTargetingBehavior",
    "DetailedTargetingDemographic",
    "DetailedTargetingInterest",
    "Devices",
    "DevicesOperatingSystem",
    "FrequencyCap",
    "PlacementsUnionMember1",
    "Regions",
    "RegionsExclude",
    "RegionsExcludeCity",
    "RegionsExcludeCustomLocation",
    "RegionsExcludeZip",
    "RegionsExcludeZipKey",
    "RegionsInclude",
    "RegionsIncludeCity",
    "RegionsIncludeCustomLocation",
    "RegionsIncludeZip",
    "RegionsIncludeZipKey",
]


class AdGroupCreateParams(TypedDict, total=False):
    ad_campaign_id: Required[str]
    """The ad campaign to create the ad group in, prefixed `adcamp_`."""

    audiences: Audiences
    """Saved audiences to deliver to or exclude.

    Can't be combined with demographics.automatic.
    """

    bid_type: Literal["minimum_cost", "average_target", "maximum_target"]
    """How delivery bids are set in the ad auction.

    Target-based strategies use `desired_cost_per_result`.
    """

    budget_amount: float
    """This ad group's budget, in the ad account's currency.

    Omit when the budget is set on the campaign instead.
    """

    budget_type: Literal["daily", "lifetime"]
    """
    Whether budget_amount is spent per day (`daily`) or over the ad group's full run
    (`lifetime`).
    """

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
    ]
    """The pixel event optimized for.

    A standard event, or any custom pixel event name.
    """

    conversion_location: Literal[
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
    """
    Where the outcome being optimized for occurs, such as a website visit,
    social-profile visit, messaging conversation, ad interaction, or lead-form
    submission. The lead form itself is set on the ad.
    """

    demographics: Demographics
    """Age, gender, and automatic-audience targeting."""

    desired_cost_per_result: float
    """
    Cost per result to aim for (`average_target`) or never exceed
    (`maximum_target`).
    """

    detailed_targeting: DetailedTargeting
    """
    Interest, behavior, and demographic targeting, using categories from the ad
    platform's targeting taxonomy. Entries across interests, behaviors, and
    demographics are OR'd together (anyone matching any entry is reached), matching
    Ads Manager's detailed-targeting box. At most 100 entries per section. Can't be
    combined with demographics.automatic, and unavailable to campaigns with
    special_ad_categories. Send the complete intended state — a section you omit is
    cleared.
    """

    devices: Devices
    """Device platforms and operating systems to target."""

    dynamic_creative: bool
    """
    Let the ad platform automatically mix and match this ad group's creatives and
    copy to find the best-performing combinations. Set at creation; can't be changed
    afterward.
    """

    ends_at: str
    """When the ad group stops delivering, as an ISO 8601 timestamp.

    Omit to run until paused.
    """

    frequency_cap: FrequencyCap
    """Cap on how often one person sees ads from this ad group.

    Only available on campaigns with the `awareness` objective.
    """

    languages: SequenceNotStr[str]
    """Languages to target, as ISO 639 codes such as `en` or `es`.

    Empty or omitted targets all languages.
    """

    message_apps: List[Literal["messenger", "instagram", "whatsapp"]]
    """Apps the conversation opens in.

    Required when setting `conversion_location` to `messaging`, and rejected unless
    the ad group's conversion location is `messaging`.
    """

    minimum_daily_spend: float
    """Minimum the ad group tries to spend each day."""

    optimization_goal: Literal[
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
    """The result the ad group's delivery is optimized to get the most of."""

    placements: Union[Literal["automatic"], Iterable[PlacementsUnionMember1]]
    """
    `automatic` to let the ad platform choose placements, or the list of platforms
    and positions to target. Omit a platform's positions to target all of them.

    Valid positions per platform:

    - `facebook`: `feed`, `right_hand_column`, `marketplace`, `search`,
      `profile_feed`, `notification`, `story`, `instream_video`, `facebook_reels`,
      `facebook_reels_overlay`, `biz_disco_feed`
    - `instagram`: `stream`, `story`, `explore`, `explore_home`, `reels`,
      `profile_feed`, `profile_reels`, `ig_search`
    - `messenger`: `story`
    - `audience_network`: `classic`, `rewarded_video`
    - `threads`: `threads_stream`
    - `whatsapp`: `status`
    """

    regions: Regions
    """Locations to target and exclude."""

    starts_at: str
    """When the ad group starts delivering, as an ISO 8601 timestamp.

    Omit to start as soon as it's active.
    """

    status: Literal["active", "paused"]
    """Initial status (default: `active`)."""

    title: str
    """The display name of the ad group."""


class Audiences(TypedDict, total=False):
    """Saved audiences to deliver to or exclude.

    Can't be combined with demographics.automatic.
    """

    exclude: SequenceNotStr[str]
    """IDs of saved audiences to exclude from delivery, prefixed `adaud_`."""

    include: SequenceNotStr[str]
    """IDs of saved audiences to deliver to, prefixed `adaud_`."""


class Demographics(TypedDict, total=False):
    """Age, gender, and automatic-audience targeting."""

    automatic: bool
    """
    Turn on automatic audience targeting (Advantage+ on Meta): the platform can
    deliver beyond the ages, genders, and detailed targeting you set, treating them
    as suggestions.
    """

    gender: Literal["all", "male", "female"]
    """Gender to target."""

    maximum_age: int
    """Oldest age to target."""

    minimum_age: int
    """Youngest age to target."""


class DetailedTargetingBehavior(TypedDict, total=False):
    id: Required[str]
    """The ad platform's ID for the category in its targeting taxonomy."""

    name: str
    """Category name, such as `Movies`."""


class DetailedTargetingDemographic(TypedDict, total=False):
    id: Required[str]
    """The ad platform's ID for the category in its targeting taxonomy."""

    type: Required[
        Literal[
            "life_events",
            "industries",
            "income",
            "family_statuses",
            "work_employers",
            "work_positions",
            "education_schools",
            "education_majors",
        ]
    ]
    """Kind of demographic the category belongs to."""

    name: str
    """Category name, such as `Recently moved`."""


class DetailedTargetingInterest(TypedDict, total=False):
    id: Required[str]
    """The ad platform's ID for the category in its targeting taxonomy."""

    name: str
    """Category name, such as `Movies`."""


class DetailedTargeting(TypedDict, total=False):
    """
    Interest, behavior, and demographic targeting, using categories from the ad platform's targeting taxonomy. Entries across interests, behaviors, and demographics are OR'd together (anyone matching any entry is reached), matching Ads Manager's detailed-targeting box. At most 100 entries per section. Can't be combined with demographics.automatic, and unavailable to campaigns with special_ad_categories. Send the complete intended state — a section you omit is cleared.
    """

    behaviors: Iterable[DetailedTargetingBehavior]
    """Behavior categories to target, such as frequent travelers."""

    demographics: Iterable[DetailedTargetingDemographic]
    """
    Demographic categories to target, such as life events, industries, work
    employers, job titles, schools, or majors.
    """

    interests: Iterable[DetailedTargetingInterest]
    """Interest categories to target, such as an interest in movies."""


class DevicesOperatingSystem(TypedDict, total=False):
    os: Required[Literal["ios", "android"]]
    """Operating system to target."""

    minimum_version: str
    """Lowest OS version to target, such as `18.0`. Omit to target any version."""


class Devices(TypedDict, total=False):
    """Device platforms and operating systems to target."""

    operating_systems: Iterable[DevicesOperatingSystem]
    """Operating systems to target. Empty targets all operating systems."""

    platforms: List[Literal["mobile", "desktop"]]
    """Device types to target. Empty targets all devices."""


class FrequencyCap(TypedDict, total=False):
    """Cap on how often one person sees ads from this ad group.

    Only available on campaigns with the `awareness` objective.
    """

    maximum_impressions: int
    """Most times one person can be shown ads from this ad group within the window."""

    per_days: int
    """Length of the rolling window, in days."""


class PlacementsUnionMember1(TypedDict, total=False):
    platform: Required[Literal["facebook", "instagram", "messenger", "audience_network", "threads", "whatsapp"]]
    """Platform the ads run on."""

    positions: SequenceNotStr[str]
    """Positions to target within the platform, such as `feed` or `story`.

    Omit to target all of the platform's positions.
    """


class RegionsExcludeCity(TypedDict, total=False):
    key: Required[str]
    """The ad platform's key for the city in its location taxonomy."""

    name: str
    """City name, such as `Austin`."""


class RegionsExcludeCustomLocation(TypedDict, total=False):
    latitude: Required[float]
    """Latitude of the center point."""

    longitude: Required[float]
    """Longitude of the center point."""

    radius: Required[float]
    """Radius around the center point: 1-50 miles or 1-80 kilometers."""

    distance_unit: Literal["mile", "kilometer"]
    """Unit for `radius`. Defaults to `mile`."""

    name: str
    """Label for the location, such as a city or address."""


class RegionsExcludeZipKey(TypedDict, total=False):
    key: Required[str]
    """The ZIP or postal code."""


RegionsExcludeZip: TypeAlias = Union[str, RegionsExcludeZipKey]


class RegionsExclude(TypedDict, total=False):
    """Locations excluded from targeting. Country groups can't be excluded."""

    cities: Iterable[RegionsExcludeCity]
    """Cities, keyed by the ad platform's location taxonomy."""

    countries: SequenceNotStr[str]
    """Countries, as ISO 3166-1 alpha-2 codes such as `US`."""

    country_groups: SequenceNotStr[str]
    """Multi-country groups such as `worldwide` or `europe`.

    Include-only — groups can't be excluded.
    """

    custom_locations: Iterable[RegionsExcludeCustomLocation]
    """Circular areas, each a coordinate plus a radius.

    At most 200 across include and exclude.
    """

    regions: SequenceNotStr[str]
    """US states and DC, as ISO 3166-2 codes such as `US-CA`.

    US territories (`PR`, `GU`, `VI`, `AS`, `MP`) and everywhere outside the US are
    targeted through `countries`.
    """

    zips: SequenceNotStr[RegionsExcludeZip]
    """ZIP and postal codes, as bare strings or objects with a key."""


class RegionsIncludeCity(TypedDict, total=False):
    key: Required[str]
    """The ad platform's key for the city in its location taxonomy."""

    name: str
    """City name, such as `Austin`."""


class RegionsIncludeCustomLocation(TypedDict, total=False):
    latitude: Required[float]
    """Latitude of the center point."""

    longitude: Required[float]
    """Longitude of the center point."""

    radius: Required[float]
    """Radius around the center point: 1-50 miles or 1-80 kilometers."""

    distance_unit: Literal["mile", "kilometer"]
    """Unit for `radius`. Defaults to `mile`."""

    name: str
    """Label for the location, such as a city or address."""


class RegionsIncludeZipKey(TypedDict, total=False):
    key: Required[str]
    """The ZIP or postal code."""


RegionsIncludeZip: TypeAlias = Union[str, RegionsIncludeZipKey]


class RegionsInclude(TypedDict, total=False):
    """Locations the ad group targets."""

    cities: Iterable[RegionsIncludeCity]
    """Cities, keyed by the ad platform's location taxonomy."""

    countries: SequenceNotStr[str]
    """Countries, as ISO 3166-1 alpha-2 codes such as `US`."""

    country_groups: SequenceNotStr[str]
    """Multi-country groups such as `worldwide` or `europe`.

    Include-only — groups can't be excluded.
    """

    custom_locations: Iterable[RegionsIncludeCustomLocation]
    """Circular areas, each a coordinate plus a radius.

    At most 200 across include and exclude.
    """

    regions: SequenceNotStr[str]
    """US states and DC, as ISO 3166-2 codes such as `US-CA`.

    US territories (`PR`, `GU`, `VI`, `AS`, `MP`) and everywhere outside the US are
    targeted through `countries`.
    """

    zips: SequenceNotStr[RegionsIncludeZip]
    """ZIP and postal codes, as bare strings or objects with a key."""


class Regions(TypedDict, total=False):
    """Locations to target and exclude."""

    exclude: RegionsExclude
    """Locations excluded from targeting. Country groups can't be excluded."""

    include: RegionsInclude
    """Locations the ad group targets."""
