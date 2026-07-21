# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "BusinessRetrieveResponse",
    "Account",
    "AccountCapabilities",
    "AccountRecommendedAction",
    "AccountRequiredAction",
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


class AccountCapabilities(BaseModel):
    accept_bank_payments: Literal["active", "inactive", "pending"]
    """Bank payins: debits, transfers, and local bank rails"""

    accept_bnpl_payments: Literal["active", "inactive", "pending"]
    """Buy-now-pay-later payins; requires approval"""

    accept_card_payments: Literal["active", "inactive", "pending"]
    """Card payins, including Apple Pay and Google Pay"""

    bank_deposit: Literal["active", "inactive", "pending"]
    """Deposits by bank wire or ACH to the account's virtual bank account"""

    card_deposit: Literal["active", "inactive", "pending"]
    """Balance top-ups by charging a stored payment method"""

    card_issuing: Literal["active", "inactive", "pending"]
    """Issuing Whop cards; requires card application approval"""

    crypto_deposit: Literal["active", "inactive", "pending"]
    """On-chain deposits to the account's crypto wallet"""

    crypto_payout: Literal["active", "inactive", "pending"]
    """On-chain payouts to a crypto wallet"""

    instant_payout: Literal["active", "inactive", "pending"]
    """Instant payouts to an eligible payout destination"""

    standard_payout: Literal["active", "inactive", "pending"]
    """Standard payouts to an external payout destination"""

    transfer: Literal["active", "inactive", "pending"]
    """Transfers to other accounts"""


class AccountRecommendedAction(BaseModel):
    action: Literal[
        "theme_business",
        "create_product",
        "create_plan",
        "verify_identity",
        "connect_affiliate_program",
        "create_promotion",
        "setup_tracking_pixel",
        "migrate_from_stripe",
        "accept_first_payment",
        "launch_first_ad",
        "launch_draft_campaign",
        "increase_ad_budget",
        "refresh_ad_creatives",
        "fix_ad_billing",
        "exclude_customers_from_ads",
        "retarget_abandoned_checkouts",
        "invite_team_member",
        "enable_tax_collection",
        "create_card",
        "join_whop_university",
        "apply_for_financing",
    ]
    """
    The recommendation; new values may be added, so handle unknown actions
    gracefully
    """

    blocked_capabilities: List[str]

    cta: str
    """The URL the call-to-action links to"""

    cta_label: str
    """Button label"""

    description: str
    """Supporting copy, or empty"""

    icon_url: Optional[str] = None
    """Illustration icon URL, or `null`"""

    impact_score: Optional[int] = None
    """Estimated impact from 0-100, or `null` when not ranked"""

    reasoning: Optional[str] = None
    """Why this action was recommended, or `null`"""

    status: Literal["optional"]
    """Always optional — never blocking"""

    title: str
    """Headline for the recommendation"""


class AccountRequiredAction(BaseModel):
    action: Literal["deposit_funds", "submit_information_request", "verify_identity", "connect_fulfillment_tracker"]
    """
    What the holder must do; new values may be added, so handle unknown actions
    gracefully
    """

    blocked_capabilities: List[str]

    cta: Optional[str] = None
    """The URL the call-to-action links to, or null when there is no button"""

    cta_label: str
    """Button label, or empty when there is no button"""

    description: str
    """Supporting copy, or empty"""

    icon_url: Optional[str] = None
    """The URL of the action's illustration icon, or null if it has none"""

    status: Literal["required", "pending"]
    """required (act now) or pending (under review)"""

    title: str
    """Headline for the action"""


class Account(BaseModel):
    """Referred account."""

    id: str
    """Referred account ID."""

    capabilities: Optional[AccountCapabilities] = None

    logo_url: Optional[str] = None
    """Referred account logo URL."""

    recommended_actions: Optional[List[AccountRecommendedAction]] = None
    """Optional actions that unlock capabilities or grow the referred account."""

    required_actions: Optional[List[AccountRequiredAction]] = None
    """Actions the referred account owner must take to unblock capabilities."""

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


class BusinessRetrieveResponse(BaseModel):
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
