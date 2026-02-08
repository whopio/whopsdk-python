# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from .currency import Currency
from ..._models import BaseModel

__all__ = ["Transfer", "Destination", "DestinationUser", "DestinationCompany", "Origin", "OriginUser", "OriginCompany"]


class DestinationUser(BaseModel):
    """A user account on Whop.

    Contains profile information, identity details, and social connections.
    """

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    typename: Literal["User"]
    """The typename of this object"""

    username: str
    """The username of the user from their Whop account."""


class DestinationCompany(BaseModel):
    """A company is a seller on Whop.

    Companies own products, manage members, and receive payouts.
    """

    id: str
    """The unique identifier for the company."""

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
    """A user account on Whop.

    Contains profile information, identity details, and social connections.
    """

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    typename: Literal["User"]
    """The typename of this object"""

    username: str
    """The username of the user from their Whop account."""


class OriginCompany(BaseModel):
    """A company is a seller on Whop.

    Companies own products, manage members, and receive payouts.
    """

    id: str
    """The unique identifier for the company."""

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
    """Credit Transaction Transfer"""

    id: str
    """The unique identifier for the credit transaction transfer."""

    amount: float
    """The amount of the transfer.

    Provided as a number in the specified currency. Eg: 10.43 for $10.43 USD.
    """

    created_at: datetime
    """The datetime the credit transaction transfer was created."""

    currency: Currency
    """The currency of the credit transaction transfer"""

    destination: Destination
    """The recipient of the credit transaction transfer"""

    destination_ledger_account_id: str
    """The ID of the destination ledger account"""

    fee_amount: Optional[float] = None
    """The decimal fee of the credit transaction transfer"""

    metadata: Optional[Dict[str, object]] = None
    """Custom key-value pairs attached to the transfer.

    Max 50 keys, 500 chars per key, 5000 chars per value.
    """

    notes: Optional[str] = None
    """The notes of the credit transaction transfer"""

    origin: Origin
    """The sender of the credit transaction transfer"""

    origin_ledger_account_id: str
    """The ID of the origin ledger account"""
