# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationListResponse", "Data", "DataRequestedInformation", "DataRequestedInformationRequestedFile"]


class DataRequestedInformationRequestedFile(BaseModel):
    category: Optional[str] = None
    """
    Identifier to send back with the uploaded file so it routes correctly; null for
    a generic upload.
    """

    is_optional: Optional[bool] = None
    """Whether this slot can be left empty."""

    kind: Optional[str] = None
    """Provider-specific document kind, when applicable."""

    label: Optional[str] = None
    """Label for this upload slot (e.g. "Front of ID Document")."""

    multiple: Optional[bool] = None
    """Whether this slot accepts more than one file."""


class DataRequestedInformation(BaseModel):
    id: Optional[str] = None
    """The requested information item id (inrqi\\__\\**). Use this when answering."""

    description: Optional[str] = None
    """Additional guidance for the field beyond the label."""

    error_message: Optional[str] = None
    """The reason a previously submitted value was rejected, or null."""

    field: Optional[str] = None
    """Stable snake_case key for the field (e.g. ssn, business_description)."""

    label: Optional[str] = None
    """Human-readable label for the field (e.g. "Social Security Number")."""

    options: Optional[List[str]] = None
    """Allowed values for a `select` field (e.g.

    account_type, business_structure) — the submitted value must be one of these;
    empty for other types.
    """

    requested_files: Optional[List[DataRequestedInformationRequestedFile]] = None
    """
    Upload slots for a files item — always at least one when type is `files`, empty
    otherwise.
    """

    type: Optional[str] = None
    """How to render the input: text, date, phone, address, files, or select."""


class Data(BaseModel):
    id: Optional[str] = None
    """The verification ID, e.g. idpf\\__\\**"""

    address: Optional[object] = None

    business_name: Optional[str] = None

    business_structure: Optional[str] = None

    country: Optional[str] = None
    """ISO 3166-1 alpha-2 country code (e.g.

    `US`, `GB`). For individuals this is the country of citizenship or residence
    reported by the identity provider; for businesses this is the country of
    incorporation.
    """

    created_at: Optional[str] = None

    date_of_birth: Optional[str] = None

    first_name: Optional[str] = None

    kind: Optional[Literal["individual", "business"]] = None

    last_name: Optional[str] = None

    requested_information: Optional[List[DataRequestedInformation]] = None
    """
    The outstanding information this verification still needs — payout RFIs and
    audit RMIs, one uniform shape.
    """

    session_url: Optional[str] = None

    status: Optional[Literal["not_started", "pending", "approved", "rejected", "action_required"]] = None

    updated_at: Optional[str] = None


class VerificationListResponse(BaseModel):
    data: Optional[List[Data]] = None
