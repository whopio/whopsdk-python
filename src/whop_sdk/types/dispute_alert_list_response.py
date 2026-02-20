# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.currency import Currency
from .dispute_alert_type import DisputeAlertType

__all__ = ["DisputeAlertListResponse", "Dispute", "Payment"]


class Dispute(BaseModel):
    """The dispute associated with the dispute alert."""

    id: str
    """The unique identifier for the dispute."""


class Payment(BaseModel):
    """The payment associated with the dispute alert."""

    id: str
    """The unique identifier for the payment."""


class DisputeAlertListResponse(BaseModel):
    """
    A dispute alert represents an early warning notification from a payment processor about a potential dispute or chargeback.
    """

    id: str
    """The unique identifier of the dispute alert."""

    alert_type: DisputeAlertType
    """The type of the dispute alert."""

    amount: float
    """The alerted amount in the specified currency."""

    charge_for_alert: bool
    """Whether this alert incurs a charge."""

    created_at: datetime
    """The time the dispute alert was created."""

    currency: Currency
    """The three-letter ISO currency code for the alerted amount."""

    dispute: Optional[Dispute] = None
    """The dispute associated with the dispute alert."""

    payment: Optional[Payment] = None
    """The payment associated with the dispute alert."""

    transaction_date: Optional[datetime] = None
    """The date of the original transaction."""
