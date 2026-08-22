# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["UserBalance", "Business", "Cash", "Crypto", "CryptoBreakdown", "CryptoBreakdownPendingSettlement"]


class Business(BaseModel):
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


class Cash(BaseModel):
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


class CryptoBreakdownPendingSettlement(BaseModel):
    """When the pending amount is expected to settle, one entry per day, earliest first.

    Money with no scheduled settlement day, such as a transfer in flight, is left out — so these can sum to less than `pending`, never more.
    """

    amount: str
    """Amount expected that day, in native units, as a decimal string."""

    date: str
    """The day this money is expected to finish settling, as an ISO 8601 date."""


class CryptoBreakdown(BaseModel):
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

    pending_settlements: List[CryptoBreakdownPendingSettlement]

    reserve: str
    """Amount held back, in native units, as a decimal string.

    Retrieve the account's reserves for why it is held and when it unlocks.
    """


class Crypto(BaseModel):
    """Per-token crypto holdings in the ledger's own wallet."""

    balance: str
    """Amount held in native token units, as a decimal string."""

    breakdown: CryptoBreakdown
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


class UserBalance(BaseModel):
    businesses: List[Business]

    businesses_total_usd: str
    """Combined USD balance across every account the user owns."""

    cash: List[Cash]

    cash_usd: str
    """Fiat cash in USD, including pending, in-transit, and reserve."""

    crypto: List[Crypto]

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
    """Balance-to-wallet USDT0 withdrawals still in flight, in USD."""
