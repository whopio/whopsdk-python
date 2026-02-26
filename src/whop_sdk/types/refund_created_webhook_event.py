# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .card_brands import CardBrands
from .refund_status import RefundStatus
from .billing_reasons import BillingReasons
from .shared.currency import Currency
from .payment_provider import PaymentProvider
from .payment_method_types import PaymentMethodTypes
from .refund_reference_type import RefundReferenceType
from .refund_reference_status import RefundReferenceStatus
from .shared.membership_status import MembershipStatus

__all__ = [
    "RefundCreatedWebhookEvent",
    "Data",
    "DataPayment",
    "DataPaymentMember",
    "DataPaymentMembership",
    "DataPaymentUser",
]


class DataPaymentMember(BaseModel):
    """The member attached to this payment."""

    id: str
    """The unique identifier for the company member."""

    phone: Optional[str] = None
    """The phone number for the member, if available."""


class DataPaymentMembership(BaseModel):
    """The membership attached to this payment."""

    id: str
    """The unique identifier for the membership."""

    status: MembershipStatus
    """The state of the membership."""


class DataPaymentUser(BaseModel):
    """The user that made this payment."""

    id: str
    """The unique identifier for the user."""

    email: Optional[str] = None
    """The user's email address.

    Requires the member:email:read permission to access. Null if not authorized.
    """

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class DataPayment(BaseModel):
    """The original payment that this refund was issued against.

    Null if the payment is no longer available.
    """

    id: str
    """The unique identifier for the payment."""

    billing_reason: Optional[BillingReasons] = None
    """The reason why a specific payment was billed"""

    card_brand: Optional[CardBrands] = None
    """Possible card brands that a payment token can have"""

    card_last4: Optional[str] = None
    """The last four digits of the card used to make this payment.

    Null if the payment was not made with a card.
    """

    created_at: datetime
    """The datetime the payment was created."""

    currency: Optional[Currency] = None
    """The available currencies on the platform"""

    dispute_alerted_at: Optional[datetime] = None
    """When an alert came in that this transaction will be disputed"""

    member: Optional[DataPaymentMember] = None
    """The member attached to this payment."""

    membership: Optional[DataPaymentMembership] = None
    """The membership attached to this payment."""

    paid_at: Optional[datetime] = None
    """The time at which this payment was successfully collected.

    Null if the payment has not yet succeeded. As a Unix timestamp.
    """

    payment_method_type: Optional[PaymentMethodTypes] = None
    """The different types of payment methods that can be used."""

    subtotal: Optional[float] = None
    """The subtotal to show to the creator (excluding buyer fees)."""

    tax_amount: Optional[float] = None
    """The calculated amount of the sales/VAT tax (if applicable)."""

    tax_behavior: Optional[Literal["exclusive", "inclusive", "unspecified", "unable_to_collect"]] = None
    """
    The type of tax inclusivity applied to the receipt, for determining whether the
    tax is included in the final price, or paid on top.
    """

    tax_refunded_amount: Optional[float] = None
    """The amount of tax that has been refunded (if applicable)."""

    total: Optional[float] = None
    """The total to show to the creator (excluding buyer fees)."""

    usd_total: Optional[float] = None
    """The total in USD to show to the creator (excluding buyer fees)."""

    user: Optional[DataPaymentUser] = None
    """The user that made this payment."""


class Data(BaseModel):
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

    payment: Optional[DataPayment] = None
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


class RefundCreatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    data: Data
    """
    A refund represents a full or partial reversal of a payment, including the
    amount, status, and payment provider.
    """

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["refund.created"]
    """The webhook event type"""

    company_id: Optional[str] = None
    """The company ID that this webhook event is associated with"""
