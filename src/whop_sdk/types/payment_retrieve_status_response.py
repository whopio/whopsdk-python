# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "PaymentRetrieveStatusResponse",
    "LastPaymentError",
    "NextAction",
    "NextActionPaymentNextActionRedirect",
    "NextActionPaymentNextActionRedirectData",
    "NextActionPaymentNextActionDisplayInstructions",
    "NextActionPaymentNextActionDisplayInstructionsData",
    "NextActionPaymentNextActionDisplayInstructionsDataPaymentVoucherInstructions",
    "NextActionPaymentNextActionDisplayInstructionsDataPaymentVoucherInstructionsVoucher",
    "NextActionPaymentNextActionDisplayInstructionsDataPaymentVoucherInstructionsVoucherAmount",
    "NextActionPaymentNextActionDisplayInstructionsDataPaymentQrInstructions",
    "NextActionPaymentNextActionDisplayInstructionsDataPaymentQrInstructionsQr",
    "NextActionPaymentNextActionDisplayInstructionsDataPaymentQrInstructionsQrAmount",
    "NextActionPaymentNextActionDisplayInstructionsDataPaymentBankTransferInstructions",
    "NextActionPaymentNextActionDisplayInstructionsDataPaymentBankTransferInstructionsBankTransfer",
    "NextActionPaymentNextActionDisplayInstructionsDataPaymentBankTransferInstructionsBankTransferAmount",
    "NextActionPaymentNextActionAwaitConfirmation",
    "NextActionPaymentNextActionAwaitConfirmationData",
    "ProcessingDetails",
]


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


class NextActionPaymentNextActionRedirectData(BaseModel):
    """Where to send the buyer."""

    frame_max_width: Optional[int] = None
    """
    The widest the provider's page lays out usefully, in CSS pixels — cap a frame or
    dialog presenting it at this width. `null` when the page fills whatever width it
    is given.
    """

    url: str
    """
    The provider's page for this payment, as an absolute URL — take the buyer there.
    """


class NextActionPaymentNextActionRedirect(BaseModel):
    data: NextActionPaymentNextActionRedirectData
    """Where to send the buyer."""

    render: List[Literal["inline", "full_page"]]

    type: Literal["redirect"]
    """Always `redirect`: send the buyer to `data.url`.

    The provider hands them back to `return_url` when they are done.
    """


class NextActionPaymentNextActionDisplayInstructionsDataPaymentVoucherInstructionsVoucherAmount(BaseModel):
    """Exactly what the buyer must pay, in the charged currency."""

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


class NextActionPaymentNextActionDisplayInstructionsDataPaymentVoucherInstructionsVoucher(BaseModel):
    """The voucher to show."""

    amount: Optional[NextActionPaymentNextActionDisplayInstructionsDataPaymentVoucherInstructionsVoucherAmount] = None
    """Exactly what the buyer must pay, in the charged currency."""

    barcode: Optional[str] = None
    """
    The barcode's contents, when the voucher carries one — render it in the
    symbology named by `barcode_format`.
    """

    barcode_format: Optional[str] = None
    """The symbology `barcode` is encoded in, such as `CODE_128`."""

    company_name: Optional[str] = None
    """Who the payment is made out to."""

    document_url: Optional[str] = None
    """A hosted page with the complete, printable instructions.

    If you would rather not render the details yourself, send the buyer here.
    """

    expires_at: Optional[str] = None
    """When the voucher stops being payable, as an ISO 8601 timestamp."""

    provider_logo: Optional[str] = None
    """URL of that network's logo."""

    provider_name: Optional[str] = None
    """The network the buyer pays at, such as OXXO."""

    reference: Optional[str] = None
    """The voucher's number — what the buyer reads out or types at the counter to pay."""


class NextActionPaymentNextActionDisplayInstructionsDataPaymentVoucherInstructions(BaseModel):
    kind: Literal["voucher"]
    """
    Always `voucher`: a code the buyer pays in person, at a convenience store or
    bank counter.
    """

    voucher: NextActionPaymentNextActionDisplayInstructionsDataPaymentVoucherInstructionsVoucher
    """The voucher to show."""


class NextActionPaymentNextActionDisplayInstructionsDataPaymentQrInstructionsQrAmount(BaseModel):
    """Exactly what the buyer must pay, in the charged currency."""

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


class NextActionPaymentNextActionDisplayInstructionsDataPaymentQrInstructionsQr(BaseModel):
    """The code to show."""

    amount: Optional[NextActionPaymentNextActionDisplayInstructionsDataPaymentQrInstructionsQrAmount] = None
    """Exactly what the buyer must pay, in the charged currency."""

    document_url: Optional[str] = None
    """A hosted page with the complete, printable instructions.

    If you would rather not render the details yourself, send the buyer here.
    """

    expires_at: Optional[str] = None
    """When the code stops being payable, as an ISO 8601 timestamp."""

    key: Optional[str] = None
    """
    An account key the buyer can pay to directly (Colombia's Bre-B llave), for apps
    that take a key instead of a scan.
    """

    qr_code: Optional[str] = None
    """
    The QR code's contents, ready to render as a scannable image — `qr_format` says
    how it is encoded.
    """

    qr_format: Optional[str] = None
    """How `qr_code` is encoded."""


class NextActionPaymentNextActionDisplayInstructionsDataPaymentQrInstructions(BaseModel):
    kind: Literal["qr"]
    """Always `qr`: a code the buyer scans with their banking app."""

    qr: NextActionPaymentNextActionDisplayInstructionsDataPaymentQrInstructionsQr
    """The code to show."""


class NextActionPaymentNextActionDisplayInstructionsDataPaymentBankTransferInstructionsBankTransferAmount(BaseModel):
    """Exactly what the buyer must send, in the charged currency."""

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


class NextActionPaymentNextActionDisplayInstructionsDataPaymentBankTransferInstructionsBankTransfer(BaseModel):
    """The account details to show."""

    account_number: Optional[str] = None
    """
    The account to send to, in the local scheme's format — `account_number_label`
    says what to call it.
    """

    account_number_label: Optional[str] = None
    """
    What to call `account_number` when showing it, in the local scheme's own terms —
    `CLABE` in Mexico, for example.
    """

    amount: Optional[
        NextActionPaymentNextActionDisplayInstructionsDataPaymentBankTransferInstructionsBankTransferAmount
    ] = None
    """Exactly what the buyer must send, in the charged currency."""

    bank_account_type: Optional[str] = None
    """
    The kind of account receiving the transfer, such as a checking account, in the
    local system's own vocabulary.
    """

    bank_branch: Optional[str] = None
    """The receiving branch, where the local system routes by branch."""

    bank_code: Optional[str] = None
    """The receiving bank's code in the local clearing system."""

    bank_name: Optional[str] = None
    """The receiving bank's name."""

    beneficiary_document: Optional[str] = None
    """
    The account holder's tax or identity document number, where the local system
    needs it to send.
    """

    beneficiary_document_type: Optional[str] = None
    """
    What kind of document `beneficiary_document` is, in the local system's own
    vocabulary.
    """

    beneficiary_name: Optional[str] = None
    """Who the account belongs to — the name the buyer's bank may ask them to confirm."""

    document_url: Optional[str] = None
    """A hosted page with the complete, printable instructions.

    If you would rather not render the details yourself, send the buyer here.
    """

    expires_at: Optional[str] = None
    """When these details stop being payable, as an ISO 8601 timestamp."""

    instructions: Optional[str] = None
    """The rail's own step-by-step payment text, when it supplies one."""

    reference: Optional[str] = None
    """
    The reference the buyer must attach to the transfer so it can be matched to this
    payment.
    """

    secondary_account_number: Optional[str] = None
    """
    A second account number, where the rail publishes the same destination in more
    than one format.
    """

    secondary_account_number_label: Optional[str] = None
    """What to call `secondary_account_number` when showing it."""


class NextActionPaymentNextActionDisplayInstructionsDataPaymentBankTransferInstructions(BaseModel):
    bank_transfer: NextActionPaymentNextActionDisplayInstructionsDataPaymentBankTransferInstructionsBankTransfer
    """The account details to show."""

    kind: Literal["bank_transfer"]
    """
    Always `bank_transfer`: account details the buyer sends money to from their own
    bank.
    """


NextActionPaymentNextActionDisplayInstructionsData: TypeAlias = Annotated[
    Union[
        NextActionPaymentNextActionDisplayInstructionsDataPaymentVoucherInstructions,
        NextActionPaymentNextActionDisplayInstructionsDataPaymentQrInstructions,
        NextActionPaymentNextActionDisplayInstructionsDataPaymentBankTransferInstructions,
    ],
    PropertyInfo(discriminator="kind"),
]


class NextActionPaymentNextActionDisplayInstructions(BaseModel):
    data: NextActionPaymentNextActionDisplayInstructionsData
    """The instructions.

    `kind` picks the shape, and the details sit under the key named for it:
    `voucher`, `qr`, or `bank_transfer`.
    """

    render: List[Literal["inline", "full_page"]]

    type: Literal["display_instructions"]
    """
    Always `display_instructions`: show the buyer `data` — what to pay, where, and
    by when. The payment completes once they pay and the rail confirms it, so keep
    polling `status`.
    """


class NextActionPaymentNextActionAwaitConfirmationData(BaseModel):
    """How long the wait can last."""

    expires_at: str
    """When the confirmation window closes, as an ISO 8601 timestamp.

    A payment still unconfirmed by then will not succeed — watch `status` for the
    failed attempt.
    """


class NextActionPaymentNextActionAwaitConfirmation(BaseModel):
    data: NextActionPaymentNextActionAwaitConfirmationData
    """How long the wait can last."""

    render: List[Literal["inline", "full_page"]]

    type: Literal["await_confirmation"]
    """
    Always `await_confirmation`: nothing to show — the buyer has done their part and
    the rail settles out of band. Poll `status` until it moves.
    """


NextAction: TypeAlias = Annotated[
    Union[
        NextActionPaymentNextActionRedirect,
        NextActionPaymentNextActionDisplayInstructions,
        NextActionPaymentNextActionAwaitConfirmation,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class ProcessingDetails(BaseModel):
    """Present while `status` is `processing` on a settlement rail, otherwise `null`."""

    expected_by: Optional[str] = None
    """When the payment is expected to settle, as an ISO 8601 timestamp."""


class PaymentRetrieveStatusResponse(BaseModel):
    id: str
    """The payment this status describes, prefixed `pay_`."""

    last_payment_error: Optional[LastPaymentError] = None
    """
    Details of the most recent failed attempt, or `null` when the payment has not
    failed.
    """

    next_action: Optional[NextAction] = None
    """What the buyer must do to finish.

    `type` picks the shape and each type carries only its own `data`, so switching
    on `type` gives you exactly that step's payload.
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
