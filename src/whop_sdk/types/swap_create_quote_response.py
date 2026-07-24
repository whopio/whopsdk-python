# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SwapCreateQuoteResponse"]


class SwapCreateQuoteResponse(BaseModel):
    amount_in: str
    """Source token amount used for the quote."""

    amount_out: str
    """Estimated destination token amount."""

    fee_bps: int
    """Whop fee in basis points."""

    from_token: Dict[str, object]
    """Resolved source token details."""

    metadata: Dict[str, object]
    """Metadata from the request."""

    object: Literal["swap_quote"]

    rate: str
    """Quoted exchange rate."""

    to_token: Dict[str, builtins.object]
    """Resolved destination token details."""

    amount_out_min: Optional[str] = None
    """Minimum destination amount after slippage."""

    bridge_fee: Optional[str] = None
    """Estimated bridge fee for cross-chain swaps."""

    estimated_duration_seconds: Optional[int] = None
    """Estimated time for the swap to complete."""

    from_address: Optional[str] = None
    """Source wallet address used for the quote."""

    requires_token_approval: Optional[bool] = None
    """Whether the source token needs approval before swapping."""

    to_address: Optional[str] = None
    """Destination wallet address used for the quote."""
