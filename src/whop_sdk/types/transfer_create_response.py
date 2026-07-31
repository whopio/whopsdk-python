# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "TransferCreateResponse",
    "Transfer",
    "TransferDestination",
    "TransferDestinationCompany",
    "TransferDestinationUser",
    "TransferOrigin",
    "TransferOriginCompany",
    "TransferOriginUser",
    "Send",
    "SendDestination",
    "SendSource",
    "ClaimLink",
    "ClaimLinkSource",
]


class TransferDestinationCompany(BaseModel):
    id: str
    """Account ID."""

    typename: Literal["Company"]

    route: Optional[str] = None
    """Account route."""

    title: Optional[str] = None
    """Account display name."""


class TransferDestinationUser(BaseModel):
    id: str
    """User ID."""

    typename: Literal["User"]

    name: Optional[str] = None
    """User display name."""

    username: Optional[str] = None
    """User's username."""


TransferDestination: TypeAlias = Annotated[
    Union[TransferDestinationCompany, TransferDestinationUser], PropertyInfo(discriminator="typename")
]


class TransferOriginCompany(BaseModel):
    id: str
    """Account ID."""

    typename: Literal["Company"]

    route: Optional[str] = None
    """Account route."""

    title: Optional[str] = None
    """Account display name."""


class TransferOriginUser(BaseModel):
    id: str
    """User ID."""

    typename: Literal["User"]

    name: Optional[str] = None
    """User display name."""

    username: Optional[str] = None
    """User's username."""


TransferOrigin: TypeAlias = Annotated[
    Union[TransferOriginCompany, TransferOriginUser], PropertyInfo(discriminator="typename")
]


class Transfer(BaseModel):
    """A transfer of credit between two ledger accounts."""

    id: str
    """Transfer ID."""

    amount: float
    """Transfer amount."""

    created_at: datetime
    """When the transfer was created."""

    currency: str
    """Transfer currency."""

    destination: TransferDestination
    """Account or user receiving funds."""

    destination_ledger_account_id: str
    """Destination ledger account ID."""

    object: Literal["transfer"]
    """The object type. Discriminates the create response from a send or a claim link."""

    origin: TransferOrigin
    """Account or user sending funds."""

    origin_ledger_account_id: str
    """Source ledger account ID."""

    fee_amount: Optional[float] = None
    """Fee charged for the transfer."""

    metadata: Optional[Dict[str, builtins.object]] = None
    """Custom metadata attached to the transfer."""

    notes: Optional[str] = None
    """Transfer note."""


class SendDestination(BaseModel):
    account_id: str

    address: str


class SendSource(BaseModel):
    account_id: str

    address: str


class Send(BaseModel):
    """Returned for a wallet_send: an onchain USDT send to a recipient."""

    amount: str

    currency: str

    destination: SendDestination

    object: Literal["send"]

    source: SendSource

    tx_hash: str


class ClaimLinkSource(BaseModel):
    account_id: str


class ClaimLink(BaseModel):
    """Returned for a claim_link: a shareable URL anyone can open to claim the funds."""

    id: str

    amount: str

    claim_url: str

    currency: str

    expires_at: Optional[datetime] = None

    object: Literal["claim_link"]

    redeemable_count: int

    source: ClaimLinkSource

    status: Literal["pending"]
    """
    A newly funded claim link is always `pending` — it stays claimable until it is
    fully claimed, canceled, or expires.
    """


TransferCreateResponse: TypeAlias = Union[Transfer, Send, ClaimLink]
