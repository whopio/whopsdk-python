# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DisputeAlertListResponse"]


class DisputeAlertListResponse(BaseModel):
    id: str
    """Dispute alert ID, prefixed `dspa_`."""

    account_id: Optional[str] = None
    """The account the alerted payment belongs to, prefixed `biz_`.

    `null` while the alert is unmatched.
    """

    actionable: bool
    """Whether refunding the payment can still avoid a chargeback.

    `false` once the payment has been disputed or fully refunded, or when the alert
    could not be matched to a payment — `not_actionable_reason` says which.
    """

    amount: float
    """The alerted amount, in whole units of `currency`.

    This is what the issuer reported, which can differ from the payment's own
    amount.
    """

    card_brand: Optional[str] = None
    """
    The card network as reported by the issuer, lowercased, such as `visa` or
    `mastercard`. `unknown` when the report carries neither a network nor a
    recognizable BIN.
    """

    created_at: str
    """When Whop received the alert, as an ISO 8601 timestamp."""

    currency: str
    """Three-letter ISO currency code of the alerted amount."""

    fee_charged: bool
    """Whether Whop charged the account an alert fee for this one.

    Always `false` for `early_fraud_warning`, which Whop is not billed for and never
    passes on.
    """

    issuer: Optional[str] = None
    """Name of the bank that issued the card and filed the report."""

    not_actionable_reason: Optional[
        Literal["network_resolved", "payment_unmatched", "payment_not_captured", "payment_disputed", "payment_refunded"]
    ] = None
    """Why refunding can no longer avoid a chargeback.

    `network_resolved` when a Visa RDR already closed the case, `payment_unmatched`
    when no payment matched, `payment_not_captured` when it never captured money,
    `payment_disputed` once the payment carries a dispute, `payment_refunded` once
    fully refunded. `null` while `actionable` is true.
    """

    payment_id: Optional[str] = None
    """The payment the issuer reported, prefixed `pay_`.

    `null` when Whop could not match the report to a payment.
    """

    product_id: Optional[str] = None
    """The product the alerted payment was for, prefixed `prod_`."""

    reported_at: str
    """When the issuer filed the report, as an ISO 8601 timestamp.

    Earlier than `created_at`, which is when Whop received it.
    """

    transaction_at: Optional[str] = None
    """When the reported transaction was made, as an ISO 8601 timestamp."""

    type: Literal["early_fraud_warning", "dispute_alert", "rapid_dispute_resolution"]
    """What the issuer sent.

    `early_fraud_warning` is a fraud report on a settled payment (Visa TC40 /
    Mastercard SAFE) — refunding still avoids the chargeback, and Whop never charges
    a fee for one. `dispute_alert` is a pre-dispute notice from the issuer's alert
    network, which Whop pays for and passes on as a fee. `rapid_dispute_resolution`
    is a Visa RDR case the network already closed by refunding the payment — nothing
    is left to act on.
    """

    updated_at: str
    """When the alert was last changed, as an ISO 8601 timestamp."""
