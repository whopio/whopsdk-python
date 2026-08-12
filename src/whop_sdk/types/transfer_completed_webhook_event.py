# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "TransferCompletedWebhookEvent",
    "Data",
    "DataCreatedByUser",
    "DataDestination",
    "DataDestinationCompany",
    "DataDestinationUser",
    "DataOrigin",
    "DataOriginCompany",
    "DataOriginUser",
]


class DataCreatedByUser(BaseModel):
    """
    The user who initiated the transfer, such as the team member who sent a manual payout. Null if the creator is unavailable.
    """

    id: str
    """User ID."""

    username: str
    """User's username."""

    name: Optional[str] = None
    """User display name."""


class DataDestinationCompany(BaseModel):
    id: str
    """Account ID."""

    typename: Literal["Company"]

    route: Optional[str] = None
    """Account route."""

    title: Optional[str] = None
    """Account display name."""


class DataDestinationUser(BaseModel):
    id: str
    """User ID."""

    typename: Literal["User"]

    name: Optional[str] = None
    """User display name."""

    username: Optional[str] = None
    """User's username."""


DataDestination: TypeAlias = Annotated[
    Union[DataDestinationCompany, DataDestinationUser], PropertyInfo(discriminator="typename")
]


class DataOriginCompany(BaseModel):
    id: str
    """Account ID."""

    typename: Literal["Company"]

    route: Optional[str] = None
    """Account route."""

    title: Optional[str] = None
    """Account display name."""


class DataOriginUser(BaseModel):
    id: str
    """User ID."""

    typename: Literal["User"]

    name: Optional[str] = None
    """User display name."""

    username: Optional[str] = None
    """User's username."""


DataOrigin: TypeAlias = Annotated[Union[DataOriginCompany, DataOriginUser], PropertyInfo(discriminator="typename")]


class Data(BaseModel):
    """A transfer of credit between two ledger accounts."""

    id: str
    """Transfer ID."""

    amount: float
    """Transfer amount."""

    created_at: datetime
    """When the transfer was created."""

    created_by_user: Optional[DataCreatedByUser] = None
    """
    The user who initiated the transfer, such as the team member who sent a manual
    payout. Null if the creator is unavailable.
    """

    currency: str
    """Transfer currency."""

    destination: DataDestination
    """Account or user receiving funds."""

    destination_ledger_account_id: str
    """Destination ledger account ID."""

    object: Literal["transfer"]
    """The object type. Discriminates the create response from a send or a claim link."""

    origin: DataOrigin
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


class TransferCompletedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    api_version_date: Optional[str] = None
    """The dated API version (Api-Version-Date) the payload is serialized to"""

    data: Data
    """A transfer of credit between two ledger accounts."""

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["transfer.completed"]
    """The webhook event type"""

    company_id: Optional[str] = None
    """The account ID that this webhook event is associated with"""
