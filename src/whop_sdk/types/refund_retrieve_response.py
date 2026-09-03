# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RefundRetrieveResponse", "Amount", "OriginalAmount"]


class Amount(BaseModel):
    """
    The refunded amount as it settled, in the payment's settlement currency, so pages of refunds net against the payment's `refunded_amount`. Converted at the rate in force when the refund was issued, not the payment's original rate. Null only when no exchange rate is recorded for a legacy multi-currency payment.
    """

    amount: str
    """The amount in major units, as an exact decimal string — `"10.00"` is ten
    dollars.

    A string so no float rounds it in transit.
    """

    currency: str
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


class OriginalAmount(BaseModel):
    """The refunded amount in the currency the processor moved."""

    amount: str
    """The amount in major units, as an exact decimal string — `"10.00"` is ten
    dollars.

    A string so no float rounds it in transit.
    """

    currency: str
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


class RefundRetrieveResponse(BaseModel):
    id: str
    """Refund ID, prefixed `rf_`."""

    account_id: Optional[str] = None
    """The account that issued the refund, prefixed `biz_`."""

    amount: Optional[Amount] = None
    """
    The refunded amount as it settled, in the payment's settlement currency, so
    pages of refunds net against the payment's `refunded_amount`. Converted at the
    rate in force when the refund was issued, not the payment's original rate. Null
    only when no exchange rate is recorded for a legacy multi-currency payment.
    """

    created_at: str
    """When the refund was requested, as an ISO 8601 timestamp."""

    failure_message: Optional[str] = None
    """The provider's own explanation of the failure, or null."""

    failure_reason: Optional[
        Literal[
            "bank_declined",
            "expired_or_canceled_card",
            "lost_or_stolen_card",
            "insufficient_funds",
            "charge_disputed",
            "not_refundable",
            "merchant_request",
            "unknown",
        ]
    ] = None
    """Why the refund failed, normalized across providers.

    Null unless the refund failed or was canceled.
    """

    original_amount: OriginalAmount
    """The refunded amount in the currency the processor moved."""

    payment_id: str
    """The payment this refund reverses, prefixed `pay_`."""

    provider: str
    """The payment provider that processed the refund, such as `paypal` or `coinbase`."""

    provider_created_at: Optional[str] = None
    """When the provider created the refund, as an ISO 8601 timestamp."""

    reason: Optional[Literal["duplicate", "fraudulent", "requested_by_customer", "expired_uncaptured_charge"]] = None
    """Why the refund was issued, when recorded."""

    reference_status: Optional[Literal["available", "pending", "unavailable"]] = None
    """Whether a banking-network tracking reference is available for this refund."""

    reference_type: Optional[
        Literal["acquirer_reference_number", "retrieval_reference_number", "system_trace_audit_number"]
    ] = None
    """The kind of tracking reference, such as an acquirer reference number."""

    reference_value: Optional[str] = None
    """The tracking reference the buyer's bank can trace the refund by."""

    status: Literal["pending", "requires_action", "succeeded", "failed", "canceled"]
    """
    Where the refund stands with the processor: `pending`, `requires_action`,
    `succeeded`, `failed`, or `canceled`.
    """

    updated_at: str
    """When the refund last changed, as an ISO 8601 timestamp."""

    visa_rdr: bool
    """
    True when the card network initiated the refund through Rapid Dispute
    Resolution.
    """
