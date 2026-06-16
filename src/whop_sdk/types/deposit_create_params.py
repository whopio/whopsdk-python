# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["DepositCreateParams", "Destination", "DestinationUnionMember1"]


class DepositCreateParams(TypedDict, total=False):
    destination: Required[Destination]
    """Destination account ID or wallet address.

    Object form is supported for compatibility.
    """

    amount: float
    """Optional amount to deposit."""

    metadata: Dict[str, object]
    """Arbitrary metadata echoed in the response."""

    network: Optional[str]
    """Optional destination network override."""


class DestinationUnionMember1(TypedDict, total=False):
    account_id: str

    address: str

    network: str


Destination: TypeAlias = Union[str, DestinationUnionMember1]
