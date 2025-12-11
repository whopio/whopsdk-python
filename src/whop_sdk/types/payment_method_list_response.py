# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .card_brands import CardBrands
from .payment_method_types import PaymentMethodTypes

__all__ = [
    "PaymentMethodListResponse",
    "BasePaymentMethod",
    "CardPaymentMethod",
    "CardPaymentMethodCard",
    "UsBankAccountPaymentMethod",
    "UsBankAccountPaymentMethodUsBankAccount",
    "CashappPaymentMethod",
    "CashappPaymentMethodCashapp",
    "IdealPaymentMethod",
    "IdealPaymentMethodIdeal",
    "SepaDebitPaymentMethod",
    "SepaDebitPaymentMethodSepaDebit",
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


class CashappPaymentMethodCashapp(BaseModel):
    """The Cash App details associated with this payment method"""

    buyer_id: Optional[str] = None
    """A unique and immutable identifier assigned by Cash App to every buyer."""

    cashtag: Optional[str] = None
    """A public identifier for buyers using Cash App."""


class CashappPaymentMethod(BaseModel):
    """The Cash App details for the payment method"""

    id: str
    """The ID of the payment method"""

    cashapp: CashappPaymentMethodCashapp
    """The Cash App details associated with this payment method"""

    created_at: datetime
    """When the payment method was created"""

    payment_method_type: PaymentMethodTypes
    """The type of the payment method"""

    typename: Literal["CashappPaymentMethod"]
    """The typename of this object"""


class IdealPaymentMethodIdeal(BaseModel):
    """The iDEAL details associated with this payment method"""

    bank: Optional[str] = None
    """The customer's bank."""

    bic: Optional[str] = None
    """The Bank Identifier Code of the customer's bank."""


class IdealPaymentMethod(BaseModel):
    """The iDEAL details for the payment method"""

    id: str
    """The ID of the payment method"""

    created_at: datetime
    """When the payment method was created"""

    ideal: IdealPaymentMethodIdeal
    """The iDEAL details associated with this payment method"""

    payment_method_type: PaymentMethodTypes
    """The type of the payment method"""

    typename: Literal["IdealPaymentMethod"]
    """The typename of this object"""


class SepaDebitPaymentMethodSepaDebit(BaseModel):
    """The SEPA Direct Debit details associated with this payment method"""

    bank_code: Optional[str] = None
    """Bank code of the bank associated with the account."""

    branch_code: Optional[str] = None
    """Branch code of the bank associated with the account."""

    country: Optional[str] = None
    """Two-letter ISO code representing the country the bank account is located in."""

    last4: Optional[str] = None
    """Last four digits of the IBAN."""


class SepaDebitPaymentMethod(BaseModel):
    """The SEPA Direct Debit details for the payment method"""

    id: str
    """The ID of the payment method"""

    created_at: datetime
    """When the payment method was created"""

    payment_method_type: PaymentMethodTypes
    """The type of the payment method"""

    sepa_debit: SepaDebitPaymentMethodSepaDebit
    """The SEPA Direct Debit details associated with this payment method"""

    typename: Literal["SepaDebitPaymentMethod"]
    """The typename of this object"""


PaymentMethodListResponse: TypeAlias = Annotated[
    Union[
        BasePaymentMethod,
        CardPaymentMethod,
        UsBankAccountPaymentMethod,
        CashappPaymentMethod,
        IdealPaymentMethod,
        SepaDebitPaymentMethod,
    ],
    PropertyInfo(discriminator="typename"),
]
