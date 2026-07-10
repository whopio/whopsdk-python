# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationUpdateParams", "RequestedInformation", "RequestedInformationFile"]


class VerificationUpdateParams(TypedDict, total=False):
    business_address: Dict[str, object]
    """Updated business address for a business verification."""

    business_name: str
    """Updated legal business name for a business verification."""

    business_structure: str
    """Updated business entity type, such as `llc` or `corporation`."""

    country: str
    """Updated ISO 3166-1 alpha-2 country code."""

    date_of_birth: str
    """Updated date of birth for an individual verification."""

    first_name: str
    """Updated first name for an individual verification."""

    last_name: str
    """Updated last name for an individual verification."""

    personal_address: Dict[str, object]
    """Updated personal address for an individual verification."""

    requested_information: Iterable[RequestedInformation]
    """Answers to items returned in `requested_information`.

    Each entry must include the requested item `id` and exactly one answer payload
    matching the item's `type`: `value` for `text`, `date`, or `phone`; `address`
    for `address`; `files` for `files`.
    """


class RequestedInformationFile(TypedDict, total=False):
    attachment_id: str
    """Existing attachment ID, when reusing an already attached document."""

    category: str
    """Requested file category copied from `requested_files.category`."""

    direct_upload_id: str
    """Direct upload ID for the uploaded document."""

    kind: str
    """Requested document kind copied from `requested_files.kind`."""


class RequestedInformation(TypedDict, total=False):
    id: Required[str]
    """Requested information item ID, prefixed `inrqi_`."""

    address: Dict[str, object]
    """Address payload for address items."""

    files: Iterable[RequestedInformationFile]
    """Uploaded file payloads for `files` items.

    Each file should include a `direct_upload_id` from the upload flow, plus the
    requested file `category` and `kind` when provided.
    """

    value: str
    """Answer value for `text`, `date`, or `phone` items."""

    value_type: Literal["raw", "vault_token"]
    """Whether `value` is raw input or a vault token."""
