# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SocialAccountPost"]


class SocialAccountPost(BaseModel):
    id: str
    """The platform's own identifier for the post or media.

    Use it to reference the post on an ad.
    """

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
    """
    The post's call-to-action button, for example shop_now (Facebook only; null for
    Instagram and TikTok).
    """

    destination_url: Optional[str] = None
    """
    The URL the post's call-to-action drives to (Facebook only; null for Instagram
    and TikTok).
    """

    embed_url: Optional[str] = None
    """
    An iframe-embeddable URL for previewing the post inline (the platform's player
    or post embed). For TikTok this is the only preview, since media_url is null;
    for Facebook and Instagram it supplements media_url. Null when no public embed
    is available.
    """

    media_url: Optional[str] = None
    """
    The URL of the post's media — the image for image posts, the playable video file
    for video posts. Null for TikTok, which exposes no raw file (use embed_url).
    Meta URLs are signed and expire after roughly 24 hours, so don't store them.
    """

    thumbnail_url: Optional[str] = None
    """
    Poster image for video posts (always set for TikTok, which is video-only); null
    for image posts, where media_url is already the image.
    """
