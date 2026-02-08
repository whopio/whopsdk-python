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
    """The withdrawal amount.

    Provided as a number in the specified currency. Eg: 100.00 for $100.00 USD.
    """

    created_at: datetime
    """The datetime the withdrawal was created."""

    currency: Currency
    """The currency of the withdrawal request."""

    fee_amount: float
    """The fee amount that was charged for the withdrawal.

    This is in the same currency as the withdrawal amount.
    """

    fee_type: Optional[WithdrawalFeeTypes] = None
    """The different fee types for a withdrawal."""

    markup_fee: float
    """The markup fee that was charged for the withdrawal.

    This is in the same currency as the withdrawal amount. This only applies to
    platform accounts using Whop Rails.
    """

    speed: WithdrawalSpeeds
    """The speed of the withdrawal."""

    status: WithdrawalStatus
    """Status of the withdrawal."""
