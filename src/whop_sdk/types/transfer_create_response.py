# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

    typename: Literal["Company"]

    route: Optional[str] = None

    title: Optional[str] = None


class TransferDestinationUser(BaseModel):
    id: str

    typename: Literal["User"]

    name: Optional[str] = None

    username: Optional[str] = None


TransferDestination: TypeAlias = Annotated[
    Union[TransferDestinationCompany, TransferDestinationUser], PropertyInfo(discriminator="typename")
]


class TransferOriginCompany(BaseModel):
    id: str

    typename: Literal["Company"]

    route: Optional[str] = None

    title: Optional[str] = None


class TransferOriginUser(BaseModel):
    id: str

    typename: Literal["User"]

    name: Optional[str] = None

    username: Optional[str] = None


TransferOrigin: TypeAlias = Annotated[
    Union[TransferOriginCompany, TransferOriginUser], PropertyInfo(discriminator="typename")
]


class Transfer(BaseModel):
    """A transfer of credit between two ledger accounts."""

    id: str

    amount: float

    created_at: datetime

    currency: str

    destination: TransferDestination

    destination_ledger_account_id: str

    origin: TransferOrigin

    origin_ledger_account_id: str

    fee_amount: Optional[float] = None

    metadata: Optional[Dict[str, object]] = None

    notes: Optional[str] = None


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

    status: str


TransferCreateResponse: TypeAlias = Union[Transfer, Send, ClaimLink]
