# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationSucceededWebhookEvent", "Data"]


class Data(BaseModel):
    """
    An identity verification session used to confirm a person or entity's identity for payout account eligibility.
    """

    id: str
    """The numeric id of the verification record."""

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
    """A human-readable explanation of the most recent verification error.

    Null if no error has occurred.
    """

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
        "action_required",
    ]
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
