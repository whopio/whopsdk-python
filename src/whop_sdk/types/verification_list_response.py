# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationListResponse", "Data", "DataRfi", "DataRfiRequestedFile"]


class DataRfiRequestedFile(BaseModel):
    category: Optional[str] = None
    """Provider document category."""

    is_optional: Optional[bool] = None
    """Whether this document can be omitted."""

    kind: Optional[str] = None
    """Document kind to upload when answering the RFI."""


class DataRfi(BaseModel):
    id: Optional[str] = None
    """RFI ID to send when answering this request."""

    created_at: Optional[str] = None
    """When the RFI was created."""

    description: Optional[str] = None
    """Request text from verification provider."""

    error_message: Optional[str] = None
    """Provider error for invalid response, if any."""

    requested_files: Optional[List[DataRfiRequestedFile]] = None
    """Documents requested for a file-upload RFI."""

    status: Optional[Literal["outstanding", "invalid"]] = None
    """RFI status."""

    type: Optional[str] = None
    """Expected answer type for this RFI."""


class Data(BaseModel):
    id: Optional[str] = None
    """Verification ID, prefixed `idpf_`."""

    address: Optional[object] = None
    """Address associated with the verification profile."""

    business_name: Optional[str] = None
    """Legal business name for business verification."""

    business_structure: Optional[str] = None
    """Business entity structure, such as `llc` or `corporation`."""

    country: Optional[str] = None
    """Two-letter ISO 3166-1 country code reported by the identity provider."""

    created_at: Optional[str] = None
    """When the verification profile was created."""

    date_of_birth: Optional[str] = None
    """Date of birth for individual verification."""

    first_name: Optional[str] = None
    """First name for individual verification."""

    kind: Optional[Literal["individual", "business"]] = None
    """Verification profile type."""

    last_name: Optional[str] = None
    """Last name for individual verification."""

    rfis: Optional[List[DataRfi]] = None
    """
    Outstanding or invalid requests for information that must be answered to
    continue verification.
    """

    session_url: Optional[str] = None
    """Hosted provider session URL for pending verifications."""

    status: Optional[Literal["not_started", "pending", "approved", "rejected", "action_required"]] = None
    """Current verification status.

    `action_required` means one or more RFIs need a response.
    """

    updated_at: Optional[str] = None
    """When the verification profile was last updated."""


class VerificationListResponse(BaseModel):
    data: Optional[List[Data]] = None
    """Verification profiles for this account."""
