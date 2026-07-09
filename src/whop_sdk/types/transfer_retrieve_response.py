# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "TransferRetrieveResponse",
    "Destination",
    "DestinationCompany",
    "DestinationUser",
    "Origin",
    "OriginCompany",
    "OriginUser",
]


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

    currency: str
    """Transfer currency."""

    destination: Destination
    """Account or user receiving funds."""

    destination_ledger_account_id: str
    """Destination ledger account ID."""

    origin: Origin
    """Account or user sending funds."""

    origin_ledger_account_id: str
    """Source ledger account ID."""

    fee_amount: Optional[float] = None
    """Fee charged for the transfer."""

    metadata: Optional[Dict[str, object]] = None
    """Custom metadata attached to the transfer."""

    notes: Optional[str] = None
    """Transfer note."""
