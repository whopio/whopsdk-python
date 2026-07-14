# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "VerificationRetrieveResponse",
    "Address",
    "RequestedInformation",
    "RequestedInformationRequestedFile",
    "RequiredDocument",
]


class Address(BaseModel):
    """Address on the verification profile. `null` when no address is set."""

    city: Optional[str] = None

    country: Optional[str] = None
    """Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    line1: Optional[str] = None
    """First line of the street address."""

    line2: Optional[str] = None
    """Second line of the street address."""

    postal_code: Optional[str] = None
    """Postal or ZIP code."""

    state: Optional[str] = None
    """State, province, or region code, for example `CA`."""


class RequestedInformationRequestedFile(BaseModel):
    category: Optional[str] = None
    """
    File category to include with the uploaded file so Whop can route the document
    correctly. `null` for a generic upload.
    """

    is_optional: Optional[bool] = None
    """Whether this slot can be left empty."""

    kind: Optional[str] = None
    """Specific document type requested, such as `Bank Statement`.

    `null` for standard identity and business document uploads.
    """

    label: Optional[str] = None
    """Label for this upload slot, such as `Front of ID Document`."""

    multiple: Optional[bool] = None
    """Whether this slot accepts more than one file."""


class RequestedInformation(BaseModel):
    id: Optional[str] = None
    """Requested information item ID, prefixed `inrqi_`.

    Include this ID when submitting an answer.
    """

    description: Optional[str] = None
    """Additional instructions for this requested item, or `null`."""

    error_message: Optional[str] = None
    """Reason a previously submitted value was rejected.

    `null` if no submitted value has been rejected.
    """

    field: Optional[str] = None
    """Stable field key, such as `ssn` or `business_description`."""

    label: Optional[str] = None
    """Human-readable label for the field, such as `Social Security Number`."""

    options: Optional[List[str]] = None
    """Allowed values for a `select` field (e.g.

    account_type, business_structure) — the submitted value must be one of these;
    empty for other types.
    """

    requested_files: Optional[List[RequestedInformationRequestedFile]] = None
    """Document upload slots for this item.

    Present when `type` is `files`; upload one file for each required slot and
    include the slot's `category` when submitting the answer.
    """

    type: Optional[str] = None
    """
    Input type expected for this item: `text`, `date`, `phone`, `address`, `files`,
    or `select`.
    """


class RequiredDocument(BaseModel):
    document: Optional[str] = None
    """Document slot key, such as `id_card_front`, `id_card_back`, or `selfie`."""

    rejection_reason: Optional[str] = None
    """
    Why the previous submission was rejected, when the provider requested new
    documents or declined the verification.
    """

    status: Optional[Literal["pending_upload", "submitted"]] = None
    """
    `pending_upload` until the document has been relayed for review; `submitted`
    afterwards.
    """


class VerificationRetrieveResponse(BaseModel):
    id: Optional[str] = None
    """Verification profile ID, prefixed `idpf_`."""

    address: Optional[Address] = None
    """Address on the verification profile. `null` when no address is set."""

    business_name: Optional[str] = None
    """Legal business name."""

    business_structure: Optional[str] = None
    """
    Legal entity structure of the business, such as `private_corporation` or
    `sole_proprietorship`. Supported values vary by country of incorporation — see
    [Business structures](/developer/verification/business-structures).
    """

    country: Optional[str] = None
    """Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    created_at: Optional[str] = None
    """When the verification profile was created, as an ISO 8601 timestamp."""

    date_of_birth: Optional[str] = None
    """Formatted as `YYYY-MM-DD`."""

    first_name: Optional[str] = None

    kind: Optional[Literal["individual", "business"]] = None

    last_name: Optional[str] = None

    requested_information: Optional[List[RequestedInformation]] = None
    """Fields or documents Whop still needs before review can continue.

    Submit answers with the Update Verification endpoint.
    """

    required_documents: Optional[List[RequiredDocument]] = None
    """Documents for a document-upload verification and their progress.

    Present only on verifications created by sending `documents`. `pending_upload`
    documents were not accepted yet — send the full set again with another Create
    Verification call.
    """

    session_url: Optional[str] = None
    """Hosted verification session URL for the user to complete identity checks.

    Expires 7 days after creation.
    """

    status: Optional[Literal["not_started", "pending", "processing", "approved", "rejected", "action_required"]] = None
    """Current verification state.

    `not_started` before any session has been created; `pending` while a session is
    in progress and needs the user's input; `processing` while the provider reviews
    submitted documents — nothing to do but wait; `action_required` when items in
    `requested_information` need answers before review can continue; `approved` once
    verification succeeds; `rejected` if it fails. Call the Create Verification
    endpoint again to start a new session.
    """

    updated_at: Optional[str] = None
    """When the verification profile was last updated, as an ISO 8601 timestamp."""
