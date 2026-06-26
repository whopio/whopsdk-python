# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SwapCreateResponse"]


class SwapCreateResponse(BaseModel):
    id: str
    """Swap ID. Poll `GET /swaps/:id` for status."""

    account_id: str
    """Account ID that owns the wallet used for the swap."""

    object: Literal["swap"]

    status: str
    """Initial swap status."""

    amount_out_expected: Optional[str] = None
    """Expected destination token amount."""

    amount_out_min: Optional[str] = None
    """Minimum destination amount after slippage."""

    rate: Optional[str] = None
    """Quoted exchange rate used to create the swap."""

    to_chain: Optional[str] = None
    """Destination chain for the swap."""
