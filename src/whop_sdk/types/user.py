# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["User", "Balance"]


class Balance(BaseModel):
    """The user's holdings (crypto and fiat), each with its USD value.

    Empty when total_usd is null (not computed)
    """

    balance: str
    """The total amount held in native units, as a decimal string"""

    breakdown: object
    """
    The holding split into available, pending, and reserve amounts (native-unit
    decimal strings). On-chain crypto is entirely available; good_funds and fiat
    cash can have pending/reserve portions
    """

    icon_url: Optional[str] = None
    """The URL of the holding's icon, when available"""

    name: str
    """The holding's display name"""

    price_usd: Optional[float] = None
    """The USD price per unit, or null when no exchange rate is available"""

    symbol: str
    """The holding's display symbol, e.g. USDT, cbBTC, or EUR"""

    value_usd: Optional[str] = None
    """The total USD value of the holding, or null when no exchange rate is available"""


class User(BaseModel):
    id: str
    """The ID of the user, which will look like user\\__******\\********"""

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
    """Total USD value across all balances with a known exchange rate.

    Only computed on the self-view (GET /users/me) for callers with the balance-read
    scope; null (with an empty balances array) otherwise and when the balance source
    is unavailable
    """

    username: str
    """The user's unique username"""
