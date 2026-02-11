# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .verification_status import VerificationStatus
from .verification_error_code import VerificationErrorCode

__all__ = ["VerificationRetrieveResponse"]


class VerificationRetrieveResponse(BaseModel):
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
