# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .card_brands import CardBrands
from .shared.currency import Currency
from .payment_method_type import PaymentMethodType

__all__ = [
    "PaymentMethodRetrieveResponse",
    "BasePaymentMethod",
    "BasePaymentMethodIcons",
    "BasePaymentMethodIconsCard",
    "BasePaymentMethodIconsCardDark",
    "BasePaymentMethodIconsCardLight",
    "BasePaymentMethodIconsSquare",
    "BasePaymentMethodIconsSquareDark",
    "BasePaymentMethodIconsSquareLight",
    "CardPaymentMethod",
    "CardPaymentMethodCard",
    "CardPaymentMethodIcons",
    "CardPaymentMethodIconsCard",
    "CardPaymentMethodIconsCardDark",
    "CardPaymentMethodIconsCardLight",
    "CardPaymentMethodIconsSquare",
    "CardPaymentMethodIconsSquareDark",
    "CardPaymentMethodIconsSquareLight",
    "UsBankAccountPaymentMethod",
    "UsBankAccountPaymentMethodIcons",
    "UsBankAccountPaymentMethodIconsCard",
    "UsBankAccountPaymentMethodIconsCardDark",
    "UsBankAccountPaymentMethodIconsCardLight",
    "UsBankAccountPaymentMethodIconsSquare",
    "UsBankAccountPaymentMethodIconsSquareDark",
    "UsBankAccountPaymentMethodIconsSquareLight",
    "UsBankAccountPaymentMethodUsBankAccount",
    "CashappPaymentMethod",
    "CashappPaymentMethodCashapp",
    "CashappPaymentMethodIcons",
    "CashappPaymentMethodIconsCard",
    "CashappPaymentMethodIconsCardDark",
    "CashappPaymentMethodIconsCardLight",
    "CashappPaymentMethodIconsSquare",
    "CashappPaymentMethodIconsSquareDark",
    "CashappPaymentMethodIconsSquareLight",
    "IdealPaymentMethod",
    "IdealPaymentMethodIcons",
    "IdealPaymentMethodIconsCard",
    "IdealPaymentMethodIconsCardDark",
    "IdealPaymentMethodIconsCardLight",
    "IdealPaymentMethodIconsSquare",
    "IdealPaymentMethodIconsSquareDark",
    "IdealPaymentMethodIconsSquareLight",
    "IdealPaymentMethodIdeal",
    "SepaDebitPaymentMethod",
    "SepaDebitPaymentMethodIcons",
    "SepaDebitPaymentMethodIconsCard",
    "SepaDebitPaymentMethodIconsCardDark",
    "SepaDebitPaymentMethodIconsCardLight",
    "SepaDebitPaymentMethodIconsSquare",
    "SepaDebitPaymentMethodIconsSquareDark",
    "SepaDebitPaymentMethodIconsSquareLight",
    "SepaDebitPaymentMethodSepaDebit",
    "PlatformBalancePaymentMethod",
    "PlatformBalancePaymentMethodIcons",
    "PlatformBalancePaymentMethodIconsCard",
    "PlatformBalancePaymentMethodIconsCardDark",
    "PlatformBalancePaymentMethodIconsCardLight",
    "PlatformBalancePaymentMethodIconsSquare",
    "PlatformBalancePaymentMethodIconsSquareDark",
    "PlatformBalancePaymentMethodIconsSquareLight",
    "PlatformBalancePaymentMethodPlatformBalance",
    "PlatformBalancePaymentMethodPlatformBalanceBalance",
]


class BasePaymentMethodIconsCardDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class BasePaymentMethodIconsCardLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class BasePaymentMethodIconsCard(BaseModel):
    """The credit-card-proportioned tile (48x30)."""

    dark: BasePaymentMethodIconsCardDark
    """The colorway for dark surfaces."""

    light: BasePaymentMethodIconsCardLight
    """The colorway for light surfaces."""


class BasePaymentMethodIconsSquareDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class BasePaymentMethodIconsSquareLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class BasePaymentMethodIconsSquare(BaseModel):
    """The square tile (32x32)."""

    dark: BasePaymentMethodIconsSquareDark
    """The colorway for dark surfaces."""

    light: BasePaymentMethodIconsSquareLight
    """The colorway for light surfaces."""


class BasePaymentMethodIcons(BaseModel):
    """Every rendition of the icon to display this payment method with.

    A saved card carries its brand's icon (Visa, Mastercard, ...) rather than the generic card art.
    """

    card: BasePaymentMethodIconsCard
    """The credit-card-proportioned tile (48x30)."""

    square: BasePaymentMethodIconsSquare
    """The square tile (32x32)."""


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

    icons: BasePaymentMethodIcons
    """Every rendition of the icon to display this payment method with.

    A saved card carries its brand's icon (Visa, Mastercard, ...) rather than the
    generic card art.
    """

    payment_method_type: PaymentMethodType
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

    expired: bool
    """Whether the card is past its expiration month.

    An expired card cannot take a new charge.
    """

    funding_type: Optional[Literal["credit", "debit", "prepaid"]] = None
    """The funding types of a card"""

    last4: Optional[str] = None
    """The last four digits of the card number. Null if not available."""

    three_ds_verified: bool
    """
    Whether this card was verified with 3D Secure, either when it was saved or on a
    payment that used it.
    """


class CardPaymentMethodIconsCardDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class CardPaymentMethodIconsCardLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class CardPaymentMethodIconsCard(BaseModel):
    """The credit-card-proportioned tile (48x30)."""

    dark: CardPaymentMethodIconsCardDark
    """The colorway for dark surfaces."""

    light: CardPaymentMethodIconsCardLight
    """The colorway for light surfaces."""


class CardPaymentMethodIconsSquareDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class CardPaymentMethodIconsSquareLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class CardPaymentMethodIconsSquare(BaseModel):
    """The square tile (32x32)."""

    dark: CardPaymentMethodIconsSquareDark
    """The colorway for dark surfaces."""

    light: CardPaymentMethodIconsSquareLight
    """The colorway for light surfaces."""


class CardPaymentMethodIcons(BaseModel):
    """Every rendition of the icon to display this payment method with.

    A saved card carries its brand's icon (Visa, Mastercard, ...) rather than the generic card art.
    """

    card: CardPaymentMethodIconsCard
    """The credit-card-proportioned tile (48x30)."""

    square: CardPaymentMethodIconsSquare
    """The square tile (32x32)."""


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

    icons: CardPaymentMethodIcons
    """Every rendition of the icon to display this payment method with.

    A saved card carries its brand's icon (Visa, Mastercard, ...) rather than the
    generic card art.
    """

    payment_method_type: PaymentMethodType
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    typename: Literal["CardPaymentMethod"]
    """The typename of this object"""


class UsBankAccountPaymentMethodIconsCardDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class UsBankAccountPaymentMethodIconsCardLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class UsBankAccountPaymentMethodIconsCard(BaseModel):
    """The credit-card-proportioned tile (48x30)."""

    dark: UsBankAccountPaymentMethodIconsCardDark
    """The colorway for dark surfaces."""

    light: UsBankAccountPaymentMethodIconsCardLight
    """The colorway for light surfaces."""


class UsBankAccountPaymentMethodIconsSquareDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class UsBankAccountPaymentMethodIconsSquareLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class UsBankAccountPaymentMethodIconsSquare(BaseModel):
    """The square tile (32x32)."""

    dark: UsBankAccountPaymentMethodIconsSquareDark
    """The colorway for dark surfaces."""

    light: UsBankAccountPaymentMethodIconsSquareLight
    """The colorway for light surfaces."""


class UsBankAccountPaymentMethodIcons(BaseModel):
    """Every rendition of the icon to display this payment method with.

    A saved card carries its brand's icon (Visa, Mastercard, ...) rather than the generic card art.
    """

    card: UsBankAccountPaymentMethodIconsCard
    """The credit-card-proportioned tile (48x30)."""

    square: UsBankAccountPaymentMethodIconsSquare
    """The square tile (32x32)."""


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

    icons: UsBankAccountPaymentMethodIcons
    """Every rendition of the icon to display this payment method with.

    A saved card carries its brand's icon (Visa, Mastercard, ...) rather than the
    generic card art.
    """

    payment_method_type: PaymentMethodType
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


class CashappPaymentMethodIconsCardDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class CashappPaymentMethodIconsCardLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class CashappPaymentMethodIconsCard(BaseModel):
    """The credit-card-proportioned tile (48x30)."""

    dark: CashappPaymentMethodIconsCardDark
    """The colorway for dark surfaces."""

    light: CashappPaymentMethodIconsCardLight
    """The colorway for light surfaces."""


class CashappPaymentMethodIconsSquareDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class CashappPaymentMethodIconsSquareLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class CashappPaymentMethodIconsSquare(BaseModel):
    """The square tile (32x32)."""

    dark: CashappPaymentMethodIconsSquareDark
    """The colorway for dark surfaces."""

    light: CashappPaymentMethodIconsSquareLight
    """The colorway for light surfaces."""


class CashappPaymentMethodIcons(BaseModel):
    """Every rendition of the icon to display this payment method with.

    A saved card carries its brand's icon (Visa, Mastercard, ...) rather than the generic card art.
    """

    card: CashappPaymentMethodIconsCard
    """The credit-card-proportioned tile (48x30)."""

    square: CashappPaymentMethodIconsSquare
    """The square tile (32x32)."""


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

    icons: CashappPaymentMethodIcons
    """Every rendition of the icon to display this payment method with.

    A saved card carries its brand's icon (Visa, Mastercard, ...) rather than the
    generic card art.
    """

    payment_method_type: PaymentMethodType
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    typename: Literal["CashappPaymentMethod"]
    """The typename of this object"""


class IdealPaymentMethodIconsCardDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class IdealPaymentMethodIconsCardLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class IdealPaymentMethodIconsCard(BaseModel):
    """The credit-card-proportioned tile (48x30)."""

    dark: IdealPaymentMethodIconsCardDark
    """The colorway for dark surfaces."""

    light: IdealPaymentMethodIconsCardLight
    """The colorway for light surfaces."""


class IdealPaymentMethodIconsSquareDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class IdealPaymentMethodIconsSquareLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class IdealPaymentMethodIconsSquare(BaseModel):
    """The square tile (32x32)."""

    dark: IdealPaymentMethodIconsSquareDark
    """The colorway for dark surfaces."""

    light: IdealPaymentMethodIconsSquareLight
    """The colorway for light surfaces."""


class IdealPaymentMethodIcons(BaseModel):
    """Every rendition of the icon to display this payment method with.

    A saved card carries its brand's icon (Visa, Mastercard, ...) rather than the generic card art.
    """

    card: IdealPaymentMethodIconsCard
    """The credit-card-proportioned tile (48x30)."""

    square: IdealPaymentMethodIconsSquare
    """The square tile (32x32)."""


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

    icons: IdealPaymentMethodIcons
    """Every rendition of the icon to display this payment method with.

    A saved card carries its brand's icon (Visa, Mastercard, ...) rather than the
    generic card art.
    """

    ideal: IdealPaymentMethodIdeal
    """
    The iDEAL-specific details for this payment method, including bank name and BIC.
    """

    payment_method_type: PaymentMethodType
    """
    The type of payment instrument stored on file (e.g., card, us_bank_account,
    cashapp, ideal, sepa_debit).
    """

    typename: Literal["IdealPaymentMethod"]
    """The typename of this object"""


class SepaDebitPaymentMethodIconsCardDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class SepaDebitPaymentMethodIconsCardLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class SepaDebitPaymentMethodIconsCard(BaseModel):
    """The credit-card-proportioned tile (48x30)."""

    dark: SepaDebitPaymentMethodIconsCardDark
    """The colorway for dark surfaces."""

    light: SepaDebitPaymentMethodIconsCardLight
    """The colorway for light surfaces."""


class SepaDebitPaymentMethodIconsSquareDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class SepaDebitPaymentMethodIconsSquareLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class SepaDebitPaymentMethodIconsSquare(BaseModel):
    """The square tile (32x32)."""

    dark: SepaDebitPaymentMethodIconsSquareDark
    """The colorway for dark surfaces."""

    light: SepaDebitPaymentMethodIconsSquareLight
    """The colorway for light surfaces."""


class SepaDebitPaymentMethodIcons(BaseModel):
    """Every rendition of the icon to display this payment method with.

    A saved card carries its brand's icon (Visa, Mastercard, ...) rather than the generic card art.
    """

    card: SepaDebitPaymentMethodIconsCard
    """The credit-card-proportioned tile (48x30)."""

    square: SepaDebitPaymentMethodIconsSquare
    """The square tile (32x32)."""


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

    icons: SepaDebitPaymentMethodIcons
    """Every rendition of the icon to display this payment method with.

    A saved card carries its brand's icon (Visa, Mastercard, ...) rather than the
    generic card art.
    """

    payment_method_type: PaymentMethodType
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


class PlatformBalancePaymentMethodIconsCardDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class PlatformBalancePaymentMethodIconsCardLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class PlatformBalancePaymentMethodIconsCard(BaseModel):
    """The credit-card-proportioned tile (48x30)."""

    dark: PlatformBalancePaymentMethodIconsCardDark
    """The colorway for dark surfaces."""

    light: PlatformBalancePaymentMethodIconsCardLight
    """The colorway for light surfaces."""


class PlatformBalancePaymentMethodIconsSquareDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class PlatformBalancePaymentMethodIconsSquareLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class PlatformBalancePaymentMethodIconsSquare(BaseModel):
    """The square tile (32x32)."""

    dark: PlatformBalancePaymentMethodIconsSquareDark
    """The colorway for dark surfaces."""

    light: PlatformBalancePaymentMethodIconsSquareLight
    """The colorway for light surfaces."""


class PlatformBalancePaymentMethodIcons(BaseModel):
    """Every rendition of the icon to display this payment method with.

    A saved card carries its brand's icon (Visa, Mastercard, ...) rather than the generic card art.
    """

    card: PlatformBalancePaymentMethodIconsCard
    """The credit-card-proportioned tile (48x30)."""

    square: PlatformBalancePaymentMethodIconsSquare
    """The square tile (32x32)."""


class PlatformBalancePaymentMethodPlatformBalanceBalance(BaseModel):
    """An amount of money.

    Never a bare number, because a bare number cannot answer the two questions a client has to answer to render it: what currency is this, and how many digits do I write? The second is stated twice rather than derived, because the digits the amount CARRIES and the digits to SHOW differ in COP — charged in centavos, written in whole pesos. Formatting is deliberately left to the caller: the number belongs in the buyer's locale, and this API does not know it.
    """

    amount: str
    """The amount in major units, as an exact decimal string — `"10.00"` is ten
    dollars.

    A string so no float rounds it in transit.
    """

    currency: Currency
    """Three-letter ISO 4217 currency code, lowercase."""

    decimals: int
    """
    How many decimal places the amount CARRIES — the precision the charge itself
    runs at.
    """

    display_decimals: int
    """How many decimal places to SHOW.

    Usually equal to `decimals`, and deliberately not always: COP is charged in
    centavos but written in whole pesos, so it is `2` and `0`. Format the number in
    your own locale using this.
    """


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

    icons: PlatformBalancePaymentMethodIcons
    """Every rendition of the icon to display this payment method with.

    A saved card carries its brand's icon (Visa, Mastercard, ...) rather than the
    generic card art.
    """

    payment_method_type: PaymentMethodType
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
