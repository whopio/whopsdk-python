# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationUpdateParams", "Rfi"]


class VerificationUpdateParams(TypedDict, total=False):
    business_address: Dict[str, object]
    """The business address."""

    business_name: str
    """The business name."""

    business_structure: str
    """The business structure."""

    country: str
    """The country code."""

    date_of_birth: str
    """The date of birth."""

    first_name: str
    """The first name on the verification."""

    last_name: str
    """The last name on the verification."""

    personal_address: Dict[str, object]
    """The personal address."""

    rfis: Iterable[Rfi]
    """RFI responses.

    Each entry must include id and a value, address, or files payload.
    """


class Rfi(TypedDict, total=False):
    id: Required[str]
    """The RFI tag (paa\\__\\**)."""

    address: Dict[str, object]
    """Address payload for address RFIs."""

    files: Iterable[object]
    """File upload payload for document RFIs."""

    value: str
    """The value for text/date/phone RFIs."""

    value_type: Literal["raw", "vault_token"]
    """Defaults to raw."""
