# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .refund_status import RefundStatus
from .shared.currency import Currency
from .payment_provider import PaymentProvider
from .refund_reference_type import RefundReferenceType
from .refund_reference_status import RefundReferenceStatus

__all__ = ["RefundListResponse", "Payment"]


class Payment(BaseModel):
    """The payment associated with the refund."""

    id: str
    """The payment ID"""


class RefundListResponse(BaseModel):
    """An object representing a refund made on a payment."""

    id: str
    """The ID of the refund."""

    amount: float
    """The amount of the refund."""

    created_at: datetime
    """The time the refund was created."""

    currency: Currency
    """The currency of the refund."""

    payment: Optional[Payment] = None
    """The payment associated with the refund."""

    provider: PaymentProvider
    """The provider of the refund."""

    provider_created_at: Optional[datetime] = None
    """The time the refund was created by the provider."""

    reference_status: Optional[RefundReferenceStatus] = None
    """The status of the refund reference."""

    reference_type: Optional[RefundReferenceType] = None
    """The type of refund reference that was made available by the payment provider."""

    reference_value: Optional[str] = None
    """The value of the reference."""

    status: RefundStatus
    """The status of the refund."""
