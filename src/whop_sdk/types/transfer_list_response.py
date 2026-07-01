# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["TransferListResponse"]


class TransferListResponse(BaseModel):
    """A transfer of credit between two ledger accounts."""

    id: str
    """Transfer ID."""

    amount: float
    """Transfer amount."""

    created_at: datetime
    """When the transfer was created."""

    currency: str
    """Transfer currency."""

    destination_ledger_account_id: str
    """Destination ledger account ID."""

    origin_ledger_account_id: str
    """Source ledger account ID."""

    fee_amount: Optional[float] = None
    """Fee charged for the transfer."""

    metadata: Optional[Dict[str, object]] = None
    """Custom metadata attached to the transfer."""

    notes: Optional[str] = None
    """Transfer note."""
