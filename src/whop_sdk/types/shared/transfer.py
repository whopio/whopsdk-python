# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from .currency import Currency
from ..._models import BaseModel

__all__ = ["Transfer", "Destination", "DestinationUser", "DestinationCompany", "Origin", "OriginUser", "OriginCompany"]


class DestinationUser(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    typename: Literal["User"]
    """The typename of this object"""

    username: str
    """The username of the user from their Whop account."""


class DestinationCompany(BaseModel):
    id: str
    """The ID (tag) of the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The title of the company."""

    typename: Literal["Company"]
    """The typename of this object"""


Destination: TypeAlias = Annotated[
    Union[Optional[DestinationUser], Optional[DestinationCompany]], PropertyInfo(discriminator="typename")
]


class OriginUser(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    typename: Literal["User"]
    """The typename of this object"""

    username: str
    """The username of the user from their Whop account."""


class OriginCompany(BaseModel):
    id: str
    """The ID (tag) of the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The title of the company."""

    typename: Literal["Company"]
    """The typename of this object"""


Origin: TypeAlias = Annotated[
    Union[Optional[OriginUser], Optional[OriginCompany]], PropertyInfo(discriminator="typename")
]


class Transfer(BaseModel):
    id: str
    """The unique identifier of the credit transaction transfer"""

    amount: float
    """The amount of the credit transaction transfer"""

    created_at: datetime
    """The timestamp when the credit transaction transfer was created"""

    currency: Currency
    """The currency of the credit transaction transfer"""

    destination: Destination
    """The recipient of the credit transaction transfer"""

    destination_ledger_account_id: str
    """The ID of the destination ledger account"""

    fee_amount: Optional[float] = None
    """The decimal fee of the credit transaction transfer"""

    notes: Optional[str] = None
    """The notes of the credit transaction transfer"""

    origin: Origin
    """The sender of the credit transaction transfer"""

    origin_ledger_account_id: str
    """The ID of the origin ledger account"""
