# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentUpdateReturnURLResponse", "LastPaymentError", "NextAction", "ProcessingDetails"]


class LastPaymentError(BaseModel):
    """
    Details of the most recent failed attempt, or `null` when the payment has not failed.
    """

    code: Optional[str] = None
    """A machine-readable classification of the failure."""

    decline_code: Optional[
        Literal[
            "insufficient_funds",
            "lost_card",
            "stolen_card",
            "expired_card",
            "suspected_fraud",
            "invalid_card_number",
            "invalid_cvc",
            "invalid_cvc_or_expiration",
            "incorrect_pin",
            "authentication_required",
            "card_not_supported",
            "currency_not_supported",
            "duplicate_transaction",
            "generic_decline",
            "invalid_account",
            "invalid_amount",
            "processing_error",
            "restricted_card",
            "card_velocity_exceeded",
            "contact_issuer",
            "bank_declined",
            "regulatory_blocked",
            "transaction_not_permitted",
            "transaction_stopped",
            "card_type_not_supported",
            "issuer_not_found",
            "closed_account",
            "issuer_unavailable",
            "invalid_zip",
            "invalid_expiry_month",
            "invalid_expiry_year",
            "invalid_expiry",
            "invalid_transaction",
            "cannot_authorize",
            "pin_required",
            "pin_try_exceeded",
            "provider_declined",
            "high_risk",
            "test_mode_decline",
            "merchant_blacklist",
            "reenter_transaction",
            "invalid_pin",
            "pin_required_as",
            "withdrawal_count_limit_exceeded",
            "invalid_country",
            "issuer_error",
            "invalid_card_holder_name",
            "no_accounts",
            "transaction_cancelled",
            "three_d_secure_success",
            "three_d_secure_canceled",
            "three_d_secure_invalid_card_number",
            "three_d_secure_generic_error",
            "three_d_secure_timeout",
            "three_d_secure_failed",
            "three_d_secure_card_not_enrolled",
            "three_d_secure_fraud",
            "three_d_secure_too_many_attempts",
            "three_d_secure_rejected_by_bank",
            "three_d_secure_reported_lost_or_stolen",
            "blocked_by_cardholder",
            "test_mode_test_card",
            "try_again_later",
            "transaction_not_allowed",
            "bank_insufficient_funds",
            "bank_account_not_found",
            "bank_account_closed",
            "bank_account_frozen",
            "bank_invalid_routing_number",
            "bank_non_transaction_account",
            "bank_authorization_revoked",
            "bank_payment_stopped",
            "bank_not_authorized",
            "bank_account_holder_deceased",
            "bank_duplicate",
            "bank_amount_error",
            "bank_regulatory_blocked",
            "bank_details_invalid",
            "bank_processing_error",
            "bank_generic_decline",
            "sepa_invalid_iban",
            "sepa_no_mandate",
            "sepa_mandate_data_invalid",
            "sepa_disputed",
            "sepa_refused_by_customer",
            "sepa_generic_decline",
        ]
    ] = None
    """The reason the payment was declined."""

    message: Optional[str] = None
    """A human-readable explanation of the failure."""


class NextAction(BaseModel):
    """
    What the buyer must do next while `status` is `requires_action`, otherwise `null`.
    """

    data: object
    """
    The payload for this step's type: `url` for `redirect`, `kind` plus that kind's
    details for `display_instructions`, `expires_at` for `await_confirmation`.
    """

    render: List[str]

    type: Literal["redirect", "display_instructions", "await_confirmation"]
    """What kind of step this is.

    `redirect` — send the buyer to `data.url`. `display_instructions` — show them
    `data`, such as a voucher code or bank transfer details. `await_confirmation` —
    nothing to show; they have done their part.
    """


class ProcessingDetails(BaseModel):
    """Present while `status` is `processing` on a settlement rail, otherwise `null`."""

    expected_by: Optional[str] = None
    """When the payment is expected to settle, as an ISO 8601 timestamp."""


class PaymentUpdateReturnURLResponse(BaseModel):
    id: str
    """The payment this status describes, prefixed `pay_`."""

    last_payment_error: Optional[LastPaymentError] = None
    """
    Details of the most recent failed attempt, or `null` when the payment has not
    failed.
    """

    next_action: Optional[NextAction] = None
    """
    What the buyer must do next while `status` is `requires_action`, otherwise
    `null`.
    """

    object: str
    """Always `payment_status`."""

    processing_details: Optional[ProcessingDetails] = None
    """Present while `status` is `processing` on a settlement rail, otherwise `null`."""

    return_url: Optional[str] = None
    """
    Where to send the buyer once the payment reaches a resting state, or `null` to
    leave them where they are. Editable until they return — see the return_url
    operation.
    """

    status: Literal["requires_confirmation", "requires_action", "confirming", "processing", "succeeded", "canceled"]
    """How far the payment has got.

    `requires_confirmation` — nothing attempted yet, or the last attempt failed and
    can be retried. `requires_action` — the buyer has a step outstanding; see
    `next_action`. `confirming` — the buyer has done their part and the processor is
    deciding. `processing` — the money is moving; see `processing_details`.
    `succeeded` — collected. `canceled` — voided or written off.
    """
