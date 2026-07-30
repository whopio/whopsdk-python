# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SwapCreateResponse", "FromToken", "ToToken"]


class FromToken(BaseModel):
    """Fiat pairs only: the funding currency."""

    symbol: Optional[str] = None


class ToToken(BaseModel):
    """Fiat pairs only: the repaid currency."""

    symbol: Optional[str] = None


class SwapCreateResponse(BaseModel):
    account_id: str
    """Account ID that owns the wallet used for the swap."""

    object: Literal["swap"]

    status: Literal["queued", "working", "complete", "failed"]
    """Swap status.

    Crypto swaps start `queued`; fiat conversions return `complete`, or `working`
    while a stablecoin repayment settles.
    """

    id: Optional[str] = None
    """Swap ID. Poll `GET /swaps/:id` for status."""

    amount_in: Optional[float] = None
    """Fiat pairs only: amount of the funding currency converted.

    Null while a stablecoin repayment is processing.
    """

    amount_out: Optional[float] = None
    """Fiat pairs only: amount credited in the repaid currency.

    Null while a stablecoin repayment is processing.
    """

    amount_out_expected: Optional[str] = None
    """Expected destination token amount."""

    amount_out_min: Optional[str] = None
    """Minimum destination amount after slippage."""

    from_token: Optional[FromToken] = None
    """Fiat pairs only: the funding currency."""

    rate: Optional[str] = None
    """Quoted exchange rate used to create the swap."""

    to_chain: Optional[str] = None
    """Destination chain for the swap."""

    to_token: Optional[ToToken] = None
    """Fiat pairs only: the repaid currency."""
