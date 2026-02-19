# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.currency import Currency
from .verification_status import VerificationStatus
from .verification_error_code import VerificationErrorCode

__all__ = [
    "LedgerAccountRetrieveResponse",
    "Balance",
    "Owner",
    "OwnerUser",
    "OwnerCompany",
    "PayoutAccountDetails",
    "PayoutAccountDetailsAddress",
    "PayoutAccountDetailsBusinessRepresentative",
    "PayoutAccountDetailsLatestVerification",
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


class OwnerCompany(BaseModel):
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


class PayoutAccountDetailsLatestVerification(BaseModel):
    """The latest verification for the connected account."""

    id: str
    """The unique identifier for the verification."""

    last_error_code: Optional[VerificationErrorCode] = None
    """An error code for a verification attempt."""

    last_error_reason: Optional[str] = None
    """A human-readable explanation of the most recent verification error.

    Null if no error has occurred.
    """

    status: VerificationStatus
    """The current status of this verification session."""


class PayoutAccountDetails(BaseModel):
    """The payout account associated with the LedgerAccount, if any."""

    id: str
    """The unique identifier for the payout account."""

    address: Optional[PayoutAccountDetailsAddress] = None
    """The physical address associated with this payout account"""

    business_name: Optional[str] = None
    """The company's legal name"""

    business_representative: Optional[PayoutAccountDetailsBusinessRepresentative] = None
    """The business representative for this payout account"""

    email: Optional[str] = None
    """The email address of the representative"""

    latest_verification: Optional[PayoutAccountDetailsLatestVerification] = None
    """The latest verification for the connected account."""

    phone: Optional[str] = None
    """The business representative's phone"""


class LedgerAccountRetrieveResponse(BaseModel):
    """
    A ledger account represents a financial account on Whop that can hold many balances.
    """

    id: str
    """The unique identifier for the ledger account."""

    balances: List[Balance]
    """The balances associated with the account."""

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
