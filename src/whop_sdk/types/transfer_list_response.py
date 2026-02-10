# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.currency import Currency

__all__ = ["TransferListResponse"]


class TransferListResponse(BaseModel):
    """A transfer of credit between two ledger accounts."""

    id: str
    """The unique identifier for the credit transaction transfer."""

    amount: float
    """The transfer amount in the currency specified by the currency field.

    For example, 10.43 represents $10.43 USD.
    """

    created_at: datetime
    """The datetime the credit transaction transfer was created."""

    currency: Currency
    """The currency in which this transfer amount is denominated."""

    destination_ledger_account_id: str
    """The unique identifier of the ledger account receiving the funds."""

    fee_amount: Optional[float] = None
    """The flat fee amount deducted from this transfer, in the transfer's currency.

    Null if no flat fee was applied.
    """

    metadata: Optional[Dict[str, object]] = None
    """Custom key-value pairs attached to this transfer.

    Maximum 50 keys, 500 characters per key, 5000 characters per value.
    """

    notes: Optional[str] = None
    """A free-text note attached to this transfer by the sender.

    Null if no note was provided.
    """

    origin_ledger_account_id: str
    """The unique identifier of the ledger account that sent the funds."""
