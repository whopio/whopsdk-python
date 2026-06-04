# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .verification_status import VerificationStatus
from .verification_error_code import VerificationErrorCode

__all__ = ["IdentityProfileCreateResponse"]


class IdentityProfileCreateResponse(BaseModel):
    """
    An identity verification session used to confirm a person or entity's identity for payout account eligibility.
    """

    id: str
    """The numeric id of the verification record."""

    created_at: datetime
    """When the verification record was created."""

    last_error_code: Optional[VerificationErrorCode] = None
    """An error code for a verification attempt."""

    last_error_reason: Optional[str] = None
    """A human-readable explanation of the most recent verification error.

    Null if no error has occurred.
    """

    session_url: Optional[str] = None
    """A URL the user can visit to complete the verification process.

    Null if the session does not require user interaction.
    """

    status: VerificationStatus
    """The current status of this verification session."""
