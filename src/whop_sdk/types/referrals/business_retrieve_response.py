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
    action: Literal["apply_for_financing", "migrate_from_stripe", "accept_first_payment", "join_whop_university"]
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
    """Business referral ID."""

    account: Optional[Account] = None
    """Referred account."""

    created_at: datetime
    """When the business referral was created."""

    earnings_usd: EarningsUsd

    object: Literal["business_referral"]

    payout_percentage: float
    """Referrer's share of Whop gross profit, as a fraction (0.3 = 30%)."""

    referral_expires_at: Optional[datetime] = None
    """When the referral expires."""

    referral_started_at: Optional[datetime] = None
    """When the referral became active."""

    status: Literal["active", "removed"]
    """Current referral status."""

    volume_usd: VolumeUsd
