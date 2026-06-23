# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SwapListResponse", "Data"]


class Data(BaseModel):
    id: str

    account_id: str

    object: Literal["swap"]

    status: str

    tx_hashes: List[str]

    error: Optional[str] = None


class SwapListResponse(BaseModel):
    data: List[Data]
