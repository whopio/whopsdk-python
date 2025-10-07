# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.currency import Currency

__all__ = ["LedgerAccountRetrieveResponse", "Balance", "Owner", "OwnerUnionMember0", "OwnerUnionMember1"]


class Balance(BaseModel):
    balance: float
    """The amount of the balance."""

    currency: Currency
    """The currency of the balance."""

    pending_balance: float
    """The amount of the balance that is pending."""

    reserve_balance: float
    """The amount of the balance that is reserved."""


class OwnerUnionMember0(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    typename: Literal["PublicProfileUser"]
    """The typename of this object"""

    username: str
    """The username of the user from their Whop account."""


class OwnerUnionMember1(BaseModel):
    id: str
    """The ID (tag) of the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The title of the company."""

    typename: Literal["PublicCompany"]
    """The typename of this object"""


Owner: TypeAlias = Union[Optional[OwnerUnionMember0], Optional[OwnerUnionMember1]]


class LedgerAccountRetrieveResponse(BaseModel):
    id: str
    """The ID of the LedgerAccount."""

    balances: List[Balance]
    """The balances associated with the account."""

    ledger_account_audit_status: Optional[Literal["reserves_imposed", "requested_more_information"]] = None
    """The different statuses a LedgerAccountAudit can be"""

    ledger_type: Literal["primary", "pool"]
    """The type of ledger account."""

    owner: Owner
    """The owner of the ledger account."""

    payments_approval_status: Optional[Literal["pending", "approved", "monitoring", "rejected"]] = None
    """The different approval statuses an account can have."""

    transfer_fee: Optional[float] = None
    """The fee for transfers, if applicable."""
