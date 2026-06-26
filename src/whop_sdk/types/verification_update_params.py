# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationUpdateParams", "Rfi"]


class VerificationUpdateParams(TypedDict, total=False):
    business_address: Dict[str, object]
    """Business address to submit for verification."""

    business_name: str
    """Legal business name to submit for verification."""

    business_structure: str
    """Business entity structure to submit for verification."""

    country: str
    """Country code to submit for verification."""

    date_of_birth: str
    """Date of birth to submit for individual verification."""

    first_name: str
    """First name to submit for individual verification."""

    last_name: str
    """Last name to submit for individual verification."""

    personal_address: Dict[str, object]
    """Personal address to submit for individual verification."""

    rfis: Iterable[Rfi]
    """Responses to outstanding RFIs.

    Each entry must include an RFI ID and a value, address, or files payload.
    """


class Rfi(TypedDict, total=False):
    id: Required[str]
    """RFI ID being answered."""

    address: Dict[str, object]
    """Address payload for address RFIs."""

    files: Iterable[object]
    """File upload payload for document RFIs."""

    value: str
    """Answer value for text, date, or phone RFIs."""

    value_type: Literal["raw", "vault_token"]
    """How the answer value is encoded. Defaults to `raw`."""
