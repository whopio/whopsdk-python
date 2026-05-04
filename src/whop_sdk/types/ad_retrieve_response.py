# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "AdRetrieveResponse",
    "ExternalAdCreativeSet",
    "ExternalAdGroup",
    "PlatformConfig",
    "PlatformConfigMetaAdPlatformConfigType",
    "PlatformConfigTiktokAdPlatformConfigType",
]


class ExternalAdCreativeSet(BaseModel):
    """The creative set used by this ad."""

    id: str
    """The unique identifier for the external ad creative set."""


class ExternalAdGroup(BaseModel):
    """The parent ad group."""

    id: str
    """The unique identifier for the external ad group."""

    name: Optional[str] = None
    """Human-readable ad group name"""

    status: Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]
    """Current operational status of the ad group"""


class PlatformConfigMetaAdPlatformConfigType(BaseModel):
    """Meta (Facebook/Instagram) ad configuration."""

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
        ]
    ] = None

    headline: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    instagram_actor_id: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    link_url: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    name: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    page_id: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    platform: Literal["meta", "tiktok"]
    """The ad platform."""

    primary_text: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    typename: Literal["MetaAdPlatformConfigType"]
    """The typename of this object"""

    url_tags: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """


class PlatformConfigTiktokAdPlatformConfigType(BaseModel):
    """TikTok ad configuration."""

    ad_format: Optional[Literal["SINGLE_IMAGE", "SINGLE_VIDEO", "CAROUSEL_ADS", "CATALOG_CAROUSEL", "LIVE_CONTENT"]] = (
        None
    )

    ad_name: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    ad_text: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

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
    ] = None
    """TikTok call-to-action button text. See docs/tiktok_api/ad.md § call_to_action."""

    identity_authorized_bc_id: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    identity_id: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    identity_type: Optional[Literal["CUSTOMIZED_USER", "AUTH_CODE", "TT_USER", "BC_AUTH_TT"]] = None

    image_ids: Optional[List[str]] = None

    landing_page_url: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """

    platform: Literal["meta", "tiktok"]
    """The ad platform."""

    typename: Literal["TiktokAdPlatformConfigType"]
    """The typename of this object"""

    video_id: Optional[str] = None
    """Represents textual data as UTF-8 character sequences.

    This type is most often used by GraphQL to represent free-form human-readable
    text.
    """


PlatformConfig: TypeAlias = Annotated[
    Union[Optional[PlatformConfigMetaAdPlatformConfigType], Optional[PlatformConfigTiktokAdPlatformConfigType]],
    PropertyInfo(discriminator="typename"),
]


class AdRetrieveResponse(BaseModel):
    """An ad belonging to an ad group"""

    id: str
    """Unique identifier for the ad."""

    created_at: datetime
    """When the ad was created."""

    external_ad_creative_set: Optional[ExternalAdCreativeSet] = None
    """The creative set used by this ad."""

    external_ad_group: ExternalAdGroup
    """The parent ad group."""

    platform_config: PlatformConfig
    """Typed platform-specific configuration."""

    status: Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]
    """Current status of the ad."""

    updated_at: datetime
    """When the ad was last updated."""
