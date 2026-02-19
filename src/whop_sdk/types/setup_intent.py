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
    """The checkout session configuration associated with this setup intent.

    Null if no checkout session was used.
    """

    id: str
    """The unique identifier for the checkout session."""


class Company(BaseModel):
    """The company that initiated this setup intent.

    Null if the company has been deleted.
    """

    id: str
    """The unique identifier for the company."""


class MemberUser(BaseModel):
    """The user for this member, if any."""

    id: str
    """The unique identifier for the company member user."""

    email: Optional[str] = None
    """The digital mailing address of the user."""

    name: Optional[str] = None
    """The user's full name."""

    username: str
    """The whop username."""


class Member(BaseModel):
    """The company member associated with this setup intent.

    Null if the user is not a member.
    """

    id: str
    """The unique identifier for the company member."""

    user: Optional[MemberUser] = None
    """The user for this member, if any."""


class PaymentMethodCard(BaseModel):
    """
    The card data associated with the payment method, if its a debit or credit card.
    """

    brand: Optional[CardBrands] = None
    """Possible card brands that a payment token can have"""

    exp_month: Optional[int] = None
    """The two-digit expiration month of the card (1-12). Null if not available."""

    exp_year: Optional[int] = None
    """The two-digit expiration year of the card (e.g., 27 for 2027).

    Null if not available.
    """

    last4: Optional[str] = None
    """The last four digits of the card number. Null if not available."""


class PaymentMethod(BaseModel):
    """The saved payment method created by this setup intent.

    Null if the setup has not completed successfully.
    """

    id: str
    """The unique identifier for the payment token."""

    card: Optional[PaymentMethodCard] = None
    """
    The card data associated with the payment method, if its a debit or credit card.
    """

    created_at: datetime
    """The datetime the payment token was created."""

    payment_method_type: PaymentMethodTypes
    """The payment method type of the payment method"""


class SetupIntent(BaseModel):
    """
    A setup intent allows a user to save a payment method for future use without making an immediate purchase.
    """

    id: str
    """The unique identifier for the setup intent."""

    checkout_configuration: Optional[CheckoutConfiguration] = None
    """The checkout session configuration associated with this setup intent.

    Null if no checkout session was used.
    """

    company: Optional[Company] = None
    """The company that initiated this setup intent.

    Null if the company has been deleted.
    """

    created_at: datetime
    """The datetime the setup intent was created."""

    error_message: Optional[str] = None
    """A human-readable error message explaining why the setup intent failed.

    Null if no error occurred.
    """

    member: Optional[Member] = None
    """The company member associated with this setup intent.

    Null if the user is not a member.
    """

    metadata: Optional[Dict[str, object]] = None
    """Custom key-value pairs attached to this setup intent.

    Null if no metadata was provided.
    """

    payment_method: Optional[PaymentMethod] = None
    """The saved payment method created by this setup intent.

    Null if the setup has not completed successfully.
    """

    status: SetupIntentStatus
    """The current status of the setup intent."""
