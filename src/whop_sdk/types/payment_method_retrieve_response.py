# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .card_brands import CardBrands
from .payment_method_types import PaymentMethodTypes

__all__ = [
    "PaymentMethodRetrieveResponse",
    "BasePaymentMethod",
    "CardPaymentMethod",
    "CardPaymentMethodCard",
    "UsBankAccountPaymentMethod",
    "UsBankAccountPaymentMethodUsBankAccount",
]


class BasePaymentMethod(BaseModel):
    """A payment method with no additional properties"""

    id: str
    """The ID of the payment method"""

    created_at: datetime
    """When the payment method was created"""

    payment_method_type: PaymentMethodTypes
    """The type of the payment method"""

    typename: Literal["BasePaymentMethod"]
    """The typename of this object"""


class CardPaymentMethodCard(BaseModel):
    """The card details associated with this payment method"""

    brand: Optional[CardBrands] = None
    """Possible card brands that a payment token can have"""

    exp_month: Optional[int] = None
    """Card expiration month, like 03 for March."""

    exp_year: Optional[int] = None
    """Card expiration year, like 27 for 2027."""

    last4: Optional[str] = None
    """Last four digits of the card."""


class CardPaymentMethod(BaseModel):
    """The card for the payment method"""

    id: str
    """The ID of the payment method"""

    card: CardPaymentMethodCard
    """The card details associated with this payment method"""

    created_at: datetime
    """When the payment method was created"""

    payment_method_type: PaymentMethodTypes
    """The type of the payment method"""

    typename: Literal["CardPaymentMethod"]
    """The typename of this object"""


class UsBankAccountPaymentMethodUsBankAccount(BaseModel):
    """The bank details associated with this payment method"""

    account_type: str
    """The type of account"""

    bank_name: str
    """The name of the bank"""

    last4: str
    """The last 4 digits of the account number"""


class UsBankAccountPaymentMethod(BaseModel):
    """The bank account for the payment method"""

    id: str
    """The ID of the payment method"""

    created_at: datetime
    """When the payment method was created"""

    payment_method_type: PaymentMethodTypes
    """The type of the payment method"""

    typename: Literal["UsBankAccountPaymentMethod"]
    """The typename of this object"""

    us_bank_account: UsBankAccountPaymentMethodUsBankAccount
    """The bank details associated with this payment method"""


PaymentMethodRetrieveResponse: TypeAlias = Annotated[
    Union[BasePaymentMethod, CardPaymentMethod, UsBankAccountPaymentMethod], PropertyInfo(discriminator="typename")
]
