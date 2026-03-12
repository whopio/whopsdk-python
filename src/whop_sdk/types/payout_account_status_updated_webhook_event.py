# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .verification_status import VerificationStatus
from .verification_error_code import VerificationErrorCode

__all__ = [
    "PayoutAccountStatusUpdatedWebhookEvent",
    "Data",
    "DataAddress",
    "DataBusinessRepresentative",
    "DataLatestVerification",
]


class DataAddress(BaseModel):
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


class DataBusinessRepresentative(BaseModel):
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


class DataLatestVerification(BaseModel):
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


class Data(BaseModel):
    """An object representing an account used for payouts."""

    id: str
    """The unique identifier for the payout account."""

    address: Optional[DataAddress] = None
    """The physical address associated with this payout account"""

    business_name: Optional[str] = None
    """The company's legal name"""

    business_representative: Optional[DataBusinessRepresentative] = None
    """The business representative for this payout account"""

    email: Optional[str] = None
    """The email address of the representative"""

    latest_verification: Optional[DataLatestVerification] = None
    """The latest verification for the connected account."""

    phone: Optional[str] = None
    """The business representative's phone"""

    status: Optional[
        Literal[
            "connected", "disabled", "action_required", "pending_verification", "verification_failed", "not_started"
        ]
    ] = None
    """
    The granular calculated statuses reflecting payout account KYC and withdrawal
    readiness.
    """


class PayoutAccountStatusUpdatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    data: Data
    """An object representing an account used for payouts."""

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["payout_account.status_updated"]
    """The webhook event type"""

    company_id: Optional[str] = None
    """The company ID that this webhook event is associated with"""
