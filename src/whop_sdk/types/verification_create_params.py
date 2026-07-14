# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "VerificationCreateParams",
    "CreateIndividualVerification",
    "CreateIndividualVerificationAddress",
    "CreateBusinessVerification",
    "CreateBusinessVerificationAddress",
]


class CreateIndividualVerification(TypedDict, total=False):
    account_id: Required[str]
    """Account or user ID whose identity you want to verify.

    Use a `biz_` account ID for account verifications, or the caller's `user_` ID
    for personal verification.
    """

    address: CreateIndividualVerificationAddress

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

    business_website: str
    """Business website URL. Whop store pages are not accepted."""

    country: str
    """Two-letter ISO 3166-1 country code, for example `US`, `DE`, or `GB`."""

    date_of_birth: str
    """Formatted as `YYYY-MM-DD`."""

    document_type: Literal["ID_CARD", "PASSPORT", "DRIVERS", "RESIDENCE_PERMIT"]
    """Identity document being sent.

    Providing it (with `documents`) verifies from uploaded documents instead of a
    hosted session, and determines the expected `documents` keys: cards and licenses
    need front and back, passports only the photo page.
    """

    documents: Dict[str, str]
    """
    Identity document files, keyed by slot (`id_card_front`, `id_card_back`,
    `selfie`, …) with each value the file's raw bytes base64-encoded. Providing them
    verifies the person from these documents instead of a hosted session —
    individual verifications only, and the request must also carry `document_type`,
    `first_name`, `last_name`, `date_of_birth`, `country`, `phone`,
    `tax_identification_number`, and an `address` with `line1`, `city`, `state`, and
    `postal_code`. JPEG, PNG, and PDF are accepted (selfies must be images), up to
    5MB per file before encoding. Send the complete set — a missing or rejected file
    fails the whole request and nothing is submitted; review starts automatically
    once every document is accepted.
    """

    first_name: str

    kind: Literal["individual"]
    """Verification type. Defaults to `individual`."""

    last_name: str

    phone: str

    tax_identification_number: str
    """
    The government-issued ID number of the person being verified — the individual
    for a KYC verification, or the business representative for a KYB verification —
    as appropriate for their country. Examples are a Social Security Number (SSN) in
    the US, or a Social Insurance Number in Canada.
    """


class CreateIndividualVerificationAddress(TypedDict, total=False):
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


class CreateBusinessVerification(TypedDict, total=False):
    account_id: Required[str]
    """Account or user ID whose identity you want to verify.

    Use a `biz_` account ID for account verifications, or the caller's `user_` ID
    for personal verification.
    """

    address: CreateBusinessVerificationAddress

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

    business_website: str
    """Business website URL. Whop store pages are not accepted."""

    country: str
    """Country of incorporation as a two-letter ISO 3166-1 country code."""

    kind: Literal["business"]
    """Must be `business` to start a KYB verification."""

    place_of_incorporation: str
    """State or region where the business is incorporated."""

    tax_identification_number: str
    """
    The government-issued ID number of the person being verified — the individual
    for a KYC verification, or the business representative for a KYB verification —
    as appropriate for their country. Examples are a Social Security Number (SSN) in
    the US, or a Social Insurance Number in Canada.
    """


class CreateBusinessVerificationAddress(TypedDict, total=False):
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


VerificationCreateParams: TypeAlias = Union[CreateIndividualVerification, CreateBusinessVerification]
