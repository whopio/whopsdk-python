# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.currency import Currency

__all__ = ["TransferListResponse"]


class TransferListResponse(BaseModel):
    """Credit Transaction Transfer"""

    id: str
    """The unique identifier of the credit transaction transfer"""

    amount: float
    """The amount of the credit transaction transfer"""

    created_at: datetime
    """The timestamp when the credit transaction transfer was created"""

    currency: Currency
    """The currency of the credit transaction transfer"""

    destination_ledger_account_id: str
    """The ID of the destination ledger account"""

    fee_amount: Optional[float] = None
    """The decimal fee of the credit transaction transfer"""

    metadata: Optional[Dict[str, object]] = None
    """A hash of metadata attached to the transfer"""

    notes: Optional[str] = None
    """The notes of the credit transaction transfer"""

    origin_ledger_account_id: str
    """The ID of the origin ledger account"""
