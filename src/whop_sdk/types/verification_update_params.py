# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "VerificationUpdateParams",
    "UpdateIndividualVerification",
    "UpdateIndividualVerificationPersonalAddress",
    "UpdateIndividualVerificationRequestedInformation",
    "UpdateIndividualVerificationRequestedInformationAddress",
    "UpdateIndividualVerificationRequestedInformationDocuments",
    "UpdateBusinessVerification",
    "UpdateBusinessVerificationBusinessAddress",
    "UpdateBusinessVerificationRequestedInformation",
    "UpdateBusinessVerificationRequestedInformationAddress",
    "UpdateBusinessVerificationRequestedInformationDocuments",
]


class UpdateIndividualVerification(TypedDict, total=False):
    business_name: str
    """Legal business name for a sole proprietor or single-member LLC."""

    business_structure: str
    """Entity type for sole proprietors, such as `single_member_llc`.

    Supported values vary by country of incorporation — see
    [Business structures](/developer/verification/business-structures).
    """

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
    """Answers to items in `requested_information`.

    Each entry pairs the item `id` with one answer payload matching its `type`.
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

    city: Optional[str]

    country: Optional[str]
    """Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    line1: Optional[str]
    """First line of the street address."""

    line2: Optional[str]
    """Second line of the street address."""

    postal_code: Optional[str]
    """Postal or ZIP code."""

    state: Optional[str]
    """State, province, or region code, for example `CA`."""


class UpdateIndividualVerificationRequestedInformationAddress(TypedDict, total=False):
    """Answer for `address` items."""

    city: Optional[str]

    country: Optional[str]
    """Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    line1: Optional[str]
    """First line of the street address."""

    line2: Optional[str]
    """Second line of the street address."""

    postal_code: Optional[str]
    """Postal or ZIP code."""

    state: Optional[str]
    """State, province, or region code, for example `CA`."""


class UpdateIndividualVerificationRequestedInformationDocuments(TypedDict, total=False):
    """
    Answer for an `id_document` item: the same slot keys Create Verification takes, so the key names both the document and the side. Send every slot for the ID you are uploading — `PASSPORT` is `passport_front`; `ID_CARD`, `DRIVERS` and `RESIDENCE_PERMIT` take a front and a back. Each value is a direct upload ID, or a `file_`-prefixed attachment ID to reuse an uploaded document.
    """

    drivers_back: str
    """Back of the driver's license."""

    drivers_front: str
    """Front of the driver's license."""

    id_card_back: str
    """Back of the ID card."""

    id_card_front: str
    """Front of the ID card."""

    passport_front: str
    """Photo page of the passport."""

    residence_permit_back: str
    """Back of the residence permit."""

    residence_permit_front: str
    """Front of the residence permit."""


class UpdateIndividualVerificationRequestedInformation(TypedDict, total=False):
    id: Required[str]
    """Item ID from `requested_information`."""

    address: UpdateIndividualVerificationRequestedInformationAddress
    """Answer for `address` items."""

    documents: UpdateIndividualVerificationRequestedInformationDocuments
    """
    Answer for an `id_document` item: the same slot keys Create Verification takes,
    so the key names both the document and the side. Send every slot for the ID you
    are uploading — `PASSPORT` is `passport_front`; `ID_CARD`, `DRIVERS` and
    `RESIDENCE_PERMIT` take a front and a back. Each value is a direct upload ID, or
    a `file_`-prefixed attachment ID to reuse an uploaded document.
    """

    files: SequenceNotStr[str]
    """
    Answer for a `files` item — one document, as a list of its pages, first page
    first. Each entry is a direct upload ID, or a `file_`-prefixed attachment ID to
    reuse an uploaded document.
    """

    value: str
    """
    Answer for `text`, `date`, `phone`, and `select` items, and the chosen document
    type for a `file` item that lists `options`.
    """

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

    date_of_birth: str
    """Business representative's date of birth, formatted as `YYYY-MM-DD`."""

    first_name: str
    """First name of the business representative."""

    last_name: str
    """Last name of the business representative."""

    requested_information: Iterable[UpdateBusinessVerificationRequestedInformation]
    """Answers to items in `requested_information`.

    Each entry pairs the item `id` with one answer payload matching its `type`.
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

    city: Optional[str]

    country: Optional[str]
    """Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    line1: Optional[str]
    """First line of the street address."""

    line2: Optional[str]
    """Second line of the street address."""

    postal_code: Optional[str]
    """Postal or ZIP code."""

    state: Optional[str]
    """State, province, or region code, for example `CA`."""


class UpdateBusinessVerificationRequestedInformationAddress(TypedDict, total=False):
    """Answer for `address` items."""

    city: Optional[str]

    country: Optional[str]
    """Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    line1: Optional[str]
    """First line of the street address."""

    line2: Optional[str]
    """Second line of the street address."""

    postal_code: Optional[str]
    """Postal or ZIP code."""

    state: Optional[str]
    """State, province, or region code, for example `CA`."""


class UpdateBusinessVerificationRequestedInformationDocuments(TypedDict, total=False):
    """
    Answer for an `id_document` item: the same slot keys Create Verification takes, so the key names both the document and the side. Send every slot for the ID you are uploading — `PASSPORT` is `passport_front`; `ID_CARD`, `DRIVERS` and `RESIDENCE_PERMIT` take a front and a back. Each value is a direct upload ID, or a `file_`-prefixed attachment ID to reuse an uploaded document.
    """

    drivers_back: str
    """Back of the driver's license."""

    drivers_front: str
    """Front of the driver's license."""

    id_card_back: str
    """Back of the ID card."""

    id_card_front: str
    """Front of the ID card."""

    passport_front: str
    """Photo page of the passport."""

    residence_permit_back: str
    """Back of the residence permit."""

    residence_permit_front: str
    """Front of the residence permit."""


class UpdateBusinessVerificationRequestedInformation(TypedDict, total=False):
    id: Required[str]
    """Item ID from `requested_information`."""

    address: UpdateBusinessVerificationRequestedInformationAddress
    """Answer for `address` items."""

    documents: UpdateBusinessVerificationRequestedInformationDocuments
    """
    Answer for an `id_document` item: the same slot keys Create Verification takes,
    so the key names both the document and the side. Send every slot for the ID you
    are uploading — `PASSPORT` is `passport_front`; `ID_CARD`, `DRIVERS` and
    `RESIDENCE_PERMIT` take a front and a back. Each value is a direct upload ID, or
    a `file_`-prefixed attachment ID to reuse an uploaded document.
    """

    files: SequenceNotStr[str]
    """
    Answer for a `files` item — one document, as a list of its pages, first page
    first. Each entry is a direct upload ID, or a `file_`-prefixed attachment ID to
    reuse an uploaded document.
    """

    value: str
    """
    Answer for `text`, `date`, `phone`, and `select` items, and the chosen document
    type for a `file` item that lists `options`.
    """

    value_type: Literal["raw", "vault_token"]
    """Whether `value` is raw input or a vault token."""


VerificationUpdateParams: TypeAlias = Union[UpdateIndividualVerification, UpdateBusinessVerification]
