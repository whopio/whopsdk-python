# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .card_brands import CardBrands
from .payment_method_types import PaymentMethodTypes

__all__ = ["PaymentTokenRetrieveResponse", "Card"]


class Card(BaseModel):
    brand: Optional[CardBrands] = None
    """Possible card brands that a payment token can have"""

    exp_month: Optional[int] = None
    """Card expiration month, like 03 for March."""

    exp_year: Optional[int] = None
    """Card expiration year, like 27 for 2027."""

    last4: Optional[str] = None
    """Last four digits of the card."""


class PaymentTokenRetrieveResponse(BaseModel):
    id: str
    """The ID of the payment token"""

    card: Optional[Card] = None
    """
    The card data associated with the payment token, if its a debit or credit card
    token.
    """

    created_at: datetime
    """The date and time the payment token was created"""

    payment_method_type: PaymentMethodTypes
    """The payment method type of the payment token"""
