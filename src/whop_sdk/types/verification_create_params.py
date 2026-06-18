# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationCreateParams"]


class VerificationCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account ID to verify (biz\\__ tag)."""

    address: Dict[str, object]
    """Optional pre-fill claim. Address (line1, city, state, postal_code)."""

    business_name: str
    """Optional pre-fill claim for businesses."""

    business_structure: str
    """Optional. Business structure (e.g. llc, corporation)."""

    country: str
    """Optional pre-fill claim.

    Country code; for businesses, the country of incorporation.
    """

    date_of_birth: str
    """Optional pre-fill claim.

    Seeds the Sumsub session; attested values come from Sumsub on approval.
    """

    first_name: str
    """Optional pre-fill claim.

    Seeds the Sumsub session; attested values come from Sumsub on approval.
    """

    kind: Literal["individual", "business"]
    """The verification type. Defaults to individual."""

    last_name: str
    """Optional pre-fill claim.

    Seeds the Sumsub session; attested values come from Sumsub on approval.
    """

    phone: str
    """Optional pre-fill claim — phone number."""

    place_of_incorporation: str
    """Optional.

    Place of incorporation (state/region); maps to the business address state.
    """

    restart: bool
    """Whether to restart an in-flight verification."""

    tax_identification_number: str
    """Optional.

    Tax identification number — SSN for individuals, EIN for businesses. Tokenized
    in transit, never stored raw; stored on the profile so the payout account,
    provisioned on approval, doesn't raise a tax-id RFI.
    """
