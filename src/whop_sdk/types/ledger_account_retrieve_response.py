# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.currency import Currency

__all__ = [
    "LedgerAccountRetrieveResponse",
    "Balance",
    "Owner",
    "OwnerUser",
    "OwnerCompany",
    "PayoutAccountDetails",
    "PayoutAccountDetailsAddress",
    "PayoutAccountDetailsBusinessRepresentative",
]


class Balance(BaseModel):
    """A cached balance for a LedgerAccount in respect to a currency."""

    balance: float
    """The amount of the balance."""

    currency: Currency
    """The currency of the balance."""

    pending_balance: float
    """The amount of the balance that is pending."""

    reserve_balance: float
    """The amount of the balance that is reserved."""


class OwnerUser(BaseModel):
    """An object representing a (sanitized) user of the site."""

    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    typename: Literal["User"]
    """The typename of this object"""

    username: str
    """The username of the user from their Whop account."""


class OwnerCompany(BaseModel):
    """An object representing a (sanitized) company."""

    id: str
    """The ID (tag) of the company."""

    route: str
    """The slug/route of the company on the Whop site."""

    title: str
    """The title of the company."""

    typename: Literal["Company"]
    """The typename of this object"""


Owner: TypeAlias = Annotated[Union[Optional[OwnerUser], Optional[OwnerCompany]], PropertyInfo(discriminator="typename")]


class PayoutAccountDetailsAddress(BaseModel):
    """The physical address associated with this payout account"""

    city: Optional[str] = None
    """The city of the address."""

    country: Optional[str] = None
    """The country of the address."""

    line1: Optional[str] = None
    """The line 1 of the address."""

    line2: Optional[str] = None
    """The line 2 of the address."""

    postal_code: Optional[str] = None
    """The postal code of the address."""

    state: Optional[str] = None
    """The state of the address."""


class PayoutAccountDetailsBusinessRepresentative(BaseModel):
    """The business representative for this payout account"""

    date_of_birth: Optional[str] = None
    """
    The date of birth of the business representative in ISO 8601 format
    (YYYY-MM-DD).
    """

    first_name: Optional[str] = None
    """The first name of the business representative."""

    last_name: Optional[str] = None
    """The last name of the business representative."""

    middle_name: Optional[str] = None
    """The middle name of the business representative."""


class PayoutAccountDetails(BaseModel):
    """The payout account associated with the LedgerAccount, if any."""

    id: str
    """Unique identifier for the object"""

    address: Optional[PayoutAccountDetailsAddress] = None
    """The physical address associated with this payout account"""

    business_name: Optional[str] = None
    """The company's legal name"""

    business_representative: Optional[PayoutAccountDetailsBusinessRepresentative] = None
    """The business representative for this payout account"""

    email: Optional[str] = None
    """The email address of the representative"""

    phone: Optional[str] = None
    """The business representative's phone"""


class LedgerAccountRetrieveResponse(BaseModel):
    """Represents a LedgerAccount."""

    id: str
    """The ID of the LedgerAccount."""

    balances: List[Balance]
    """The balances associated with the account."""

    ledger_account_audit_status: Optional[
        Literal[
            "pending",
            "pending_ai_review",
            "approved",
            "reserves_imposed",
            "suspended",
            "ignored",
            "rejected",
            "requested_more_information",
            "information_submitted",
            "requested_tos_violation_correction",
            "clawback_attempted",
            "awaiting_sales_review",
        ]
    ] = None
    """The different statuses a LedgerAccountAudit can be"""

    ledger_type: Literal["primary", "pool"]
    """The type of ledger account."""

    owner: Owner
    """The owner of the ledger account."""

    payments_approval_status: Optional[Literal["pending", "approved", "monitoring", "rejected"]] = None
    """The different approval statuses an account can have."""

    payout_account_details: Optional[PayoutAccountDetails] = None
    """The payout account associated with the LedgerAccount, if any."""

    transfer_fee: Optional[float] = None
    """The fee for transfers, if applicable."""
