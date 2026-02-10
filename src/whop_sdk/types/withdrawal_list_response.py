# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.currency import Currency
from .withdrawal_speeds import WithdrawalSpeeds
from .withdrawal_status import WithdrawalStatus
from .withdrawal_fee_types import WithdrawalFeeTypes

__all__ = ["WithdrawalListResponse"]


class WithdrawalListResponse(BaseModel):
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

    fee_amount: float
    """
    The fee charged for processing this withdrawal, in the same currency as the
    withdrawal amount.
    """

    fee_type: Optional[WithdrawalFeeTypes] = None
    """The different fee types for a withdrawal."""

    markup_fee: float
    """
    An additional markup fee charged for the withdrawal, in the same currency as the
    withdrawal amount. Only applies to platform accounts using Whop Rails.
    """

    speed: WithdrawalSpeeds
    """The processing speed selected for this withdrawal ('standard' or 'instant')."""

    status: WithdrawalStatus
    """
    The computed lifecycle status of the withdrawal, accounting for the state of
    associated payouts (e.g., 'requested', 'in_transit', 'completed', 'failed').
    """
