# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TransferListResponse", "CreatedByUser"]


class CreatedByUser(BaseModel):
    """
    The user who initiated the transfer, such as the team member who sent a manual payout. Null if the creator is unavailable.
    """

    id: str
    """User ID."""

    username: str
    """User's username."""

    name: Optional[str] = None
    """User display name."""


class TransferListResponse(BaseModel):
    """A transfer of credit between two ledger accounts."""

    id: str
    """Transfer ID."""

    amount: float
    """Transfer amount."""

    created_at: datetime
    """When the transfer was created."""

    created_by_user: Optional[CreatedByUser] = None
    """
    The user who initiated the transfer, such as the team member who sent a manual
    payout. Null if the creator is unavailable.
    """

    currency: str
    """Transfer currency."""

    destination_ledger_account_id: str
    """Destination ledger account ID."""

    object: Literal["transfer"]
    """The object type."""

    origin_ledger_account_id: str
    """Source ledger account ID."""

    status: Literal["processing", "succeeded", "failed"]
    """Transfer status.

    `processing` means the on-chain leg is still executing — poll the transfer until
    it resolves to `succeeded` or `failed`. A `failed` transfer may be retried under
    the same ID and later resolve to `succeeded`.
    """

    failed_at: Optional[datetime] = None
    """When the transfer failed, as an ISO 8601 timestamp.

    Null unless the transfer has failed.
    """

    failure_code: Optional[str] = None
    """Machine-readable code for why the transfer failed.

    Null unless the transfer has failed.
    """

    failure_reason: Optional[str] = None
    """Human-readable explanation of why the transfer failed.

    Null unless the transfer has failed.
    """

    fee_amount: Optional[float] = None
    """Fee charged for the transfer."""

    metadata: Optional[Dict[str, builtins.object]] = None
    """Custom metadata attached to the transfer."""

    notes: Optional[str] = None
    """Transfer note."""
