# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletBalanceResponse", "Balance"]


class Balance(BaseModel):
    address: Optional[str] = None

    amount: float

    chain_id: Optional[str] = None

    currency: str

    network: Optional[str] = None

    usd_value: float


class WalletBalanceResponse(BaseModel):
    available: str

    balances: List[Balance]

    object: Literal["balance"]

    pending: str

    total_usd: str
