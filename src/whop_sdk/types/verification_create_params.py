# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationCreateParams"]


class VerificationCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account ID to verify (biz\\__ tag)."""

    address: Dict[str, object]
    """Address to prefill in provider session."""

    business_name: str
    """Legal business name to prefill in provider session."""

    business_structure: str
    """Business entity structure, such as `llc` or `corporation`."""

    business_website: str
    """Business website URL for account verifications.

    Stored on the account and used when provisioning the payout account. Whop store
    pages are rejected.
    """

    country: str
    """Country code for provider session.

    For businesses, use the country of incorporation.
    """

    date_of_birth: str
    """Date of birth to prefill in provider session.

    Approved values come from the provider.
    """

    first_name: str
    """First name to prefill in provider session.

    Approved values come from the provider.
    """

    kind: Literal["individual", "business"]
    """Verification profile type. Defaults to `individual`."""

    last_name: str
    """Last name to prefill in provider session.

    Approved values come from the provider.
    """

    phone: str
    """Phone number to prefill in provider session."""

    place_of_incorporation: str
    """State or region of incorporation for business verification."""

    restart: bool
    """Whether to restart an in-flight verification."""

    tax_identification_number: str
    """Tax ID for verification, such as an SSN for individuals or EIN for businesses.

    Tokenized in transit and stored only on the profile.
    """
