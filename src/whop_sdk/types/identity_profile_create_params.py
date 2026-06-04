# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .identity_profile_kind import IdentityProfileKind

__all__ = ["IdentityProfileCreateParams"]


class IdentityProfileCreateParams(TypedDict, total=False):
    kind: Required[IdentityProfileKind]
    """Which slot to verify: 'individual' (KYC) or 'business' (KYB)."""

    ledger_account_id: Required[str]
    """The ID of the LedgerAccount to verify (typically a company's primary ledger)."""

    address_city: Optional[str]
    """Optional pre-fill claim — city."""

    address_line1: Optional[str]
    """Optional pre-fill claim — street address line 1."""

    address_postal_code: Optional[str]
    """Optional pre-fill claim — postal code."""

    address_state: Optional[str]
    """Optional pre-fill claim — state/region."""

    country: Optional[str]
    """Optional pre-fill claim (ISO2 or ISO3 country code)."""

    date_of_birth: Optional[str]
    """Optional pre-fill claim (ISO date, e.g. 1990-05-15)."""

    first_name: Optional[str]
    """Optional pre-fill claim."""

    last_name: Optional[str]
    """Optional pre-fill claim."""

    phone: Optional[str]
    """Optional pre-fill claim."""

    restart: Optional[bool]
    """
    Force a fresh verification session, abandoning any session already in flight for
    this slot. Defaults to false, which resumes the in-flight session if one exists
    (avoiding duplicate Sumsub sessions).
    """
