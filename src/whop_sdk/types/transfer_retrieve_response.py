# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "TransferRetrieveResponse",
    "CreatedByUser",
    "Destination",
    "DestinationCompany",
    "DestinationUser",
    "Origin",
    "OriginCompany",
    "OriginUser",
]


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


class DestinationCompany(BaseModel):
    id: str
    """Account ID."""

    typename: Literal["Company"]

    route: Optional[str] = None
    """Account route."""

    title: Optional[str] = None
    """Account display name."""


class DestinationUser(BaseModel):
    id: str
    """User ID."""

    typename: Literal["User"]

    name: Optional[str] = None
    """User display name."""

    username: Optional[str] = None
    """User's username."""


Destination: TypeAlias = Annotated[Union[DestinationCompany, DestinationUser], PropertyInfo(discriminator="typename")]


class OriginCompany(BaseModel):
    id: str
    """Account ID."""

    typename: Literal["Company"]

    route: Optional[str] = None
    """Account route."""

    title: Optional[str] = None
    """Account display name."""


class OriginUser(BaseModel):
    id: str
    """User ID."""

    typename: Literal["User"]

    name: Optional[str] = None
    """User display name."""

    username: Optional[str] = None
    """User's username."""


Origin: TypeAlias = Annotated[Union[OriginCompany, OriginUser], PropertyInfo(discriminator="typename")]


class TransferRetrieveResponse(BaseModel):
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

    destination: Destination
    """Account or user receiving funds."""

    destination_ledger_account_id: str
    """Destination ledger account ID."""

    object: Literal["transfer"]
    """The object type. Discriminates the create response from a send or a claim link."""

    origin: Origin
    """Account or user sending funds."""

    origin_ledger_account_id: str
    """Source ledger account ID."""

    status: Literal["processing", "succeeded", "failed"]
    """Transfer status.

    `processing` means the on-chain leg is still executing — poll the transfer until
    it resolves to `succeeded` or `failed`.
    """

    fee_amount: Optional[float] = None
    """Fee charged for the transfer."""

    metadata: Optional[Dict[str, builtins.object]] = None
    """Custom metadata attached to the transfer."""

    notes: Optional[str] = None
    """Transfer note."""
