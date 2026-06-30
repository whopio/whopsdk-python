# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["User", "Balance"]


class Balance(BaseModel):
    """User holdings (crypto and fiat), each with USD value.

    Empty when `total_usd` is `null`.
    """

    balance: str
    """Total amount held in native units, as a decimal string."""

    breakdown: object
    """
    Balance split into available, pending, and reserve amounts, as native-unit
    decimal strings. On-chain crypto is entirely available; good_funds and fiat cash
    can have pending or reserve portions.
    """

    icon_url: Optional[str] = None
    """Holding icon URL."""

    name: str
    """The holding's display name"""

    price_usd: Optional[float] = None
    """USD price per unit, or `null` when no exchange rate is available."""

    symbol: str
    """Holding display symbol, such as `USDT`, `cbBTC`, or `EUR`."""

    value_usd: Optional[str] = None
    """Holding USD value, or `null` when no exchange rate is available."""


class User(BaseModel):
    id: str
    """User ID, prefixed `user_`."""

    balances: List[Balance]

    bio: Optional[str] = None
    """The user's biography"""

    created_at: str
    """When the user was created, as an ISO 8601 timestamp"""

    name: Optional[str] = None
    """The user's display name"""

    profile_picture: Optional[object] = None
    """The user's profile picture, an object with a url"""

    total_usd: Optional[str] = None
    """Total USD value across the user's balances with known exchange rates.

    Computed only on `GET /users/me` self-view for callers with balance-read scope;
    `null` otherwise.
    """

    username: str
    """The user's unique username"""

    verification: object
    """
    Identity verification status for the user's `individual` (KYC) and `business`
    (KYB) profiles. Each is `null` until created, otherwise a `status` of
    `not_started`, `pending`, `approved`, or `rejected`.
    """
