# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationRetrieveResponse"]


class VerificationRetrieveResponse(BaseModel):
    """An object representing an identity verification session"""

    id: str
    """A unique identifier for the verification."""

    last_error_code: Optional[
        Literal[
            "abandoned",
            "consent_declined",
            "country_not_supported",
            "device_not_supported",
            "document_expired",
            "document_type_not_supported",
            "document_unverified_other",
            "email_unverified_other",
            "email_verification_declined",
            "id_number_insufficient_document_data",
            "id_number_mismatch",
            "id_number_unverified_other",
            "phone_unverified_other",
            "phone_verification_declined",
            "selfie_document_missing_photo",
            "selfie_face_mismatch",
            "selfie_manipulated",
            "selfie_unverified_other",
            "under_supported_age",
        ]
    ] = None
    """An error code for a verification attempt."""

    last_error_reason: Optional[str] = None
    """The last error reason that occurred during the verification."""

    status: Literal[
        "requires_input",
        "processing",
        "verified",
        "canceled",
        "created",
        "started",
        "submitted",
        "approved",
        "declined",
        "resubmission_requested",
        "expired",
        "abandoned",
        "review",
    ]
    """The status of the verification."""
