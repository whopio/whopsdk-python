# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .user_balance import UserBalance

__all__ = [
    "User",
    "BalanceHistory",
    "BalanceHistoryData",
    "EarningsUsd",
    "EarningsUsdOwnedAccounts",
    "EarningsUsdPersonal",
    "EarningsUsdTotal",
]


class BalanceHistoryData(BaseModel):
    """Cumulative balance points over the requested window, oldest first."""

    t: int
    """Point timestamp, in Unix seconds."""

    v: float
    """Cumulative wallet balance at this point, in USD."""


class BalanceHistory(BaseModel):
    """
    The user's cumulative wallet balance over time (USD `{ t, v }` points plus last/min/max), for the balance chart. Opt in with `include_balance_history=true` on `GET /users/me`; populated only for callers with balance-read scope and `null` otherwise. A user with no wallet activity returns an empty series.
    """

    data: List[BalanceHistoryData]

    last: float
    """Value of the most recent point, in USD."""

    max: float
    """Maximum value across the window, in USD."""

    min: float
    """Minimum value across the window, in USD."""


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
    """The user's gross USD income over time.

    Populated only on single-user self reads for callers with balance-read scope; `null` otherwise.
    """

    first_earned_at: Optional[str] = None
    """The first time the user earned gross income, as an ISO 8601 timestamp."""

    owned_accounts: EarningsUsdOwnedAccounts
    """Gross income from accounts the user owns or is owner-authorized on."""

    personal: EarningsUsdPersonal
    """Gross income from the user's personal wallet."""

    total: EarningsUsdTotal
    """
    Gross income from the user's personal wallet plus accounts they own or are
    owner-authorized on.
    """


class User(BaseModel):
    id: str
    """User ID, prefixed `user_`."""

    balance: Optional[UserBalance] = None
    """
    The user's balance: personal cash + crypto + in-flight treasury deposits, plus
    account balances for accounts they own. Computed only on `GET /users/me`
    self-view for callers with balance-read scope; `null` otherwise.
    """

    balance_history: Optional[BalanceHistory] = None
    """
    The user's cumulative wallet balance over time (USD `{ t, v }` points plus
    last/min/max), for the balance chart. Opt in with `include_balance_history=true`
    on `GET /users/me`; populated only for callers with balance-read scope and
    `null` otherwise. A user with no wallet activity returns an empty series.
    """

    bio: Optional[str] = None
    """The user's biography"""

    created_at: str
    """When the user was created, as an ISO 8601 timestamp"""

    earnings_usd: Optional[EarningsUsd] = None
    """The user's gross USD income over time.

    Populated only on single-user self reads for callers with balance-read scope;
    `null` otherwise.
    """

    name: Optional[str] = None
    """The user's display name"""

    profile_picture: Optional[object] = None
    """The user's profile picture, an object with a url"""

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
