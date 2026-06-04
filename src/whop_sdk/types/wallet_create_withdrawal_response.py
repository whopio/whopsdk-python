# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletCreateWithdrawalResponse"]


class WalletCreateWithdrawalResponse(BaseModel):
    id: str

    amount: str

    asset: str

    created_at: str

    object: Literal["withdrawal"]

    payout_method_id: str

    status: str

    fee_amount: Optional[str] = None

    fee_type: Optional[str] = None

    speed: Optional[str] = None
