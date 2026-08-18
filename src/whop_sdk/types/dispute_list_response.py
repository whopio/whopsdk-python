# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.currency import Currency
from .dispute_statuses import DisputeStatuses

__all__ = [
    "DisputeListResponse",
    "Company",
    "Payment",
    "PaymentPaymentInstrument",
    "PaymentPaymentInstrumentIcons",
    "PaymentPaymentInstrumentIconsSquare",
    "PaymentPaymentInstrumentIconsSquareDark",
    "PaymentPaymentInstrumentIconsSquareLight",
    "Plan",
    "Product",
]


class Company(BaseModel):
    """The company that the dispute was filed against."""

    id: str
    """The unique identifier for the company."""

    title: str
    """The written name of the company."""


class PaymentPaymentInstrumentIconsSquareDark(BaseModel):
    """The colorway for dark surfaces."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class PaymentPaymentInstrumentIconsSquareLight(BaseModel):
    """The colorway for light surfaces."""

    svg: str
    """The vector file. Prefer this everywhere SVG renders."""


class PaymentPaymentInstrumentIconsSquare(BaseModel):
    """The square tile (32x32)."""

    dark: PaymentPaymentInstrumentIconsSquareDark
    """The colorway for dark surfaces."""

    light: PaymentPaymentInstrumentIconsSquareLight
    """The colorway for light surfaces."""


class PaymentPaymentInstrumentIcons(BaseModel):
    """
    The standard icon set: square and card shapes, each in light and dark colorways.
    """

    square: PaymentPaymentInstrumentIconsSquare
    """The square tile (32x32)."""


class PaymentPaymentInstrument(BaseModel):
    """
    The instrument this payment was made with, shaped for display: the method type, a buyer-facing name, the standard icon set, and the card facts when it was a card. Null when the receipt names no payment method.
    """

    display_name: str
    """
    Buyer-facing instrument name — "Visa •••• 4242" when the card surfaced, else the
    method's own name ("Klarna").
    """

    icons: PaymentPaymentInstrumentIcons
    """
    The standard icon set: square and card shapes, each in light and dark colorways.
    """

    installment_count: Optional[int] = None
    """Installment methods only: how many payments the charge splits into.

    Data, not copy — compose and translate the label client-side.
    """

    payment_method_type: str
    """The payment method type identifier, e.g. `card`, `klarna`, `apple_pay`."""


class Payment(BaseModel):
    """The original payment that was disputed."""

    id: str
    """The unique identifier for the payment."""

    payment_instrument: Optional[PaymentPaymentInstrument] = None
    """
    The instrument this payment was made with, shaped for display: the method type,
    a buyer-facing name, the standard icon set, and the card facts when it was a
    card. Null when the receipt names no payment method.
    """


class Plan(BaseModel):
    """The plan associated with the disputed payment.

    Null if the dispute is not linked to a specific plan.
    """

    id: str
    """The unique identifier for the plan."""


class Product(BaseModel):
    """The product associated with the disputed payment.

    Null if the dispute is not linked to a specific product.
    """

    id: str
    """The unique identifier for the product."""

    title: str
    """
    The display name of the product shown to customers on the product page and in
    search results.
    """


class DisputeListResponse(BaseModel):
    """
    A dispute is a chargeback or payment challenge filed against a company, including evidence and response status.
    """

    id: str
    """The unique identifier for the dispute."""

    amount: float
    """The disputed amount in the specified currency, formatted as a decimal."""

    company: Optional[Company] = None
    """The company that the dispute was filed against."""

    created_at: Optional[datetime] = None
    """The datetime the dispute was created."""

    currency: Currency
    """The three-letter ISO currency code for the disputed amount."""

    editable: Optional[bool] = None
    """Whether the dispute evidence can still be edited and submitted."""

    needs_response_by: Optional[datetime] = None
    """The deadline by which dispute evidence must be submitted.

    Null if no response deadline is set.
    """

    payment: Optional[Payment] = None
    """The original payment that was disputed."""

    plan: Optional[Plan] = None
    """The plan associated with the disputed payment.

    Null if the dispute is not linked to a specific plan.
    """

    product: Optional[Product] = None
    """The product associated with the disputed payment.

    Null if the dispute is not linked to a specific product.
    """

    reason: Optional[str] = None
    """A human-readable reason for the dispute."""

    reason_code: Optional[str] = None
    """The card network reason code for the dispute.

    Null when the payment processor did not provide one.
    """

    status: DisputeStatuses
    """
    The current status of the dispute lifecycle, such as needs_response,
    under_review, won, or lost.
    """

    visa_rdr: bool
    """
    Whether the dispute was automatically resolved through Visa Rapid Dispute
    Resolution (RDR).
    """
