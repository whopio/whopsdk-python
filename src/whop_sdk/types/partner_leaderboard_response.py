# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "PartnerLeaderboardResponse",
    "Leader",
    "LeaderUser",
    "LeaderUserProfilePicture",
    "Me",
    "MeUser",
    "MeUserProfilePicture",
]


class LeaderUserProfilePicture(BaseModel):
    """The user's profile picture. Present only on the caller's own entry."""

    url: str
    """The user's profile picture URL."""


class LeaderUser(BaseModel):
    """The ranked referrer.

    Identity fields (id, name, username, profile_picture) are returned only on the caller's own entry; other referrers expose coarse location only.
    """

    city: Optional[str] = None
    """The city where the referrer is located, derived from their IP address.

    Null if location sharing is disabled.
    """

    country: Optional[str] = None
    """The country where the referrer is located, derived from their IP address.

    Null if location sharing is disabled.
    """

    id: Optional[str] = None
    """User ID, prefixed `user_`. Present only on the caller's own entry."""

    name: Optional[str] = None
    """The user's display name. Present only on the caller's own entry."""

    profile_picture: Optional[LeaderUserProfilePicture] = None
    """The user's profile picture. Present only on the caller's own entry."""

    username: Optional[str] = None
    """The user's unique username. Present only on the caller's own entry."""


class Leader(BaseModel):
    first_referral_started_at: datetime
    """When the referrer's earliest partner business became active."""

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
    """The ranked referrer.

    Identity fields (id, name, username, profile_picture) are returned only on the
    caller's own entry; other referrers expose coarse location only.
    """


class MeUserProfilePicture(BaseModel):
    """The user's profile picture. Present only on the caller's own entry."""

    url: str
    """The user's profile picture URL."""


class MeUser(BaseModel):
    """The ranked referrer.

    Identity fields (id, name, username, profile_picture) are returned only on the caller's own entry; other referrers expose coarse location only.
    """

    city: Optional[str] = None
    """The city where the referrer is located, derived from their IP address.

    Null if location sharing is disabled.
    """

    country: Optional[str] = None
    """The country where the referrer is located, derived from their IP address.

    Null if location sharing is disabled.
    """

    id: Optional[str] = None
    """User ID, prefixed `user_`. Present only on the caller's own entry."""

    name: Optional[str] = None
    """The user's display name. Present only on the caller's own entry."""

    profile_picture: Optional[MeUserProfilePicture] = None
    """The user's profile picture. Present only on the caller's own entry."""

    username: Optional[str] = None
    """The user's unique username. Present only on the caller's own entry."""


class Me(BaseModel):
    """The caller's own standing; null when the caller has no referral earnings."""

    first_referral_started_at: datetime
    """When the referrer's earliest partner business became active."""

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
    """The ranked referrer.

    Identity fields (id, name, username, profile_picture) are returned only on the
    caller's own entry; other referrers expose coarse location only.
    """


class PartnerLeaderboardResponse(BaseModel):
    leaders: List[Leader]
    """The top referrers by total earnings, best first."""

    me: Optional[Me] = None
    """The caller's own standing; null when the caller has no referral earnings."""
