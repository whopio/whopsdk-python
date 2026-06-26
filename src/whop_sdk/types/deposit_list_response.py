# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DepositListResponse", "Bank"]


class Bank(BaseModel):
    id: str
    """Bank deposit transaction ID."""

    created_at: datetime
    """When the bank deposit transaction was created."""

    destination_amount: Optional[str] = None
    """Amount credited to the account balance."""

    destination_currency: Optional[str] = None
    """Currency credited to the account balance."""

    source_amount: str
    """Amount sent by the depositor."""

    source_currency: str
    """Currency sent by the depositor."""

    status: str
    """Current bank deposit status."""


class DepositListResponse(BaseModel):
    account_id: str
    """Account ID that owns these deposit transactions."""

    bank: List[Bank]
    """Bank deposit transactions for this account."""

    object: Literal["deposits"]
