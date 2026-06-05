# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["LedgerLine", "Currency"]


class Currency(BaseModel):
    """Currency information including code and precision."""

    code: Optional[str] = None
    """The currency code (e.g. 'usd', 'eur')."""

    precision: str
    """The precision factor for this currency (e.g.

    100000000 for USD, 1 for zero-decimal currencies).
    """


class LedgerLine(BaseModel):
    """A ledger line represents a single debit or credit entry on a ledger account."""

    id: str
    """The unique identifier of the ledger line."""

    account_identifier: Optional[str] = None
    """A human-readable identifier derived from the account path (e.g.

    a release date or 'available').
    """

    amount: str
    """The amount of the ledger line in the currency's smallest precision units."""

    currency: Currency
    """Currency information including code and precision."""

    line_category: Optional[str] = None
    """The semantic transaction category of the line (e.g.

    'withdrawal', 'payment_refund'). Matches the line_category filter.
    """

    posted_at: Optional[datetime] = None
    """The timestamp when the ledger line was posted."""

    source_id: Optional[str] = None
    """The tag of the resource this line originated from (e.g.

    a payment, withdrawal, or transfer), if available.
    """
