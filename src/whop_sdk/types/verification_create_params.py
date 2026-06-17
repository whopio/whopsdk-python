# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationCreateParams"]


class VerificationCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account ID to verify (biz\\__ tag)."""

    address: Dict[str, object]
    """Address (line1, city, state, postal_code).

    line1, city and postal_code are required for individuals when this request sets
    up the payout account; not required for businesses.
    """

    business_name: str
    """Business name. Required for businesses."""

    business_structure: str
    """Business structure (e.g. llc, corporation)."""

    country: str
    """Country code. Required. For businesses this is the country of incorporation."""

    date_of_birth: str
    """Date of birth.

    Required for individuals when this request sets up the payout account.
    """

    first_name: str
    """First name.

    Required for individuals when this request sets up the payout account.
    """

    kind: Literal["individual", "business"]
    """The verification type. Defaults to individual."""

    last_name: str
    """Last name.

    Required for individuals when this request sets up the payout account.
    """

    phone: str
    """Pre-fill the phone number."""

    place_of_incorporation: str
    """Place of incorporation (state/region).

    Required for businesses; maps to the address state.
    """

    restart: bool
    """Whether to restart an in-flight verification."""

    tax_identification_number: str
    """Tax identification number — SSN for individuals, EIN for businesses.

    Required for business; recommended for individuals. Tokenized in transit, never
    stored raw, and pre-fills the payout account's tax-id requirement so no RFI is
    raised for it.
    """
