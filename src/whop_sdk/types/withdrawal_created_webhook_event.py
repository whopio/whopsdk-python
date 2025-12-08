# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.currency import Currency
from .withdrawal_types import WithdrawalTypes
from .withdrawal_speeds import WithdrawalSpeeds
from .withdrawal_status import WithdrawalStatus
from .withdrawal_fee_types import WithdrawalFeeTypes

__all__ = ["WithdrawalCreatedWebhookEvent", "Data", "DataLedgerAccount", "DataPayoutToken"]


class DataLedgerAccount(BaseModel):
    """The ledger account associated with the withdrawal."""

    id: str
    """The ID of the LedgerAccount."""

    company_id: Optional[str] = None
    """The ID of the company associated with this ledger account."""


class DataPayoutToken(BaseModel):
    """The payout token used for the withdrawal, if applicable."""

    id: str
    """The ID of the payout token"""

    created_at: datetime
    """The date and time the payout token was created"""

    destination_currency_code: str
    """The currency code of the payout destination.

    This is the currency that payouts will be made in for this token.
    """

    nickname: Optional[str] = None
    """An optional nickname for the payout token to help the user identify it.

    This is not used by the provider and is only for the user's reference.
    """

    payer_name: Optional[str] = None
    """The name of the payer associated with the payout token."""


class Data(BaseModel):
    """A withdrawal request."""

    id: str
    """Internal ID of the withdrawal request."""

    amount: float
    """How much money was attempted to be withdrawn, in a float type."""

    created_at: datetime
    """When the withdrawal request was created."""

    currency: Currency
    """The currency of the withdrawal request."""

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
    """The error message for the withdrawal, if any."""

    estimated_availability: Optional[datetime] = None
    """The estimated availability date for the withdrawal, if any."""

    fee_amount: float
    """The fee amount that was charged for the withdrawal.

    This is in the same currency as the withdrawal amount.
    """

    fee_type: Optional[WithdrawalFeeTypes] = None
    """The different fee types for a withdrawal."""

    ledger_account: DataLedgerAccount
    """The ledger account associated with the withdrawal."""

    markup_fee: float
    """The markup fee that was charged for the withdrawal.

    This is in the same currency as the withdrawal amount. This only applies to
    platform accounts using Whop Rails.
    """

    payout_token: Optional[DataPayoutToken] = None
    """The payout token used for the withdrawal, if applicable."""

    speed: WithdrawalSpeeds
    """The speed of the withdrawal."""

    status: WithdrawalStatus
    """Status of the withdrawal."""

    trace_code: Optional[str] = None
    """The trace code for the payout, if applicable.

    Provided on ACH transactions when available.
    """

    withdrawal_type: WithdrawalTypes
    """The type of withdrawal."""


class WithdrawalCreatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    data: Data
    """A withdrawal request."""

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["withdrawal.created"]
    """The webhook event type"""
