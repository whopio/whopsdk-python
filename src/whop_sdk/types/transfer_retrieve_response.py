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

    typename: Literal["Company"]

    route: Optional[str] = None

    title: Optional[str] = None


class DestinationUser(BaseModel):
    id: str

    typename: Literal["User"]

    name: Optional[str] = None

    username: Optional[str] = None


Destination: TypeAlias = Annotated[Union[DestinationCompany, DestinationUser], PropertyInfo(discriminator="typename")]


class OriginCompany(BaseModel):
    id: str

    typename: Literal["Company"]

    route: Optional[str] = None

    title: Optional[str] = None


class OriginUser(BaseModel):
    id: str

    typename: Literal["User"]

    name: Optional[str] = None

    username: Optional[str] = None


Origin: TypeAlias = Annotated[Union[OriginCompany, OriginUser], PropertyInfo(discriminator="typename")]


class TransferRetrieveResponse(BaseModel):
    """A transfer of credit between two ledger accounts."""

    id: str

    amount: float

    created_at: datetime

    currency: str

    destination: Destination

    destination_ledger_account_id: str

    origin: Origin

    origin_ledger_account_id: str

    fee_amount: Optional[float] = None

    metadata: Optional[Dict[str, object]] = None

    notes: Optional[str] = None
