# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .payment_method_types import PaymentMethodTypes

__all__ = [
    "SetupIntent",
    "LastSetupError",
    "PaymentInstrument",
    "PaymentInstrumentCard",
    "PaymentInstrumentIcons",
    "PaymentInstrumentIconsCard",
    "PaymentInstrumentIconsCardDark",
    "PaymentInstrumentIconsCardLight",
    "PaymentInstrumentIconsSquare",
    "PaymentInstrumentIconsSquareDark",
    "PaymentInstrumentIconsSquareLight",
    "User",
    "UserProfilePicture",
]


class LastSetupError(BaseModel):
    """Why the setup ended where it did, or `null` when nothing has failed.

    Present on `canceled` — a buyer who abandoned carries no code, one refused by the provider does. Dropped once the setup succeeds.
    """

    code: Optional[str] = None
    """A machine-readable classification of the failure, e.g.

    `enrollment_declined`. Absent when the buyer simply abandoned the setup.
    """

    message: Optional[str] = None
    """A human-readable explanation of the failure."""


class PaymentInstrumentCard(BaseModel):
    """
    Card payments only: the card's network, last four, and issuer identification number.
    """

    brand: Optional[str] = None
    """
    The network identifier (`visa`, `amex`, …), matching `card.networks` entries and
    saved card payment methods. Null when the vault did not record the network.
    """

    exp_month: Optional[float] = None
    """The card's expiry month, 1 to 12. Null when the vault did not record it."""

    exp_year: Optional[float] = None
    """The card's four-digit expiry year. Null when the vault did not record it."""

    issuer_identification_number: Optional[str] = None
    """
    The issuer identification number, also called the BIN: the card's leading six or
    eight digits, which identify the issuing bank. Null when the processor did not
    report it.
    """

    last4: Optional[str] = None
    """The card's last four digits, when captured."""


class PaymentInstrumentIconsCardDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class PaymentInstrumentIconsCardLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class PaymentInstrumentIconsCard(BaseModel):
    """The credit-card-proportioned tile (48x30)."""

    dark: PaymentInstrumentIconsCardDark
    """The colorway for dark surfaces."""

    light: PaymentInstrumentIconsCardLight
    """The colorway for light surfaces."""


class PaymentInstrumentIconsSquareDark(BaseModel):
    """The colorway for dark surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class PaymentInstrumentIconsSquareLight(BaseModel):
    """The colorway for light surfaces."""

    png_1x: str
    """Raster fallback at the shape's native size."""

    png_2x: str
    """Raster fallback at double density."""

    png_4x: str
    """Raster fallback at quadruple density."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class PaymentInstrumentIconsSquare(BaseModel):
    """The square tile (32x32)."""

    dark: PaymentInstrumentIconsSquareDark
    """The colorway for dark surfaces."""

    light: PaymentInstrumentIconsSquareLight
    """The colorway for light surfaces."""


class PaymentInstrumentIcons(BaseModel):
    """
    The standard icon set: square and card shapes, each in light and dark colorways.
    """

    card: PaymentInstrumentIconsCard
    """The credit-card-proportioned tile (48x30)."""

    square: PaymentInstrumentIconsSquare
    """The square tile (32x32)."""


class PaymentInstrument(BaseModel):
    """
    The method behind this setup shaped for display: a buyer-facing name, the standard icon set, and the card's brand, last four, issuer identification number, and expiry when it was a card. Null until a method was collected.
    """

    card: Optional[PaymentInstrumentCard] = None
    """
    Card payments only: the card's network, last four, and issuer identification
    number.
    """

    display_name: str
    """
    Buyer-facing instrument name — "Visa •••• 4242" when the card surfaced, else the
    method's own name ("Klarna").
    """

    icons: PaymentInstrumentIcons
    """
    The standard icon set: square and card shapes, each in light and dark colorways.
    """

    installment_count: Optional[float] = None
    """Installment methods only: how many payments the charge splits into.

    Data, not copy — compose and translate the label client-side.
    """

    payment_method_type: str
    """The payment method type identifier, e.g. `card`, `klarna`, `apple_pay`."""


class UserProfilePicture(BaseModel):
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when the user set no picture.
    """

    url: str
    """Avatar image URL.

    Always present — a generated placeholder when the user set no picture.
    """


class User(BaseModel):
    """The user saving the payment method.

    Null when the buyer is a company rather than a user.
    """

    id: str
    """User ID, prefixed `user_`."""

    name: Optional[str] = None
    """Display name."""

    profile_picture: UserProfilePicture
    """
    Avatar wrapper; its `url` is always present, using a generated placeholder when
    the user set no picture.
    """

    username: str
    """Public username."""


class SetupIntent(BaseModel):
    id: str
    """Setup intent ID, prefixed `sint_`."""

    account_id: Optional[str] = None
    """The account the payment method is saved for, prefixed `biz_`."""

    checkout_configuration_id: Optional[str] = None
    """The checkout configuration this setup was created through, prefixed `ch_`.

    Null for a setup created through this API rather than a hosted checkout.
    """

    client_secret: Optional[str] = None
    """
    The credential a buyer's surface presents to poll this setup and set its return
    URL — hand it to the elements' `handleNextAction`. Only on setups created
    through this API, and always null in list responses — retrieve the setup intent
    for it.
    """

    created_at: str
    """When the setup intent was created, as an ISO 8601 timestamp."""

    last_setup_error: Optional[LastSetupError] = None
    """Why the setup ended where it did, or `null` when nothing has failed.

    Present on `canceled` — a buyer who abandoned carries no code, one refused by
    the provider does. Dropped once the setup succeeds.
    """

    member_id: Optional[str] = None
    """The buyer's member record on the account, prefixed `mber_`.

    Null without the member:basic:read permission, unless the caller is the buyer.
    """

    metadata: Optional[object] = None
    """Your own key-value data attached when the setup intent was created."""

    payment_instrument: Optional[PaymentInstrument] = None
    """
    The method behind this setup shaped for display: a buyer-facing name, the
    standard icon set, and the card's brand, last four, issuer identification
    number, and expiry when it was a card. Null until a method was collected.
    """

    payment_method_id: Optional[str] = None
    """The saved payment method, prefixed `payt_`, ready to charge with Create Payment.

    Null until the setup has `succeeded`.
    """

    payment_method_type: Optional[PaymentMethodTypes] = None
    """The different types of payment methods that can be used."""

    return_url: Optional[str] = None
    """
    Where the buyer lands after completing an off-site step, or `null` to leave them
    where they are.
    """

    status: Literal["processing", "succeeded", "canceled", "requires_action"]
    """How far the setup has got.

    **A 201 or 200 means we answered, not that the method was saved — always branch
    on this.** `requires_action` — the buyer has a step outstanding; hand
    `client_secret` to the elements or poll Retrieve setup status. `processing` —
    the processor is deciding. `succeeded` — the method is saved, and only this one
    means saved. `canceled` — abandoned or refused; see `last_setup_error`.
    """

    three_ds_verified: bool
    """True when the buyer completed 3D Secure while saving this payment method."""

    updated_at: str
    """When the setup intent was last updated, as an ISO 8601 timestamp."""

    user: Optional[User] = None
    """The user saving the payment method.

    Null when the buyer is a company rather than a user.
    """
