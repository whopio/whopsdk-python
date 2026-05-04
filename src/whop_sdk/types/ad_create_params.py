# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "AdCreateParams",
    "PlatformConfig",
    "PlatformConfigMeta",
    "PlatformConfigMetaCarouselCard",
    "PlatformConfigTiktok",
]


class AdCreateParams(TypedDict, total=False):
    ad_group_id: Required[str]
    """The unique identifier of the ad group to create this ad in."""

    creative_set_id: Optional[str]
    """The unique identifier of the creative set to use."""

    existing_instagram_media_id: Optional[str]
    """
    ID of an existing Instagram media item to use as the ad creative (instead of a
    creative set or Facebook post).
    """

    existing_post_id: Optional[str]
    """
    ID of an existing Facebook post to use as the ad creative (instead of a creative
    set).
    """

    platform_config: Optional[PlatformConfig]
    """Platform-specific configuration. Must match the campaign platform."""

    status: Optional[Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]]
    """The status of an external ad."""


class PlatformConfigMetaCarouselCard(TypedDict, total=False):
    """Per-card configuration for a carousel ad."""

    call_to_action_type: Optional[str]
    """CTA button type (e.g., SHOP_NOW, LEARN_MORE)."""

    description: Optional[str]
    """Card description (max 30 chars recommended)."""

    link: Optional[str]
    """Destination URL for this card (defaults to ad destination)."""

    name: Optional[str]
    """Card title (max 35 chars recommended)."""


class PlatformConfigMeta(TypedDict, total=False):
    """Configuration for Meta (Facebook/Instagram) ads."""

    call_to_action_type: Optional[
        Literal[
            "LEARN_MORE",
            "SHOP_NOW",
            "SIGN_UP",
            "SUBSCRIBE",
            "GET_STARTED",
            "BOOK_NOW",
            "APPLY_NOW",
            "CONTACT_US",
            "DOWNLOAD",
            "ORDER_NOW",
            "BUY_NOW",
            "GET_QUOTE",
            "MESSAGE_PAGE",
            "WHATSAPP_MESSAGE",
            "INSTAGRAM_MESSAGE",
            "CALL_NOW",
            "GET_DIRECTIONS",
            "SEND_UPDATES",
            "GET_OFFER",
            "WATCH_MORE",
            "LISTEN_NOW",
            "PLAY_GAME",
            "OPEN_LINK",
            "NO_BUTTON",
            "GET_OFFER_VIEW",
            "GET_EVENT_TICKETS",
            "SEE_MENU",
            "REQUEST_TIME",
            "EVENT_RSVP",
            "SEE_DETAILS",
        ]
    ]
    """Call-to-action button type."""

    carousel_cards: Optional[Iterable[PlatformConfigMetaCarouselCard]]
    """Per-card carousel config."""

    description: Optional[str]
    """Description of the ad creative (legacy single-value)."""

    descriptions: Optional[SequenceNotStr[str]]
    """Up to 5 description variants, rendered via Meta asset_feed_spec."""

    existing_instagram_media_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    existing_post_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    headline: Optional[str]
    """Headline of the ad creative (legacy single-value)."""

    headlines: Optional[SequenceNotStr[str]]
    """Up to 5 headline variants, rendered via Meta asset_feed_spec."""

    instagram_actor_id: Optional[str]
    """Unique identifier of the Instagram account."""

    lead_form_config: Optional[Dict[str, object]]
    """Lead generation form configuration (JSON)."""

    link_url: Optional[str]
    """Destination URL."""

    multi_advertiser_enrollment: Optional[Literal["OPT_IN", "OPT_OUT"]]

    name: Optional[str]
    """Ad name."""

    page_id: Optional[str]
    """Unique identifier of the Facebook Page."""

    page_welcome_message: Optional[Dict[str, object]]
    """Messenger welcome message / ice-breaker template (JSON)."""

    primary_text: Optional[str]
    """Primary text of the ad creative (legacy single-value)."""

    primary_texts: Optional[SequenceNotStr[str]]
    """Up to 5 primary-text variants, rendered via Meta asset_feed_spec."""

    url_tags: Optional[str]
    """URL query parameters appended to the destination link."""


class PlatformConfigTiktok(TypedDict, total=False):
    """Configuration for TikTok ads."""

    access_pass_tag: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    ad_format: Optional[Literal["SINGLE_IMAGE", "SINGLE_VIDEO", "CAROUSEL_ADS", "CATALOG_CAROUSEL", "LIVE_CONTENT"]]
    """
    Ad format (SINGLE_IMAGE, SINGLE_VIDEO, CAROUSEL_ADS, CATALOG_CAROUSEL,
    LIVE_CONTENT).
    """

    ad_name: Optional[str]
    """Ad name."""

    ad_text: Optional[str]
    """Ad copy (single variant)."""

    ad_texts: Optional[SequenceNotStr[str]]
    """Ad copy variants for search ads (up to 5)."""

    aigc_disclosure_type: Optional[Literal["UNSET", "CONTAINS_AIGC", "IS_AIGC", "NOT_AIGC"]]
    """Whether the ad creative is AI-generated content.

    See docs/tiktok_api/ad.md § aigc_disclosure_type.
    """

    auto_disclaimer_types: Optional[SequenceNotStr[str]]
    """Automatic disclaimer categories (e.g., FINANCE, ALCOHOL)."""

    automate_creative_enabled: Optional[bool]
    """Represents `true` or `false` values."""

    brand_safety_postbid_partner: Optional[Literal["UNSET", "IAS", "DOUBLE_VERIFY", "OPEN_SLATE", "ZEFR"]]
    """Post-bid brand-safety vendor.

    See docs/tiktok_api/ad.md § brand_safety_postbid_partner.
    """

    brand_safety_vast_url: Optional[str]
    """VAST URL for brand safety measurement."""

    call_to_action: Optional[
        Literal[
            "LEARN_MORE",
            "DOWNLOAD",
            "SHOP_NOW",
            "SIGN_UP",
            "CONTACT_US",
            "APPLY_NOW",
            "BOOK_NOW",
            "PLAY_GAME",
            "WATCH_NOW",
            "READ_MORE",
            "VIEW_NOW",
            "GET_QUOTE",
            "ORDER_NOW",
            "INSTALL_NOW",
            "GET_SHOWTIMES",
            "LISTEN_NOW",
            "INTERESTED",
            "SUBSCRIBE",
            "GET_TICKETS_NOW",
            "EXPERIENCE_NOW",
            "PRE_ORDER_NOW",
            "VISIT_STORE",
        ]
    ]
    """TikTok call-to-action button text. See docs/tiktok_api/ad.md § call_to_action."""

    call_to_action_enabled: Optional[bool]
    """Represents `true` or `false` values."""

    call_to_action_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    call_to_action_mode: Optional[Literal["STANDARD", "DYNAMIC"]]
    """How the call-to-action text is chosen.

    STANDARD uses a single fixed CTA; DYNAMIC lets TikTok rotate through a set of
    CTAs to maximize performance.
    """

    card_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    carousel_image_index: Optional[int]
    """Represents non-fractional signed whole numeric values.

    Int can represent values between -(2^31) and 2^31 - 1.
    """

    catalog_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    click_tracking_url: Optional[str]
    """Third-party click tracker URL."""

    cpp_url: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    creative_authorized: Optional[bool]
    """
    Whether the creator has authorized the use of this creative for paid promotion
    (Spark Ads).
    """

    creative_auto_enhancement_strategy_list: Optional[SequenceNotStr[str]]

    dark_post_status: Optional[Literal["ON", "OFF"]]

    deeplink: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    deeplink_format_type: Optional[Literal["UNSET", "DEEPLINK", "DEFERRED_DEEPLINK"]]
    """How the ad's deeplink is resolved.

    See docs/tiktok_api/ad.md § deeplink_format_type.
    """

    deeplink_type: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    deeplink_utm_params: Optional[Iterable[Dict[str, object]]]
    """UTM params appended to the deeplink."""

    disclaimer_clickable_texts: Optional[Iterable[Dict[str, object]]]
    """Clickable disclaimer segments (text + url)."""

    disclaimer_text: Optional[str]
    """Plain text shown when disclaimer_type is DISCLAIMER_TEXT / DISCLAIMER_WITH_URL."""

    disclaimer_type: Optional[Literal["NONE", "DISCLAIMER_TEXT", "DISCLAIMER_WITH_URL"]]
    """Ad disclaimer mode. See docs/tiktok_api/ad.md § disclaimer_type."""

    dynamic_destination: Optional[str]
    """Dynamic destination strategy for shopping ads."""

    dynamic_format: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    end_card_cta: Optional[str]
    """End-card CTA text for video ads."""

    fallback_type: Optional[Literal["UNSET", "APP_STORE", "LANDING_PAGE"]]
    """Destination fallback when a deferred deeplink cannot open the app.

    See docs/tiktok_api/ad.md § fallback_type.
    """

    identity_authorized_bc_id: Optional[str]
    """Business Center ID (required when identity_type is BC_AUTH_TT)."""

    identity_id: Optional[str]
    """Unique identifier of the identity."""

    identity_type: Optional[Literal["CUSTOMIZED_USER", "AUTH_CODE", "TT_USER", "BC_AUTH_TT"]]
    """Identity type."""

    image_ids: Optional[SequenceNotStr[str]]
    """Unique identifiers of the images."""

    impression_tracking_url: Optional[str]
    """Third-party impression tracker URL."""

    item_duet_status: Optional[Literal["ENABLE", "DISABLE"]]

    item_group_ids: Optional[SequenceNotStr[str]]

    item_stitch_status: Optional[Literal["ENABLE", "DISABLE"]]

    landing_page_url: Optional[str]
    """Landing page URL."""

    link_url: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    music_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    page_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    product_display_field_list: Optional[SequenceNotStr[str]]
    """Fields displayed on dynamic product cards."""

    product_set_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    product_specific_type: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    promotional_music_disabled: Optional[bool]
    """Represents `true` or `false` values."""

    shopping_ads_fallback_type: Optional[Literal["UNSET", "LANDING_PAGE", "STORE"]]
    """Fallback destination for shopping ads when the primary target is unavailable.

    See docs/tiktok_api/ad.md § shopping_ads_fallback_type.
    """

    shopping_ads_video_package_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    showcase_products: Optional[Iterable[Dict[str, object]]]

    sku_ids: Optional[SequenceNotStr[str]]

    tiktok_item_id: Optional[str]
    """TikTok item ID for Spark Ads (promotes an organic post)."""

    tracking_app_id: Optional[str]
    """TikTok MMP-tracked app ID."""

    tracking_message_event_set_id: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    tracking_offline_event_set_ids: Optional[SequenceNotStr[str]]
    """Offline event set IDs for attribution."""

    tracking_pixel_id: Optional[str]
    """TikTok pixel ID used for conversion tracking on this ad."""

    utm_params: Optional[Iterable[Dict[str, object]]]

    vertical_video_strategy: Optional[str]
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    video_id: Optional[str]
    """Unique identifier of the video."""

    video_view_tracking_url: Optional[str]
    """Third-party video-view tracker URL."""

    viewability_postbid_partner: Optional[Literal["UNSET", "IAS", "DOUBLE_VERIFY", "MOAT"]]
    """Post-bid viewability measurement partner.

    See docs/tiktok_api/ad.md § viewability_postbid_partner.
    """

    viewability_vast_url: Optional[str]
    """VAST URL for viewability measurement."""


class PlatformConfig(TypedDict, total=False):
    """Platform-specific configuration. Must match the campaign platform."""

    meta: Optional[PlatformConfigMeta]
    """Configuration for Meta (Facebook/Instagram) ads."""

    tiktok: Optional[PlatformConfigTiktok]
    """Configuration for TikTok ads."""
