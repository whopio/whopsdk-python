# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SwapCreateQuoteResponse"]


class SwapCreateQuoteResponse(BaseModel):
    amount_in: str

    amount_out: str

    cross_chain: bool

    fee_bps: int

    from_token: Dict[str, object]

    metadata: Dict[str, object]

    object: Literal["swap_quote"]

    rate: str

    to_token: Dict[str, builtins.object]

    amount_out_min: Optional[str] = None

    bridge_fee: Optional[str] = None

    estimated_duration_seconds: Optional[int] = None

    from_address: Optional[str] = None

    requires_token_approval: Optional[bool] = None

    to_address: Optional[str] = None
