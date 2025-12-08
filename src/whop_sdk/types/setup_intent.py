# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .card_brands import CardBrands
from .setup_intent_status import SetupIntentStatus
from .payment_method_types import PaymentMethodTypes

__all__ = [
    "SetupIntent",
    "CheckoutConfiguration",
    "Company",
    "Member",
    "MemberUser",
    "PaymentMethod",
    "PaymentMethodCard",
]


class CheckoutConfiguration(BaseModel):
    """The checkout configuration associated with the setup intent"""

    id: str
    """The ID of the checkout configuration"""


class Company(BaseModel):
    """The company of the setup intent"""

    id: str
    """The ID (tag) of the company."""


class MemberUser(BaseModel):
    """The user for this member, if any."""

    id: str
    """The internal ID of the user account."""

    email: Optional[str] = None
    """The digital mailing address of the user."""

    name: Optional[str] = None
    """The user's full name."""

    username: str
    """The whop username."""


class Member(BaseModel):
    """The member connected to the setup intent"""

    id: str
    """The ID of the member"""

    user: Optional[MemberUser] = None
    """The user for this member, if any."""


class PaymentMethodCard(BaseModel):
    """
    The card data associated with the payment method, if its a debit or credit card.
    """

    brand: Optional[CardBrands] = None
    """Possible card brands that a payment token can have"""

    exp_month: Optional[int] = None
    """Card expiration month, like 03 for March."""

    exp_year: Optional[int] = None
    """Card expiration year, like 27 for 2027."""

    last4: Optional[str] = None
    """Last four digits of the card."""


class PaymentMethod(BaseModel):
    """The payment method created during the setup, if available."""

    id: str
    """The ID of the payment method"""

    card: Optional[PaymentMethodCard] = None
    """
    The card data associated with the payment method, if its a debit or credit card.
    """

    created_at: datetime
    """The date and time the payment method was created"""

    payment_method_type: PaymentMethodTypes
    """The payment method type of the payment method"""


class SetupIntent(BaseModel):
    """
    An object representing a setup intent, which is a flow for allowing a customer to add a payment method to their account without making a purchase.
    """

    id: str
    """The setup intent ID"""

    checkout_configuration: Optional[CheckoutConfiguration] = None
    """The checkout configuration associated with the setup intent"""

    company: Optional[Company] = None
    """The company of the setup intent"""

    created_at: datetime
    """The datetime the payment was created"""

    error_message: Optional[str] = None
    """The error message, if any."""

    member: Optional[Member] = None
    """The member connected to the setup intent"""

    metadata: Optional[Dict[str, object]] = None
    """The metadata associated with the setup intent"""

    payment_method: Optional[PaymentMethod] = None
    """The payment method created during the setup, if available."""

    status: SetupIntentStatus
    """The status of the setup intent"""
