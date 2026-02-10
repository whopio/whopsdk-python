# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.currency import Currency
from .withdrawal_speeds import WithdrawalSpeeds
from .withdrawal_status import WithdrawalStatus
from .withdrawal_fee_types import WithdrawalFeeTypes

__all__ = ["Withdrawal", "LedgerAccount", "PayoutToken"]


class LedgerAccount(BaseModel):
    """The ledger account from which the withdrawal funds are sourced."""

    id: str
    """The unique identifier for the ledger account."""

    company_id: Optional[str] = None
    """Represents a unique identifier that is Base64 obfuscated.

    It is often used to refetch an object or as key for a cache. The ID type appears
    in a JSON response as a String; however, it is not intended to be
    human-readable. When expected as an input type, any string (such as
    `"VXNlci0xMA=="`) or integer (such as `4`) input value will be accepted as an
    ID.
    """


class PayoutToken(BaseModel):
    """
    The saved payout destination used for this withdrawal (e.g., a bank account or PayPal address). Null if no payout token was used.
    """

    id: str
    """The unique identifier for the payout token."""

    created_at: datetime
    """The datetime the payout token was created."""

    destination_currency_code: str
    """
    The three-letter ISO currency code that payouts are delivered in for this
    destination.
    """

    nickname: Optional[str] = None
    """A user-defined label to help identify this payout destination.

    Not sent to the provider. Null if no nickname has been set.
    """

    payer_name: Optional[str] = None
    """The legal name of the account holder receiving payouts. Null if not provided."""


class Withdrawal(BaseModel):
    """
    A withdrawal represents a request to transfer funds from a company's ledger account to an external payout method.
    """

    id: str
    """The unique identifier for the withdrawal."""

    amount: float
    """
    The withdrawal amount as a decimal number in the specified currency (e.g.,
    100.00 for $100.00 USD).
    """

    created_at: datetime
    """The datetime the withdrawal was created."""

    currency: Currency
    """The three-letter ISO currency code for this withdrawal (e.g., 'usd', 'eur')."""

    error_code: Optional[
        Literal[
            "account_closed",
            "account_does_not_exist",
            "account_information_invalid",
            "account_number_invalid_region",
            "account_frozen",
            "account_lookup_failed",
            "account_not_found",
            "amount_out_of_bounds",
            "attributes_not_validated",
            "b2b_payments_prohibited",
            "bank_statement_required",
            "compliance_review",
            "currency_not_supported",
            "deposit_canceled",
            "deposit_failed",
            "deposit_rejected",
            "destination_unavailable",
            "exceeded_account_limit",
            "expired_quote",
            "generic_payout_error",
            "technical_problem",
            "identification_number_invalid",
            "invalid_account_number",
            "invalid_bank_code",
            "invalid_beneficiary",
            "invalid_mailing_address",
            "invalid_branch_number",
            "invalid_branch_code",
            "invalid_phone_number",
            "invalid_routing_number",
            "invalid_swift_code",
            "invalid_company_details",
            "manual_cancelation",
            "misc_error",
            "missing_city_and_country",
            "missing_phone_number",
            "missing_remittance_info",
            "payee_name_invalid",
            "receiving_account_locked",
            "rejected_by_compliance",
            "rtp_not_supported",
            "non_transaction_account",
            "source_token_insufficient_funds",
            "ssn_invalid",
            "wallet_screenshot_required",
            "unsupported_region",
        ]
    ] = None
    """The different error codes a payout can be in."""

    error_message: Optional[str] = None
    """A human-readable message describing why the payout failed.

    Null if no error occurred.
    """

    estimated_availability: Optional[datetime] = None
    """
    The estimated time at which the funds become available in the destination
    account. Null if no estimate is available. As a Unix timestamp.
    """

    fee_amount: float
    """
    The fee charged for processing this withdrawal, in the same currency as the
    withdrawal amount.
    """

    fee_type: Optional[WithdrawalFeeTypes] = None
    """The different fee types for a withdrawal."""

    ledger_account: LedgerAccount
    """The ledger account from which the withdrawal funds are sourced."""

    markup_fee: float
    """
    An additional markup fee charged for the withdrawal, in the same currency as the
    withdrawal amount. Only applies to platform accounts using Whop Rails.
    """

    payout_token: Optional[PayoutToken] = None
    """
    The saved payout destination used for this withdrawal (e.g., a bank account or
    PayPal address). Null if no payout token was used.
    """

    speed: WithdrawalSpeeds
    """The processing speed selected for this withdrawal ('standard' or 'instant')."""

    status: WithdrawalStatus
    """
    The computed lifecycle status of the withdrawal, accounting for the state of
    associated payouts (e.g., 'requested', 'in_transit', 'completed', 'failed').
    """

    trace_code: Optional[str] = None
    """The ACH trace number for tracking the payout through the banking network.

    Null if not available or not an ACH transaction.
    """
