# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .verification_status import VerificationStatus
from .verification_error_code import VerificationErrorCode

__all__ = ["VerificationRetrieveResponse"]


class VerificationRetrieveResponse(BaseModel):
    """An object representing an identity verification session"""

    id: str
    """The unique identifier for the verification."""

    last_error_code: Optional[VerificationErrorCode] = None
    """An error code for a verification attempt."""

    last_error_reason: Optional[str] = None
    """The last error reason that occurred during the verification."""

    status: VerificationStatus
    """The status of the verification."""
