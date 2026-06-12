# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["User", "Balance", "BalanceToken"]


class BalanceToken(BaseModel):
    """The account's per-token holdings"""

    balance: str
    """The token amount in native units, as a decimal string"""

    icon_url: Optional[str] = None
    """The URL of the token icon, when available"""

    name: str
    """The token's display name"""

    price_usd: Optional[float] = None
    """The USD price per token, or null when no exchange rate is available"""

    symbol: str
    """The token's display symbol, e.g. USDT or cbBTC"""

    token_address: Optional[str] = None
    """The token contract address, when the holding maps to a single contract"""

    value_usd: Optional[str] = None
    """The USD value of the holding, or null when no exchange rate is available"""


class Balance(BaseModel):
    """The user's balance by token.

    Only computed on the self-view (GET /users/me) for callers with the company:balance:read scope; null otherwise and when the balance source is unavailable
    """

    tokens: List[BalanceToken]

    total_usd: str
    """The total USD value across all tokens with a known exchange rate"""


class User(BaseModel):
    id: str
    """The ID of the user, which will look like user\\__******\\********"""

    balance: Optional[Balance] = None
    """The user's balance by token.

    Only computed on the self-view (GET /users/me) for callers with the
    company:balance:read scope; null otherwise and when the balance source is
    unavailable
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
