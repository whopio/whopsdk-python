# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationCreateParams"]


class VerificationCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account or user ID whose identity you want to verify.

    Use a `biz_` account ID for account verifications, or the caller's `user_` ID
    for personal verification.
    """

    address: Dict[str, object]
    """Address to prefill in the hosted verification session."""

    business_name: str
    """Legal business name to prefill for a business verification."""

    business_structure: str
    """
    Legal entity structure of the business, such as `private_corporation` or
    `sole_proprietorship`. Supported values vary by country of incorporation — see
    [Business structures](/developer/verification/business-structures).
    """

    business_website: str
    """Business website URL used during verification.

    Whop store pages are not accepted.
    """

    country: str
    """ISO 3166-1 alpha-2 country code.

    For businesses, use the country of incorporation.
    """

    date_of_birth: str
    """Date of birth to prefill in the hosted verification session."""

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
    """First name to prefill in the hosted verification session."""

    kind: Literal["individual", "business"]
    """Verification type. Defaults to `individual`."""

    last_name: str
    """Last name to prefill in the hosted verification session."""

    phone: str
    """Phone number to prefill in the hosted verification session."""

    place_of_incorporation: str
    """State or region where the business is incorporated."""

    restart: bool
    """Set to `true` to abandon the current in-flight session and start a new one."""

    tax_identification_number: str
    """Tax ID for the individual or business, such as an SSN or EIN.

    Tokenized in transit and never stored raw.
    """
