# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletBalanceResponse", "Token"]


class Token(BaseModel):
    balance: str

    icon_url: Optional[str] = None

    name: str

    price_usd: float

    symbol: str

    token_address: Optional[str] = None

    value_usd: str


class WalletBalanceResponse(BaseModel):
    object: Literal["balance"]

    tokens: List[Token]

    total_usd: str
