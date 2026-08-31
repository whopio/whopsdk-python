# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "User",
    "Balance",
    "BalanceBusiness",
    "BalanceCash",
    "BalanceCrypto",
    "BalanceCryptoBreakdown",
    "BalanceCryptoBreakdownPendingSettlement",
    "BalanceHistory",
    "BalanceHistoryData",
    "Banner",
    "EarningsUsd",
    "EarningsUsdOwnedAccounts",
    "EarningsUsdPartners",
    "EarningsUsdPersonal",
    "EarningsUsdTotal",
    "ProfilePicture",
    "SocialAccount",
    "SocialAccountParentSocialAccount",
    "Staff",
]


class BalanceBusiness(BaseModel):
    """Account balances for accounts the user owns, highest balance first.

    Excludes accounts with no balance.
    """

    id: str
    """The account ID, which looks like biz\\__******\\********."""

    balance_usd: str
    """The account's total balance in USD."""

    logo_url: Optional[str] = None
    """The account's logo URL."""

    name: Optional[str] = None
    """The account's display name."""


class BalanceCash(BaseModel):
    """Per-currency fiat cash balances."""

    balance: float
    """Available balance in the native currency."""

    balance_usd: float
    """Available balance converted to USD."""

    currency: str
    """Lowercase ISO currency code, such as `usd` or `eur`."""

    in_transit_balance_usd: float
    """Balance moving to the user's own wallet or card, converted to USD."""

    pending_balance_usd: float
    """Pending balance converted to USD."""

    price_usd: Optional[float] = None
    """
    USD price per native currency unit, or `null` when no exchange rate is
    available.
    """

    reserve_balance_usd: float
    """Reserved balance converted to USD."""

    total_withdrawable_balance: float
    """Withdrawable amount in the native currency."""


class BalanceCryptoBreakdownPendingSettlement(BaseModel):
    """When the pending amount is expected to settle, one entry per day, earliest first.

    Money with no scheduled settlement day, such as a transfer in flight, is left out — so these can sum to less than `pending`, never more.
    """

    amount: str
    """Amount expected that day, in native units, as a decimal string."""

    date: str
    """The day this money is expected to finish settling, as an ISO 8601 date."""


class BalanceCryptoBreakdown(BaseModel):
    """
    Balance split into available, pending, in-transit, and reserve amounts, as native-unit decimal strings. Transfers between the user's own wallet and card are reported in `in_transit` until they arrive.
    """

    available: str
    """
    Amount you can spend, send, or withdraw now, in native units, as a decimal
    string.
    """

    in_transit: str
    """
    Amount moving between the account's own destinations, such as a treasury sweep
    to its crypto wallet or a card top-up. In native units, as a decimal string.
    """

    pending: str
    """
    Amount from recent payments still settling, in native units, as a decimal
    string.
    """

    pending_settlements: List[BalanceCryptoBreakdownPendingSettlement]

    reserve: str
    """Amount held back, in native units, as a decimal string.

    Retrieve the account's reserves for why it is held and when it unlocks.
    """


class BalanceCrypto(BaseModel):
    """Per-token crypto holdings in the ledger's own wallet."""

    balance: str
    """Amount held in native token units, as a decimal string."""

    breakdown: BalanceCryptoBreakdown
    """
    Balance split into available, pending, in-transit, and reserve amounts, as
    native-unit decimal strings. Transfers between the user's own wallet and card
    are reported in `in_transit` until they arrive.
    """

    icon_url: Optional[str] = None
    """Token icon URL."""

    name: Optional[str] = None
    """The token's display name."""

    price_usd: Optional[float] = None
    """USD price per token, or `null` when unknown."""

    symbol: str
    """Token display symbol, such as `USDT`, `XAUT`, or `cbBTC`."""

    value_usd: float
    """Holding USD value."""


class Balance(BaseModel):
    """
    The user's balance: personal cash + crypto + in-flight treasury deposits, plus account balances for accounts they own. Computed only on the self view (retrieved with the reserved id `me`) for callers with balance-read scope; `null` otherwise.
    """

    businesses: List[BalanceBusiness]

    businesses_total_usd: str
    """Combined USD balance across every account the user owns."""

    cash: List[BalanceCash]

    cash_usd: str
    """Fiat cash in USD, including pending, in-transit, and reserve."""

    crypto: List[BalanceCrypto]

    crypto_usd: str
    """Crypto holdings in USD."""

    pending_usd: str
    """Fiat pending and in-transit balances, plus in-flight treasury deposits, in USD."""

    total_usd: str
    """
    The user's personal balance in USD: cash (available + pending + in-transit +
    reserve) + crypto + in-flight treasury deposits. Excludes account balances (see
    businesses_total_usd).
    """

    treasury_pending_usd: str
    """Balance-to-wallet USDT0 payouts still in flight, in USD."""


class BalanceHistoryData(BaseModel):
    """Cumulative balance points over the requested window, oldest first."""

    t: int
    """Point timestamp, in Unix seconds."""

    v: float
    """Cumulative wallet balance at this point, in USD."""


class BalanceHistory(BaseModel):
    """
    The user's cumulative wallet balance over time (USD `{ t, v }` points plus last/min/max), for the balance chart. Opt in with `include_balance_history=true` when retrieving yourself with the reserved id `me`; populated only for callers with balance-read scope and `null` otherwise. A user with no wallet activity returns an empty series.
    """

    data: List[BalanceHistoryData]

    last: float
    """Value of the most recent point, in USD."""

    max: float
    """Maximum value across the window, in USD."""

    min: float
    """Minimum value across the window, in USD."""


class Banner(BaseModel):
    """The user's profile banner wrapper. `null` when the user has no banner."""

    url: str
    """Profile banner image URL."""


class EarningsUsdOwnedAccounts(BaseModel):
    """Gross income from accounts the user owns or is owner-authorized on."""

    last_24_hours: str
    """Gross income in USD over the last 24 hours."""

    last_30_days: str
    """Gross income in USD over the last 30 days."""

    last_7_days: str
    """Gross income in USD over the last 7 days."""

    lifetime: str
    """All-time gross income in USD."""


class EarningsUsdPartners(BaseModel):
    """Partner commissions posted to the user's wallet.

    Pending Partner payouts are excluded until they post; later reversals do not reduce gross income.
    """

    last_24_hours: str
    """Gross income in USD over the last 24 hours."""

    last_30_days: str
    """Gross income in USD over the last 30 days."""

    last_7_days: str
    """Gross income in USD over the last 7 days."""

    lifetime: str
    """All-time gross income in USD."""


class EarningsUsdPersonal(BaseModel):
    """Gross income from the user's personal wallet."""

    last_24_hours: str
    """Gross income in USD over the last 24 hours."""

    last_30_days: str
    """Gross income in USD over the last 30 days."""

    last_7_days: str
    """Gross income in USD over the last 7 days."""

    lifetime: str
    """All-time gross income in USD."""


class EarningsUsdTotal(BaseModel):
    """
    Gross income from the user's personal wallet plus accounts they own or are owner-authorized on.
    """

    last_24_hours: str
    """Gross income in USD over the last 24 hours."""

    last_30_days: str
    """Gross income in USD over the last 30 days."""

    last_7_days: str
    """Gross income in USD over the last 7 days."""

    lifetime: str
    """All-time gross income in USD."""


class EarningsUsd(BaseModel):
    """The user's gross USD income over time, including a Partner commission breakdown.

    Populated only on single-user self reads for callers with balance-read scope; `null` otherwise.
    """

    first_earned_at: Optional[str] = None
    """The first time the user earned gross income, as an ISO 8601 timestamp."""

    owned_accounts: EarningsUsdOwnedAccounts
    """Gross income from accounts the user owns or is owner-authorized on."""

    partners: EarningsUsdPartners
    """Partner commissions posted to the user's wallet.

    Pending Partner payouts are excluded until they post; later reversals do not
    reduce gross income.
    """

    personal: EarningsUsdPersonal
    """Gross income from the user's personal wallet."""

    total: EarningsUsdTotal
    """
    Gross income from the user's personal wallet plus accounts they own or are
    owner-authorized on.
    """


class ProfilePicture(BaseModel):
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when the user set no picture.
    """

    url: str
    """Avatar image URL.

    Always present — a generated placeholder when the user set no picture.
    """


class SocialAccountParentSocialAccount(BaseModel):
    """
    The social account this one belongs to on the platform, such as the Facebook page that owns an Instagram account. Null when the social account stands on its own.
    """

    id: str
    """Social account ID, prefixed `sacc_`."""

    external_id: Optional[str] = None
    """The platform-specific ID for the parent social account."""

    name: Optional[str] = None
    """The display name of the parent social account on the platform."""

    platform: Literal["x", "instagram", "youtube", "tiktok", "facebook", "discord", "telegram"]
    """The platform the parent social account exists on."""

    profile_picture_url: Optional[str] = None
    """The URL where the profile picture of the parent social account can be accessed."""

    username: Optional[str] = None
    """The username of the parent social account on the platform."""

    verified: bool
    """Whether the parent social account is verified on the platform."""


class SocialAccount(BaseModel):
    """Social accounts linked to the user (Discord, X/Twitter, Telegram), oldest first.

    Reading your own profile returns every linked account; other profiles only include what is public on Whop (the primary Discord and the X account). Empty when none are linked.
    """

    id: str
    """Unique identifier for the social account."""

    error: Optional[str] = None
    """
    Why this social account currently can't be used for advertising — a failed share
    or a Meta-side restriction. Null when the account is healthy.
    """

    external_id: Optional[str] = None
    """The platform-specific ID for this social account."""

    name: Optional[str] = None
    """The display name of the social account on the platform."""

    parent_social_account: Optional[SocialAccountParentSocialAccount] = None
    """
    The social account this one belongs to on the platform, such as the Facebook
    page that owns an Instagram account. Null when the social account stands on its
    own.
    """

    platform: Literal["x", "instagram", "youtube", "tiktok", "facebook", "discord", "telegram"]
    """The platform the social account exists on."""

    profile_picture_url: Optional[str] = None
    """The URL where the profile picture of the social account can be accessed."""

    scopes: List[str]

    url: Optional[str] = None
    """The URL where the social account can be accessed on the platform.

    Null while a Whop-owned page is still being provisioned.
    """

    username: Optional[str] = None
    """The username of the social account on the platform.

    Null while a Whop-owned page is still being provisioned.
    """

    verified: bool
    """Whether the social account is verified on the platform."""


class Staff(BaseModel):
    """Whop staff access flags.

    Populated only on the self view (retrieved with the reserved id `me`) for callers with staff-read scope; `null` there for every user who is not Whop staff, and always `null` elsewhere.
    """

    admin: bool
    """Whether the user holds the admin staff role with a valid second factor."""

    investigation_access: bool
    """
    Whether the user can open Whop-internal investigation tooling right now: a
    qualifying staff role plus their investigation toggle switched on.
    """

    manager: bool
    """Whether the user holds the manager staff role with a valid second factor."""

    support: bool
    """Whether the user holds the support staff role with a valid second factor."""


class User(BaseModel):
    id: str
    """User ID, prefixed `user_`."""

    balance: Optional[Balance] = None
    """
    The user's balance: personal cash + crypto + in-flight treasury deposits, plus
    account balances for accounts they own. Computed only on the self view
    (retrieved with the reserved id `me`) for callers with balance-read scope;
    `null` otherwise.
    """

    balance_history: Optional[BalanceHistory] = None
    """
    The user's cumulative wallet balance over time (USD `{ t, v }` points plus
    last/min/max), for the balance chart. Opt in with `include_balance_history=true`
    when retrieving yourself with the reserved id `me`; populated only for callers
    with balance-read scope and `null` otherwise. A user with no wallet activity
    returns an empty series.
    """

    banner: Optional[Banner] = None
    """The user's profile banner wrapper. `null` when the user has no banner."""

    bio: Optional[str] = None
    """The user's biography"""

    created_at: str
    """When the user was created, as an ISO 8601 timestamp"""

    earnings_usd: Optional[EarningsUsd] = None
    """The user's gross USD income over time, including a Partner commission breakdown.

    Populated only on single-user self reads for callers with balance-read scope;
    `null` otherwise.
    """

    email: Optional[str] = None
    """The user's email address.

    Populated only on the self view (retrieved with the reserved id `me`) for
    callers with email-read scope; `null` otherwise, or while the account has no
    confirmed email yet.
    """

    name: Optional[str] = None
    """The user's display name"""

    profile_picture: ProfilePicture
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when
    the user set no picture.
    """

    social_accounts: List[SocialAccount]

    staff: Optional[Staff] = None
    """Whop staff access flags.

    Populated only on the self view (retrieved with the reserved id `me`) for
    callers with staff-read scope; `null` there for every user who is not Whop
    staff, and always `null` elsewhere.
    """

    username: str
    """The user's unique username"""

    verification: object
    """
    Identity verification status for the user's `individual` (KYC) and `business`
    (KYB) profiles. Each is `null` until created, otherwise a `status` of
    `not_started`, `pending`, `approved`, or `rejected`.
    """

    whop_partner_enabled_at: Optional[str] = None
    """When the user became an enrolled Whop Partner, as an ISO 8601 timestamp.

    `null` if never enrolled.
    """
