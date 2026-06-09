# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationCreateParams"]


class VerificationCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account ID to verify (biz\\__ tag)."""

    address: Dict[str, object]
    """Pre-fill address (line1, city, state, postal_code)."""

    country: str
    """Pre-fill the country."""

    date_of_birth: str
    """Pre-fill the date of birth."""

    first_name: str
    """Pre-fill the first name."""

    kind: Literal["individual", "business"]
    """The verification type. Defaults to individual."""

    last_name: str
    """Pre-fill the last name."""

    phone: str
    """Pre-fill the phone number."""

    restart: bool
    """Whether to restart an in-flight verification."""
