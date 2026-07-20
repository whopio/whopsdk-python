# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["DepositCreateParams", "Destination", "DestinationUnionMember1"]


class DepositCreateParams(TypedDict, total=False):
    destination: Required[Destination]
    """Destination account ID or wallet address.

    Object form is supported for compatibility.
    """

    amount: float
    """Amount to prefill on hosted deposit page."""

    metadata: Dict[str, object]
    """Metadata to include with the deposit response."""

    network: Optional[str]
    """Destination network override."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class DestinationUnionMember1(TypedDict, total=False):
    account_id: str
    """Destination account ID."""

    address: str
    """Destination wallet address."""

    network: str
    """Destination wallet network."""


Destination: TypeAlias = Union[str, DestinationUnionMember1]
