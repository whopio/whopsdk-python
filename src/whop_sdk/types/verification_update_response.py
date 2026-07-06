# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationUpdateResponse", "RequestedInformation", "RequestedInformationRequestedFile"]


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


class VerificationUpdateResponse(BaseModel):
    id: Optional[str] = None
    """Verification profile ID, prefixed `idpf_`."""

    access_token: Optional[str] = None
    """
    Token for embedding the verification session directly in your own UI, as an
    alternative to redirecting to `session_url`. Follows the same presence rules as
    `session_url`.
    """

    address: Optional[object] = None
    """
    Personal or business address on the verification profile, with `line1`, `line2`,
    `city`, `state`, `postal_code`, and `country`. `null` when no address is set.
    """

    business_name: Optional[str] = None
    """Legal business name on a business verification."""

    business_structure: Optional[str] = None
    """Business entity type, such as `llc` or `corporation`."""

    country: Optional[str] = None
    """ISO 3166-1 alpha-2 country code for the individual or business being verified."""

    created_at: Optional[str] = None
    """When the verification profile was created, as an ISO 8601 timestamp."""

    date_of_birth: Optional[str] = None
    """Date of birth for an individual verification, formatted as `YYYY-MM-DD`."""

    first_name: Optional[str] = None
    """First name on an individual verification."""

    kind: Optional[Literal["individual", "business"]] = None
    """Verification type: `individual` for a person or `business` for a business."""

    last_name: Optional[str] = None
    """Last name on an individual verification."""

    requested_information: Optional[List[RequestedInformation]] = None
    """Fields or documents Whop still needs before review can continue.

    Submit answers with the Update Verification endpoint.
    """

    session_url: Optional[str] = None
    """Hosted verification session URL for the user to complete identity checks.

    Expires 7 days after creation. Omitted unless this verification's own status is
    `pending`; `null` if `pending` with no active session.
    """

    status: Optional[Literal["not_started", "pending", "approved", "rejected", "action_required"]] = None
    """Current verification state.

    `not_started` before any session has been created; `pending` while a session is
    in progress; `action_required` when items in `requested_information` need
    answers before review can continue; `approved` once verification succeeds;
    `rejected` if it fails. Call the Create Verification endpoint again to start a
    new session.
    """

    updated_at: Optional[str] = None
    """When the verification profile was last updated, as an ISO 8601 timestamp."""
