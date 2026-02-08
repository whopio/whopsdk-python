# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.currency import Currency

__all__ = ["TransferListResponse"]


class TransferListResponse(BaseModel):
    """Credit Transaction Transfer"""

    id: str
    """The unique identifier for the credit transaction transfer."""

    amount: float
    """The amount of the transfer.

    Provided as a number in the specified currency. Eg: 10.43 for $10.43 USD.
    """

    created_at: datetime
    """The datetime the credit transaction transfer was created."""

    currency: Currency
    """The currency of the credit transaction transfer"""

    destination_ledger_account_id: str
    """The ID of the destination ledger account"""

    fee_amount: Optional[float] = None
    """The decimal fee of the credit transaction transfer"""

    metadata: Optional[Dict[str, object]] = None
    """Custom key-value pairs attached to the transfer.

    Max 50 keys, 500 chars per key, 5000 chars per value.
    """

    notes: Optional[str] = None
    """The notes of the credit transaction transfer"""

    origin_ledger_account_id: str
    """The ID of the origin ledger account"""
