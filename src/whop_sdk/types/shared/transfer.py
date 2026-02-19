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
    """The user's display name shown on their public profile."""

    typename: Literal["User"]
    """The typename of this object"""

    username: str
    """The user's unique username shown on their public profile."""


class DestinationCompany(BaseModel):
    """A company is a seller on Whop.

    Companies own products, manage members, and receive payouts.
    """

    id: str
    """The unique identifier for the company."""

    route: str
    """
    The URL slug for the company's store page (e.g., 'pickaxe' in whop.com/pickaxe).
    """

    title: str
    """The display name of the company shown to customers."""

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
    """The user's display name shown on their public profile."""

    typename: Literal["User"]
    """The typename of this object"""

    username: str
    """The user's unique username shown on their public profile."""


class OriginCompany(BaseModel):
    """A company is a seller on Whop.

    Companies own products, manage members, and receive payouts.
    """

    id: str
    """The unique identifier for the company."""

    route: str
    """
    The URL slug for the company's store page (e.g., 'pickaxe' in whop.com/pickaxe).
    """

    title: str
    """The display name of the company shown to customers."""

    typename: Literal["Company"]
    """The typename of this object"""


Origin: TypeAlias = Annotated[
    Union[Optional[OriginUser], Optional[OriginCompany]], PropertyInfo(discriminator="typename")
]


class Transfer(BaseModel):
    """A transfer of credit between two ledger accounts."""

    id: str
    """The unique identifier for the credit transaction transfer."""

    amount: float
    """The transfer amount in the currency specified by the currency field.

    For example, 10.43 represents $10.43 USD.
    """

    created_at: datetime
    """The datetime the credit transaction transfer was created."""

    currency: Currency
    """The currency in which this transfer amount is denominated."""

    destination: Destination
    """The entity receiving the transferred funds."""

    destination_ledger_account_id: str
    """The unique identifier of the ledger account receiving the funds."""

    fee_amount: Optional[float] = None
    """The flat fee amount deducted from this transfer, in the transfer's currency.

    Null if no flat fee was applied.
    """

    metadata: Optional[Dict[str, object]] = None
    """Custom key-value pairs attached to this transfer.

    Maximum 50 keys, 500 characters per key, 5000 characters per value.
    """

    notes: Optional[str] = None
    """A free-text note attached to this transfer by the sender.

    Null if no note was provided.
    """

    origin: Origin
    """The entity that sent the transferred funds."""

    origin_ledger_account_id: str
    """The unique identifier of the ledger account that sent the funds."""
