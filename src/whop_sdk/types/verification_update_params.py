# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationUpdateParams", "RequestedInformation"]


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

    requested_information: Iterable[RequestedInformation]
    """Answers to requested information.

    Each entry must include id and a value, address, or files payload.
    """


class RequestedInformation(TypedDict, total=False):
    id: Required[str]
    """The requested information item id (inrqi\\__\\**)."""

    address: Dict[str, object]
    """Address payload for address items."""

    files: Iterable[object]
    """File upload payload for document items."""

    value: str
    """The value for text/date/phone items."""

    value_type: Literal["raw", "vault_token"]
    """Defaults to the field's configured type."""
