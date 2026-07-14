# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "VerificationUpdateParams",
    "UpdateIndividualVerification",
    "UpdateIndividualVerificationPersonalAddress",
    "UpdateIndividualVerificationRequestedInformation",
    "UpdateIndividualVerificationRequestedInformationAddress",
    "UpdateIndividualVerificationRequestedInformationFile",
    "UpdateBusinessVerification",
    "UpdateBusinessVerificationBusinessAddress",
    "UpdateBusinessVerificationRequestedInformation",
    "UpdateBusinessVerificationRequestedInformationAddress",
    "UpdateBusinessVerificationRequestedInformationFile",
]


class UpdateIndividualVerification(TypedDict, total=False):
    business_tax_identification_number: str
    """The business ID number of the company, as appropriate for the company's country.

    Examples are an Employer Identification Number (EIN) in the US, a Business
    Number in Canada, or a Company Number in the UK.
    """

    country: str
    """Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    date_of_birth: str
    """Formatted as `YYYY-MM-DD`."""

    first_name: str

    last_name: str

    personal_address: UpdateIndividualVerificationPersonalAddress
    """Personal address for the individual."""

    requested_information: Iterable[UpdateIndividualVerificationRequestedInformation]
    """Answers to items returned in `requested_information`.

    Each entry must include the requested item `id` and exactly one answer payload
    matching the item's `type`: `value` for `text`, `date`, or `phone`; `address`
    for `address`; `files` for `files`.
    """

    tax_identification_number: str
    """
    The government-issued ID number of the person being verified — the individual
    for a KYC verification, or the business representative for a KYB verification —
    as appropriate for their country. Examples are a Social Security Number (SSN) in
    the US, or a Social Insurance Number in Canada.
    """


class UpdateIndividualVerificationPersonalAddress(TypedDict, total=False):
    """Personal address for the individual."""

    city: str

    country: str
    """Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    line1: str
    """First line of the street address."""

    line2: str
    """Second line of the street address."""

    postal_code: str
    """Postal or ZIP code."""

    state: str
    """State, province, or region code, for example `CA`."""


class UpdateIndividualVerificationRequestedInformationAddress(TypedDict, total=False):
    """Address payload for `address` items."""

    city: str

    country: str
    """Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    line1: str
    """First line of the street address."""

    line2: str
    """Second line of the street address."""

    postal_code: str
    """Postal or ZIP code."""

    state: str
    """State, province, or region code, for example `CA`."""


class UpdateIndividualVerificationRequestedInformationFile(TypedDict, total=False):
    attachment_id: str
    """Existing attachment ID, when reusing an already attached document."""

    category: str
    """Requested file category copied from `requested_files.category`."""

    direct_upload_id: str
    """Direct upload ID for the uploaded document."""

    kind: str
    """Requested document kind copied from `requested_files.kind`."""


class UpdateIndividualVerificationRequestedInformation(TypedDict, total=False):
    id: Required[str]
    """Requested information item ID, prefixed `inrqi_`."""

    address: UpdateIndividualVerificationRequestedInformationAddress
    """Address payload for `address` items."""

    files: Iterable[UpdateIndividualVerificationRequestedInformationFile]
    """Uploaded file payloads for `files` items.

    Each file should include a `direct_upload_id` from the upload flow, plus the
    requested file `category` and `kind` when provided.
    """

    value: str
    """Answer value for `text`, `date`, or `phone` items."""

    value_type: Literal["raw", "vault_token"]
    """Whether `value` is raw input or a vault token."""


class UpdateBusinessVerification(TypedDict, total=False):
    business_address: UpdateBusinessVerificationBusinessAddress
    """Business address."""

    business_name: str
    """Legal business name."""

    business_structure: str
    """
    Legal entity structure of the business, such as `private_corporation` or
    `sole_proprietorship`. Supported values vary by country of incorporation — see
    [Business structures](/developer/verification/business-structures).
    """

    business_tax_identification_number: str
    """The business ID number of the company, as appropriate for the company's country.

    Examples are an Employer Identification Number (EIN) in the US, a Business
    Number in Canada, or a Company Number in the UK.
    """

    country: str
    """Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    requested_information: Iterable[UpdateBusinessVerificationRequestedInformation]
    """Answers to items returned in `requested_information`.

    Each entry must include the requested item `id` and exactly one answer payload
    matching the item's `type`: `value` for `text`, `date`, or `phone`; `address`
    for `address`; `files` for `files`.
    """

    tax_identification_number: str
    """
    The government-issued ID number of the person being verified — the individual
    for a KYC verification, or the business representative for a KYB verification —
    as appropriate for their country. Examples are a Social Security Number (SSN) in
    the US, or a Social Insurance Number in Canada.
    """


class UpdateBusinessVerificationBusinessAddress(TypedDict, total=False):
    """Business address."""

    city: str

    country: str
    """Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    line1: str
    """First line of the street address."""

    line2: str
    """Second line of the street address."""

    postal_code: str
    """Postal or ZIP code."""

    state: str
    """State, province, or region code, for example `CA`."""


class UpdateBusinessVerificationRequestedInformationAddress(TypedDict, total=False):
    """Address payload for `address` items."""

    city: str

    country: str
    """Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    line1: str
    """First line of the street address."""

    line2: str
    """Second line of the street address."""

    postal_code: str
    """Postal or ZIP code."""

    state: str
    """State, province, or region code, for example `CA`."""


class UpdateBusinessVerificationRequestedInformationFile(TypedDict, total=False):
    attachment_id: str
    """Existing attachment ID, when reusing an already attached document."""

    category: str
    """Requested file category copied from `requested_files.category`."""

    direct_upload_id: str
    """Direct upload ID for the uploaded document."""

    kind: str
    """Requested document kind copied from `requested_files.kind`."""


class UpdateBusinessVerificationRequestedInformation(TypedDict, total=False):
    id: Required[str]
    """Requested information item ID, prefixed `inrqi_`."""

    address: UpdateBusinessVerificationRequestedInformationAddress
    """Address payload for `address` items."""

    files: Iterable[UpdateBusinessVerificationRequestedInformationFile]
    """Uploaded file payloads for `files` items.

    Each file should include a `direct_upload_id` from the upload flow, plus the
    requested file `category` and `kind` when provided.
    """

    value: str
    """Answer value for `text`, `date`, or `phone` items."""

    value_type: Literal["raw", "vault_token"]
    """Whether `value` is raw input or a vault token."""


VerificationUpdateParams: TypeAlias = Union[UpdateIndividualVerification, UpdateBusinessVerification]
