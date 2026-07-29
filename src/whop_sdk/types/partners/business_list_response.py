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
    "PayoutPercentages",
    "SecondTierPartner",
    "SecondTierPartnerProfilePicture",
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


class PayoutPercentages(BaseModel):
    """
    The referrer's commission rate for each income source, expressed as a fraction (0.3 = 30%).
    """

    ad_spend: Optional[float] = None
    """Share of the referred business's Whop Ads spend."""

    card_interchange: Optional[float] = None
    """Share of Whop's profit from card interchange."""

    sales: float
    """Share of Whop's profit from product sales."""

    transfer: Optional[float] = None
    """Share of Whop's profit from platform balance transfers."""


class SecondTierPartnerProfilePicture(BaseModel):
    """The user's profile picture."""

    url: str
    """The user's profile picture URL."""


class SecondTierPartner(BaseModel):
    """
    The second-tier partner who earns on this business (referred the first-tier partner). Null if there is no active second-tier partner.
    """

    id: str
    """User ID, prefixed `user_`."""

    name: Optional[str] = None
    """The user's display name."""

    profile_picture: SecondTierPartnerProfilePicture
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
    """Partner business ID."""

    account: Optional[Account] = None
    """Referred account."""

    created_at: datetime
    """When the partner business was created."""

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

    object: Literal["partner_business"]

    owner: Optional[Owner] = None
    """The owner of the referred business."""

    payout_percentages: PayoutPercentages
    """
    The referrer's commission rate for each income source, expressed as a fraction
    (0.3 = 30%).
    """

    referral_expires_at: Optional[datetime] = None
    """When the referral expires."""

    referral_started_at: Optional[datetime] = None
    """When the referral became active."""

    second_tier_partner: Optional[SecondTierPartner] = None
    """
    The second-tier partner who earns on this business (referred the first-tier
    partner). Null if there is no active second-tier partner.
    """

    status: Literal["active", "removed"]
    """Current referral status."""

    volume_usd: VolumeUsd
