# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MembershipExtendParams"]


class MembershipExtendParams(TypedDict, total=False):
    days: Required[int]
    """Number of free days to add (1-1095)."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
