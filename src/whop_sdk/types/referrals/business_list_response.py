# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "BusinessListResponse",
    "Account",
    "EarningsUsd",
    "FirstTierPartner",
    "FirstTierPartnerProfilePicture",
    "Owner",
    "OwnerProfilePicture",
    "VolumeUsd",
]


class Account(BaseModel):
    """Referred account."""

    id: str
    """Referred account ID."""

    logo_url: Optional[str] = None
    """Referred account logo URL."""

    route: str
    """Referred account route."""

    title: str
    """Referred account display name."""


class EarningsUsd(BaseModel):
    completed: str
    """Commission already paid out, in USD."""

    pending: str
    """Commission scheduled but not yet paid, in USD."""

    total: str
    """Pending + completed commission, in USD."""


class FirstTierPartnerProfilePicture(BaseModel):
    """The user's profile picture."""

    url: str
    """The user's profile picture URL."""


class FirstTierPartner(BaseModel):
    """The partner who referred the business owner onto Whop (first tier).

    Null if there is no active first-tier partner.
    """

    id: str
    """User ID, prefixed `user_`."""

    name: Optional[str] = None
    """The user's display name."""

    profile_picture: FirstTierPartnerProfilePicture
    """The user's profile picture."""

    username: str
    """The user's unique username."""


class OwnerProfilePicture(BaseModel):
    """The user's profile picture."""

    url: str
    """The user's profile picture URL."""


class Owner(BaseModel):
    """The owner of the referred business."""

    id: str
    """User ID, prefixed `user_`."""

    name: Optional[str] = None
    """The user's display name."""

    profile_picture: OwnerProfilePicture
    """The user's profile picture."""

    username: str
    """The user's unique username."""


class VolumeUsd(BaseModel):
    attributed: str
    """
    Credited GMV (awaiting_settlement + settled); excludes canceled and reversed, in
    USD.
    """

    awaiting_settlement: str
    """GMV awaiting settlement (commission not yet computed), in USD."""

    settled: str
    """GMV of pending + completed payments, in USD."""


class BusinessListResponse(BaseModel):
    id: str
    """Business referral ID."""

    account: Optional[Account] = None
    """Referred account."""

    created_at: datetime
    """When the business referral was created."""

    earnings_usd: EarningsUsd

    first_tier_partner: Optional[FirstTierPartner] = None
    """The partner who referred the business owner onto Whop (first tier).

    Null if there is no active first-tier partner.
    """

    my_partner_tier: Literal["first", "second"]
    """
    Which tier the caller earns on for this business: `first` (they referred the
    owner) or `second` (they referred the first-tier partner).
    """

    object: Literal["business_referral"]

    owner: Optional[Owner] = None
    """The owner of the referred business."""

    payout_percentage: float
    """Referrer's share of Whop gross profit, as a fraction (0.3 = 30%).

    Second-tier referrals earn a flat 0.1.
    """

    referral_expires_at: Optional[datetime] = None
    """When the referral expires."""

    referral_started_at: Optional[datetime] = None
    """When the referral became active."""

    status: Literal["active", "removed"]
    """Current referral status."""

    volume_usd: VolumeUsd
