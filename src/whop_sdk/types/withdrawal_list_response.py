# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.currency import Currency
from .withdrawal_types import WithdrawalTypes
from .withdrawal_speeds import WithdrawalSpeeds
from .withdrawal_status import WithdrawalStatus
from .withdrawal_fee_types import WithdrawalFeeTypes

__all__ = ["WithdrawalListResponse"]


class WithdrawalListResponse(BaseModel):
    """A withdrawal request."""

    id: str
    """Internal ID of the withdrawal request."""

    amount: float
    """How much money was attempted to be withdrawn, in a float type."""

    created_at: datetime
    """When the withdrawal request was created."""

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

    withdrawal_type: WithdrawalTypes
    """The type of withdrawal."""
