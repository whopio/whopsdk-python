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
    """The ID of the member"""

    phone: Optional[str] = None
    """The phone number for the member, if available."""


class DataPaymentMembership(BaseModel):
    """The membership attached to this payment."""

    id: str
    """The internal ID of the membership."""

    status: MembershipStatus
    """The state of the membership."""


class DataPaymentUser(BaseModel):
    """The user that made this payment."""

    id: str
    """The internal ID of the user."""

    email: Optional[str] = None
    """The email of the user"""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class DataPayment(BaseModel):
    """The payment associated with the refund."""

    id: str
    """The payment ID"""

    billing_reason: Optional[BillingReasons] = None
    """The reason why a specific payment was billed"""

    card_brand: Optional[CardBrands] = None
    """Possible card brands that a payment token can have"""

    card_last4: Optional[str] = None
    """The last 4 digits of the card used to make the payment."""

    created_at: datetime
    """The datetime the payment was created"""

    currency: Optional[Currency] = None
    """The available currencies on the platform"""

    dispute_alerted_at: Optional[datetime] = None
    """When an alert came in that this transaction will be disputed"""

    member: Optional[DataPaymentMember] = None
    """The member attached to this payment."""

    membership: Optional[DataPaymentMembership] = None
    """The membership attached to this payment."""

    paid_at: Optional[datetime] = None
    """The datetime the payment was paid"""

    payment_method_type: Optional[PaymentMethodTypes] = None
    """The different types of payment methods that can be used."""

    subtotal: Optional[float] = None
    """The subtotal to show to the creator (excluding buyer fees)."""

    total: Optional[float] = None
    """The total to show to the creator (excluding buyer fees)."""

    usd_total: Optional[float] = None
    """The total in USD to show to the creator (excluding buyer fees)."""

    user: Optional[DataPaymentUser] = None
    """The user that made this payment."""


class Data(BaseModel):
    """An object representing a refund made on a payment."""

    id: str
    """The ID of the refund."""

    amount: float
    """The amount of the refund."""

    created_at: datetime
    """The time the refund was created."""

    currency: Currency
    """The currency of the refund."""

    payment: Optional[DataPayment] = None
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


class RefundCreatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    data: Data
    """An object representing a refund made on a payment."""

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["refund.created"]
    """The webhook event type"""
