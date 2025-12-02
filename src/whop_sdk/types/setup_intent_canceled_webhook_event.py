# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .card_brands import CardBrands
from .payment_method_types import PaymentMethodTypes

__all__ = [
    "SetupIntentCanceledWebhookEvent",
    "Data",
    "DataCheckoutConfiguration",
    "DataCompany",
    "DataMember",
    "DataMemberUser",
    "DataPaymentToken",
    "DataPaymentTokenCard",
]


class DataCheckoutConfiguration(BaseModel):
    id: str
    """The ID of the checkout configuration"""


class DataCompany(BaseModel):
    id: str
    """The ID (tag) of the company."""


class DataMemberUser(BaseModel):
    id: str
    """The internal ID of the user account."""

    email: Optional[str] = None
    """The digital mailing address of the user."""

    name: Optional[str] = None
    """The user's full name."""

    username: str
    """The whop username."""


class DataMember(BaseModel):
    id: str
    """The ID of the member"""

    user: Optional[DataMemberUser] = None
    """The user for this member, if any."""


class DataPaymentTokenCard(BaseModel):
    brand: Optional[CardBrands] = None
    """Possible card brands that a payment token can have"""

    exp_month: Optional[int] = None
    """Card expiration month, like 03 for March."""

    exp_year: Optional[int] = None
    """Card expiration year, like 27 for 2027."""

    last4: Optional[str] = None
    """Last four digits of the card."""


class DataPaymentToken(BaseModel):
    id: str
    """The ID of the payment token"""

    card: Optional[DataPaymentTokenCard] = None
    """
    The card data associated with the payment token, if its a debit or credit card
    token.
    """

    created_at: datetime
    """The date and time the payment token was created"""

    payment_method_type: PaymentMethodTypes
    """The payment method type of the payment token"""


class Data(BaseModel):
    id: str
    """The setup intent ID"""

    checkout_configuration: Optional[DataCheckoutConfiguration] = None
    """The checkout configuration associated with the setup intent"""

    company: Optional[DataCompany] = None
    """The company of the setup intent"""

    created_at: datetime
    """The datetime the payment was created"""

    error_message: Optional[str] = None
    """The error message, if any."""

    member: Optional[DataMember] = None
    """The member connected to the setup intent"""

    metadata: Optional[Dict[str, object]] = None
    """The metadata associated with the setup intent"""

    payment_token: Optional[DataPaymentToken] = None
    """The payment token created during the setup, if available."""

    status: Literal["processing", "succeeded", "canceled", "requires_action"]
    """The status of the setup intent"""


class SetupIntentCanceledWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    data: Data
    """
    An object representing a setup intent, which is a flow for allowing a customer
    to add a payment method to their account without making a purchase.
    """

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["setup_intent.canceled"]
    """The webhook event type"""
