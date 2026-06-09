# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletBalanceResponse", "Balance"]


class Balance(BaseModel):
    balance: float

    balance_usd: float

    currency: str

    pending_balance: float

    pending_balance_usd: float

    reserve_balance: float

    reserve_balance_usd: float

    withdrawable_balance: float

    withdrawable_balance_usd: float


class WalletBalanceResponse(BaseModel):
    balances: List[Balance]

    object: Literal["balance"]

    total_usd: str
