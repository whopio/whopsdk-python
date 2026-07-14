# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SwapRetrieveResponse"]


class SwapRetrieveResponse(BaseModel):
    id: str
    """Swap ID."""

    account_id: str
    """Account ID that owns the wallet used for the swap."""

    object: Literal["swap"]

    status: str
    """Current swap status."""

    tx_hashes: List[str]
    """On-chain transaction hashes produced by the swap."""

    error: Optional[str] = None
    """Latest error returned for a failed swap."""
