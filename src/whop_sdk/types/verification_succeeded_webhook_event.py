# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .verification_status import VerificationStatus
from .verification_error_code import VerificationErrorCode

__all__ = ["VerificationSucceededWebhookEvent", "Data"]


class Data(BaseModel):
    """
    An identity verification session used to confirm a person or entity's identity for payout account eligibility.
    """

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


class VerificationSucceededWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    data: Data
    """
    An identity verification session used to confirm a person or entity's identity
    for payout account eligibility.
    """

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["verification.succeeded"]
    """The webhook event type"""

    company_id: Optional[str] = None
    """The company ID that this webhook event is associated with"""
