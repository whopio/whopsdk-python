# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "VerificationRetrieveResponse",
    "Address",
    "RequestedInformation",
    "RequestedInformationError",
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


class RequestedInformationError(BaseModel):
    code: Optional[str] = None
    """Stable error code."""

    reason: Optional[str] = None
    """Why it was rejected."""


class RequestedInformation(BaseModel):
    id: str
    """Requested information item ID, prefixed `inrqi_`."""

    label: str
    """Instruction to show the user.

    Carries the reviewer's note verbatim when there is one.
    """

    requirement: str
    """
    What is needed: a document name such as `bank_statement`, or a field key such as
    `ssn` or `identity_document`. Handle unrecognized values by `type`.
    """

    type: str
    """
    What to send as the answer, so you never have to infer it: `files` (a document,
    as a list of its pages), `id_document` (send `documents` with the slot keys for
    the ID you are uploading), `text`, `date`, `phone` or `select` (send `value`),
    or `address` (send `address`).
    """

    errors: Optional[List[RequestedInformationError]] = None
    """Present after a rejected submission."""

    optional: Optional[bool] = None
    """`true` when the item can be skipped."""

    options: Optional[List[str]] = None
    """The values `value` may take on a `select` item.

    On an `id_document` item these are the ID types accepted, and the chosen one
    decides which `documents` slots to send. Absent when the item has no choice to
    make.
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
    """What Whop still needs before review can continue — one requirement per entry.

    Answer with Update Verification; nothing from the response is echoed back. Keys
    that don't apply are omitted.
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

    status: Optional[
        Literal["not_started", "pending", "processing", "manual_review", "approved", "rejected", "action_required"]
    ] = None
    """Current verification state.

    `not_started` before any session exists; `pending` while a session needs the
    user's input; `processing` while the provider's automated checks run on a fresh
    submission; `action_required` when `requested_information` needs answers;
    `manual_review` while information already sent is under review — an audit
    answer, or a document the payout provider holds — nothing to submit, usually
    done within 3 business days; `approved` on success; `rejected` on failure. Call
    Create Verification again to start a new session.
    """

    updated_at: Optional[str] = None
    """When the verification profile was last updated, as an ISO 8601 timestamp."""
