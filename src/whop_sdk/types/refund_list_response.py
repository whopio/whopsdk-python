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
    """The original payment that this refund was issued against.

    Null if the payment is no longer available.
    """

    id: str
    """The unique identifier for the payment."""


class RefundListResponse(BaseModel):
    """
    A refund represents a full or partial reversal of a payment, including the amount, status, and payment provider.
    """

    id: str
    """The unique identifier for the refund."""

    amount: float
    """
    The refunded amount as a decimal in the specified currency, such as 10.43 for
    $10.43 USD.
    """

    created_at: datetime
    """The datetime the refund was created."""

    currency: Currency
    """The three-letter ISO currency code for the refunded amount."""

    payment: Optional[Payment] = None
    """The original payment that this refund was issued against.

    Null if the payment is no longer available.
    """

    provider: PaymentProvider
    """The payment provider that processed the refund."""

    provider_created_at: Optional[datetime] = None
    """The timestamp when the refund was created in the payment provider's system.

    Null if not available from the provider.
    """

    reference_status: Optional[RefundReferenceStatus] = None
    """The status of the refund reference."""

    reference_type: Optional[RefundReferenceType] = None
    """The type of refund reference that was made available by the payment provider."""

    reference_value: Optional[str] = None
    """
    The tracking reference value from the payment processor, used to trace the
    refund through banking networks. Null if no reference was provided.
    """

    status: RefundStatus
    """
    The current processing status of the refund, such as pending, succeeded, or
    failed.
    """
