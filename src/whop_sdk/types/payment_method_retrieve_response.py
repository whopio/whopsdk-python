# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .card_brands import CardBrands
from .payment_method_types import PaymentMethodTypes

__all__ = ["PaymentMethodRetrieveResponse", "Bank", "Card"]


class Bank(BaseModel):
    """
    The bank account data associated with the payment method, if it's a bank account.
    """

    account_type: str
    """The type of account"""

    bank_name: str
    """The name of the bank"""

    last4: str
    """The last 4 digits of the account number"""


class Card(BaseModel):
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


class PaymentMethodRetrieveResponse(BaseModel):
    """A stored payment method used to process payments.

    This could be a credit/debit card, bank account, PayPal wallet, etc.
    """

    id: str
    """The ID of the payment method"""

    bank: Optional[Bank] = None
    """
    The bank account data associated with the payment method, if it's a bank
    account.
    """

    card: Optional[Card] = None
    """
    The card data associated with the payment method, if its a debit or credit card.
    """

    created_at: datetime
    """The date and time the payment method was created"""

    payment_method_type: PaymentMethodTypes
    """The payment method type of the payment method"""
