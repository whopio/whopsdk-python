# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .user_balance import UserBalance

__all__ = ["User", "BalanceHistory", "BalanceHistoryData"]


class BalanceHistoryData(BaseModel):
    """Cumulative balance points over the requested window, oldest first."""

    t: int
    """Point timestamp, in Unix seconds."""

    v: float
    """Cumulative wallet balance at this point, in USD."""


class BalanceHistory(BaseModel):
    """
    The user's cumulative wallet balance over time (USD `{ t, v }` points plus last/min/max), for the balance chart. Opt-in and heavier: computed only on `GET /users/me` self-view when `include_balance_history=true` and the caller has balance-read scope; `null` otherwise. A migrated account that never transacted returns an empty series.
    """

    data: List[BalanceHistoryData]

    last: float
    """Value of the most recent point, in USD."""

    max: float
    """Maximum value across the window, in USD."""

    min: float
    """Minimum value across the window, in USD."""


class User(BaseModel):
    id: str
    """User ID, prefixed `user_`."""

    balance: Optional[UserBalance] = None
    """
    The user's balance: personal cash + crypto + in-flight treasury deposits, plus
    per-company balances for companies they own. Computed only on `GET /users/me`
    self-view for callers with balance-read scope; `null` otherwise.
    """

    balance_history: Optional[BalanceHistory] = None
    """
    The user's cumulative wallet balance over time (USD `{ t, v }` points plus
    last/min/max), for the balance chart. Opt-in and heavier: computed only on
    `GET /users/me` self-view when `include_balance_history=true` and the caller has
    balance-read scope; `null` otherwise. A migrated account that never transacted
    returns an empty series.
    """

    bio: Optional[str] = None
    """The user's biography"""

    created_at: str
    """When the user was created, as an ISO 8601 timestamp"""

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
