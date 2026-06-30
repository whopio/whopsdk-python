# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["AdUpdateParams", "Creative", "SocialAccount"]


class AdUpdateParams(TypedDict, total=False):
    call_to_action: Literal["shop_now", "learn_more", "sign_up", "subscribe", "order_now", "get_offer", "see_details"]
    """The call-to-action button shown on the ad."""

    creatives: Iterable[Creative]
    """The ad's creatives.

    Each entry is an uploaded file id with an optional format; omit format for the
    original/uncropped asset. Replaces a live ad's creative on the platform.
    """

    descriptions: SequenceNotStr[str]
    """The description variants shown on the ad."""

    headlines: SequenceNotStr[str]
    """The headline variants shown on the ad."""

    primary_texts: SequenceNotStr[str]
    """The primary text variants shown in the ad body."""

    social_accounts: Iterable[SocialAccount]
    """The social accounts the ad runs under."""

    title: str
    """The display name of the ad."""

    url: str
    """The URL the ad links to."""

    url_parameters: object
    """Query parameters appended to the destination URL, as a string-to-string map."""


class Creative(TypedDict, total=False):
    id: str

    format: Literal["square", "vertical", "horizontal"]


class SocialAccount(TypedDict, total=False):
    id: str
