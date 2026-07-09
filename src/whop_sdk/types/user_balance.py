# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["UserBalance", "Business", "Cash", "Crypto"]


class Business(BaseModel):
    """Per-company balances for companies the user owns, highest balance first.

    Excludes companies with no balance.
    """

    id: str
    """The company ID, which looks like biz\\__******\\********."""

    balance_usd: str
    """The company's total balance in USD."""

    logo_url: Optional[str] = None
    """The company's logo URL."""

    name: Optional[str] = None
    """The company's display name."""


class Cash(BaseModel):
    """Per-currency fiat cash balances."""

    balance: float
    """Available balance in the native currency."""

    balance_usd: float
    """Available balance converted to USD."""

    currency: str
    """Lowercase ISO currency code, such as `usd` or `eur`."""

    pending_balance_usd: float
    """Pending balance converted to USD."""

    reserve_balance_usd: float
    """Reserved balance converted to USD."""

    total_withdrawable_balance: float
    """Withdrawable amount in the native currency."""


class Crypto(BaseModel):
    """Per-token crypto holdings in the ledger's own wallet."""

    balance: str
    """Amount held in native token units, as a decimal string."""

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


class UserBalance(BaseModel):
    businesses: List[Business]

    businesses_total_usd: str
    """Combined USD balance across every company the user owns."""

    cash: List[Cash]

    cash_usd: str
    """Fiat cash in USD, including pending and reserve."""

    crypto: List[Crypto]

    crypto_usd: str
    """Crypto holdings in USD."""

    pending_usd: str
    """Pending funds in USD: fiat pending + in-flight treasury deposits."""

    total_usd: str
    """
    The user's personal balance in USD: cash (available + pending + reserve) +
    crypto + in-flight treasury deposits. Excludes companies (see
    businesses_total_usd).
    """

    treasury_pending_usd: str
    """Balance-to-wallet USDT0 withdrawals still in flight, in USD."""
