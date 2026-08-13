# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .card_brands import CardBrands
from .shared.currency import Currency
from .payment_method_types import PaymentMethodTypes

__all__ = [
    "PaymentMethodRetrieveResponse",
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
    "PlatformBalancePaymentMethod",
    "PlatformBalancePaymentMethodPlatformBalance",
    "PlatformBalancePaymentMethodPlatformBalanceBalance",
]


class BasePaymentMethod(BaseModel):
    """A saved payment method with no type-specific details available."""

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    created_at: datetime
    """The time of the event in ISO 8601 UTC format with millisecond precision"""

    payment_method_type: PaymentMethodTypes
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    typename: Literal["BasePaymentMethod"]
    """The typename of this object"""


class CardPaymentMethodCard(BaseModel):
    """
    The card-specific details for this payment method, including brand, last four digits, and expiration.
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

    three_ds_verified: bool
    """
    Whether this card was verified with 3D Secure, either when it was saved or on a
    payment that used it.
    """


class CardPaymentMethod(BaseModel):
    """
    A saved card payment method, including brand, last four digits, and expiration details.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    card: CardPaymentMethodCard
    """
    The card-specific details for this payment method, including brand, last four
    digits, and expiration.
    """

    created_at: datetime
    """The time of the event in ISO 8601 UTC format with millisecond precision"""

    has_payer_document: bool
    """
    Whether this card has the payer identity document required by its payment
    provider.
    """

    payment_method_type: PaymentMethodTypes
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    typename: Literal["CardPaymentMethod"]
    """The typename of this object"""


class UsBankAccountPaymentMethodUsBankAccount(BaseModel):
    """
    The bank account-specific details for this payment method, including bank name and last four digits.
    """

    account_type: str
    """The type of bank account (e.g., checking, savings)."""

    bank_name: str
    """The name of the financial institution holding the account."""

    last4: str
    """The last four digits of the bank account number."""


class UsBankAccountPaymentMethod(BaseModel):
    """
    A saved US bank account payment method, including bank name, last four digits, and account type.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    created_at: datetime
    """The time of the event in ISO 8601 UTC format with millisecond precision"""

    payment_method_type: PaymentMethodTypes
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    typename: Literal["UsBankAccountPaymentMethod"]
    """The typename of this object"""

    us_bank_account: UsBankAccountPaymentMethodUsBankAccount
    """
    The bank account-specific details for this payment method, including bank name
    and last four digits.
    """


class CashappPaymentMethodCashapp(BaseModel):
    """
    The Cash App-specific details for this payment method, including cashtag and buyer ID.
    """

    buyer_id: Optional[str] = None
    """The unique and immutable identifier assigned by Cash App to the buyer.

    Null if not available.
    """

    cashtag: Optional[str] = None
    """The public cashtag handle of the buyer on Cash App. Null if not available."""


class CashappPaymentMethod(BaseModel):
    """
    A saved Cash App payment method, including the buyer's cashtag and unique identifier.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    cashapp: CashappPaymentMethodCashapp
    """
    The Cash App-specific details for this payment method, including cashtag and
    buyer ID.
    """

    created_at: datetime
    """The time of the event in ISO 8601 UTC format with millisecond precision"""

    payment_method_type: PaymentMethodTypes
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    typename: Literal["CashappPaymentMethod"]
    """The typename of this object"""


class IdealPaymentMethodIdeal(BaseModel):
    """
    The iDEAL-specific details for this payment method, including bank name and BIC.
    """

    bank: Optional[str] = None
    """The name of the customer's bank used for the iDEAL transaction.

    Null if not available.
    """

    bic: Optional[str] = None
    """The Bank Identifier Code (BIC/SWIFT) of the customer's bank.

    Null if not available.
    """


class IdealPaymentMethod(BaseModel):
    """A saved iDEAL payment method, including the customer's bank name and BIC code."""

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    created_at: datetime
    """The time of the event in ISO 8601 UTC format with millisecond precision"""

    ideal: IdealPaymentMethodIdeal
    """
    The iDEAL-specific details for this payment method, including bank name and BIC.
    """

    payment_method_type: PaymentMethodTypes
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    typename: Literal["IdealPaymentMethod"]
    """The typename of this object"""


class SepaDebitPaymentMethodSepaDebit(BaseModel):
    """
    The SEPA Direct Debit-specific details for this payment method, including bank code and last four IBAN digits.
    """

    bank_code: Optional[str] = None
    """The bank code of the financial institution associated with this SEPA account.

    Null if not available.
    """

    branch_code: Optional[str] = None
    """The branch code of the financial institution associated with this SEPA account.

    Null if not available.
    """

    country: Optional[str] = None
    """The two-letter ISO country code where the bank account is located.

    Null if not available.
    """

    last4: Optional[str] = None
    """The last four digits of the IBAN associated with this SEPA account.

    Null if not available.
    """


class SepaDebitPaymentMethod(BaseModel):
    """
    A saved SEPA Direct Debit payment method, including the bank code, country, and last four IBAN digits.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    created_at: datetime
    """The time of the event in ISO 8601 UTC format with millisecond precision"""

    payment_method_type: PaymentMethodTypes
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    sepa_debit: SepaDebitPaymentMethodSepaDebit
    """
    The SEPA Direct Debit-specific details for this payment method, including bank
    code and last four IBAN digits.
    """

    typename: Literal["SepaDebitPaymentMethod"]
    """The typename of this object"""


class PlatformBalancePaymentMethodPlatformBalanceBalance(BaseModel):
    """An available balance in one currency."""

    amount: float
    """The available amount in this currency."""

    currency: Currency
    """The currency this amount is held in."""


class PlatformBalancePaymentMethodPlatformBalance(BaseModel):
    """What is available to spend, and whether the account may spend it."""

    balances: List[PlatformBalancePaymentMethodPlatformBalanceBalance]
    """Available amount per currency.

    Read from the balance cache, so it is indicative — the charge revalidates
    against settled funds and may still refuse.
    """

    spendable: bool
    """
    Whether this balance can pay right now, which here means only whether it holds
    funds — an account blocked from spending is not listed at all. A zero balance is
    still returned so a client can show it as an option the buyer could top up.
    """


class PlatformBalancePaymentMethod(BaseModel):
    """The buyer's Whop balance, offered as a payment method.

    Charged by naming its ledger id on a `saved` confirmation token — it is a live wallet, not a stored credential, so it cannot be vaulted or charged off-session.
    """

    id: str
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """

    created_at: datetime
    """The time of the event in ISO 8601 UTC format with millisecond precision"""

    payment_method_type: PaymentMethodTypes
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    platform_balance: PlatformBalancePaymentMethodPlatformBalance
    """What is available to spend, and whether the account may spend it."""

    typename: Literal["PlatformBalancePaymentMethod"]
    """The typename of this object"""


PaymentMethodRetrieveResponse: TypeAlias = Annotated[
    Union[
        BasePaymentMethod,
        CardPaymentMethod,
        UsBankAccountPaymentMethod,
        CashappPaymentMethod,
        IdealPaymentMethod,
        SepaDebitPaymentMethod,
        PlatformBalancePaymentMethod,
    ],
    PropertyInfo(discriminator="typename"),
]
