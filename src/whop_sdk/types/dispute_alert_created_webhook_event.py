# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .card_brands import CardBrands
from .billing_reasons import BillingReasons
from .shared.currency import Currency
from .dispute_statuses import DisputeStatuses
from .payment_method_types import PaymentMethodTypes
from .shared.membership_status import MembershipStatus

__all__ = [
    "DisputeAlertCreatedWebhookEvent",
    "Data",
    "DataDispute",
    "DataPayment",
    "DataPaymentMember",
    "DataPaymentMembership",
    "DataPaymentUser",
]


class DataDispute(BaseModel):
    """The dispute associated with the dispute alert."""

    id: str
    """The unique identifier for the dispute."""

    amount: float
    """The disputed amount in the specified currency, formatted as a decimal."""

    created_at: Optional[datetime] = None
    """The datetime the dispute was created."""

    currency: Currency
    """The three-letter ISO currency code for the disputed amount."""

    reason: Optional[str] = None
    """A human-readable reason for the dispute."""

    status: DisputeStatuses
    """
    The current status of the dispute lifecycle, such as needs_response,
    under_review, won, or lost.
    """


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
    """The payment associated with the dispute alert."""

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

    total: Optional[float] = None
    """The total to show to the creator (excluding buyer fees)."""

    usd_total: Optional[float] = None
    """The total in USD to show to the creator (excluding buyer fees)."""

    user: Optional[DataPaymentUser] = None
    """The user that made this payment."""


class Data(BaseModel):
    """
    A dispute alert represents an early warning notification from a payment processor about a potential dispute or chargeback.
    """

    id: str
    """The unique identifier of the dispute alert."""

    alert_type: Literal["dispute", "dispute_rdr", "fraud"]
    """The type of the dispute alert."""

    amount: float
    """The alerted amount in the specified currency."""

    charge_for_alert: bool
    """Whether this alert incurs a charge."""

    created_at: datetime
    """The time the dispute alert was created."""

    currency: Currency
    """The three-letter ISO currency code for the alerted amount."""

    dispute: Optional[DataDispute] = None
    """The dispute associated with the dispute alert."""

    payment: Optional[DataPayment] = None
    """The payment associated with the dispute alert."""

    transaction_date: Optional[datetime] = None
    """The date of the original transaction."""


class DisputeAlertCreatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    data: Data
    """
    A dispute alert represents an early warning notification from a payment
    processor about a potential dispute or chargeback.
    """

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["dispute_alert.created"]
    """The webhook event type"""

    company_id: Optional[str] = None
    """The company ID that this webhook event is associated with"""
