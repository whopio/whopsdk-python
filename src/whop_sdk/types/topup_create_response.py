# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.currency import Currency
from .shared.receipt_status import ReceiptStatus

__all__ = ["TopupCreateResponse"]


class TopupCreateResponse(BaseModel):
    """A payment represents a completed or attempted charge for a membership.

    Payments track the amount, status, currency, and payment method used.
    """

    id: str
    """The unique identifier for the payment."""

    created_at: datetime
    """The datetime the payment was created."""

    currency: Optional[Currency] = None
    """The available currencies on the platform"""

    failure_message: Optional[str] = None
    """If the payment failed, the reason for the failure."""

    paid_at: Optional[datetime] = None
    """The datetime the payment was paid"""

    status: Optional[ReceiptStatus] = None
    """The status of a receipt"""

    total: Optional[float] = None
    """The total to show to the creator (excluding buyer fees)."""
