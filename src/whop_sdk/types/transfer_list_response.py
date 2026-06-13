# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["TransferListResponse"]


class TransferListResponse(BaseModel):
    """A transfer of credit between two ledger accounts."""

    id: str

    amount: float

    created_at: datetime

    currency: str

    destination_ledger_account_id: str

    origin_ledger_account_id: str

    fee_amount: Optional[float] = None

    metadata: Optional[Dict[str, object]] = None

    notes: Optional[str] = None
