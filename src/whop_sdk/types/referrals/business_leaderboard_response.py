# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = [
    "BusinessLeaderboardResponse",
    "Leader",
    "LeaderUser",
    "LeaderUserProfilePicture",
    "Me",
    "MeUser",
    "MeUserProfilePicture",
]


class LeaderUserProfilePicture(BaseModel):
    """The user's profile picture."""

    url: str
    """The user's profile picture URL."""


class LeaderUser(BaseModel):
    """The ranked referrer."""

    id: str
    """User ID, prefixed `user_`."""

    city: Optional[str] = None
    """The city where the user is located, derived from their IP address.

    Null if location sharing is disabled.
    """

    country: Optional[str] = None
    """The country where the user is located, derived from their IP address.

    Null if location sharing is disabled.
    """

    name: Optional[str] = None
    """The user's display name."""

    profile_picture: LeaderUserProfilePicture
    """The user's profile picture."""

    username: str
    """The user's unique username."""


class Leader(BaseModel):
    first_referral_started_at: datetime
    """When the referrer's earliest business referral became active."""

    rank: int
    """1-based leaderboard position."""

    total_earnings_usd: str
    """
    The referrer's pending + completed earnings across all referred businesses, in
    USD.
    """

    total_volume_usd: str
    """Credited GMV across all the referrer's referred businesses, in USD."""

    user: Optional[LeaderUser] = None
    """The ranked referrer."""


class MeUserProfilePicture(BaseModel):
    """The user's profile picture."""

    url: str
    """The user's profile picture URL."""


class MeUser(BaseModel):
    """The ranked referrer."""

    id: str
    """User ID, prefixed `user_`."""

    city: Optional[str] = None
    """The city where the user is located, derived from their IP address.

    Null if location sharing is disabled.
    """

    country: Optional[str] = None
    """The country where the user is located, derived from their IP address.

    Null if location sharing is disabled.
    """

    name: Optional[str] = None
    """The user's display name."""

    profile_picture: MeUserProfilePicture
    """The user's profile picture."""

    username: str
    """The user's unique username."""


class Me(BaseModel):
    """The caller's own standing; null when the caller has no referral earnings."""

    first_referral_started_at: datetime
    """When the referrer's earliest business referral became active."""

    rank: int
    """1-based leaderboard position."""

    total_earnings_usd: str
    """
    The referrer's pending + completed earnings across all referred businesses, in
    USD.
    """

    total_volume_usd: str
    """Credited GMV across all the referrer's referred businesses, in USD."""

    user: Optional[MeUser] = None
    """The ranked referrer."""


class BusinessLeaderboardResponse(BaseModel):
    leaders: List[Leader]
    """The top referrers by total earnings, best first."""

    me: Optional[Me] = None
    """The caller's own standing; null when the caller has no referral earnings."""
