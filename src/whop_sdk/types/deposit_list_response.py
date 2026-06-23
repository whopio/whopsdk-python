# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DepositListResponse", "Bank"]


class Bank(BaseModel):
    id: str

    created_at: datetime

    destination_amount: Optional[str] = None

    destination_currency: Optional[str] = None

    source_amount: str

    source_currency: str

    status: str


class DepositListResponse(BaseModel):
    account_id: str

    bank: List[Bank]

    object: Literal["deposits"]
