# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SwapCreateResponse"]


class SwapCreateResponse(BaseModel):
    id: str
    """Swap ID — poll GET /swaps/{id} for status."""

    account_id: str

    object: Literal["swap"]

    status: str

    amount_out_expected: Optional[str] = None

    amount_out_min: Optional[str] = None

    rate: Optional[str] = None

    to_chain: Optional[str] = None
