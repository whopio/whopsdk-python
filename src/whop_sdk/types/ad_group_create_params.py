# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AdGroupCreateParams"]


class AdGroupCreateParams(TypedDict, total=False):
    ad_campaign_id: Required[str]
    """The ad campaign to create the ad group in."""

    audiences: object
    """Saved-audience targeting: { include, exclude } arrays of audience IDs.

    Incompatible with demographics.automatic (Advantage+).
    """

    bid_type: Literal["minimum_cost", "average_target", "maximum_target"]
    """Bid strategy."""

    budget_amount: float
    """Ad-set budget in dollars (ABO only; omit under CBO)."""

    budget_type: Literal["daily", "lifetime"]
    """Whether the budget is daily or lifetime."""

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
        "messaging",
        "on_ad",
        "instant_forms",
        "instant_forms_and_messenger",
        "website_and_instant_forms",
    ]
    """
    Where results happen: website (conversions), profile (IG/FB engagement),
    messaging (DM), on_ad (engagement on the ad, surface follows the optimization
    goal), or the lead destinations (instant_forms, instant_forms_and_messenger,
    website_and_instant_forms). The lead form itself is set on the ad.
    """

    demographics: object
    """Demographic targeting: { automatic, minimum_age, maximum_age, gender }."""

    desired_cost_per_result: float
    """Target/cap cost for average_target / maximum_target."""

    devices: object
    """Device targeting: { platforms, operating_systems: [{ os, minimum_version }] }."""

    dynamic_creative: bool
    """Run Meta dynamic (Advantage+) creative for this ad set.

    Set at creation; immutable afterward.
    """

    ends_at: str
    """Schedule end, ISO 8601."""

    frequency_cap: object
    """{ maximum_impressions, per_days } — only valid for reach optimization."""

    languages: SequenceNotStr[str]
    """Languages to target as ISO 639 codes (e.g.

    en, es). Empty/omitted = all languages.
    """

    message_apps: List[Literal["messenger", "instagram", "whatsapp"]]
    """Required when conversion_location is messaging: which apps to message on.

    Combinations map to the matching Meta destination.
    """

    minimum_daily_spend: float
    """Daily spend floor within the budget."""

    optimization_goal: str
    """What the ad group optimizes for (e.g. conversions, link_clicks, reach)."""

    placements: object
    """'automatic' (Advantage+) or a list of { platform, positions }.

    Omit positions to target all of a platform's.

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

    regions: object
    """
    Geo targeting: { include / exclude: { countries (ISO 3166-1), regions
    (states/provinces as ISO 3166-2, e.g. US-CA), cities (keyed), zips,
    custom_locations } }. custom_locations entries are pin + radius: { latitude,
    longitude, radius, distance_unit ('mile' default, or 'kilometer'), name
    (optional display label) }. Radius must be 1-50 miles or 1-80 km; at most 200
    custom locations across include and exclude.
    """

    starts_at: str
    """Schedule start, ISO 8601."""

    status: Literal["active", "paused"]
    """Initial status (default: active)."""

    title: str
    """The display name of the ad group."""
