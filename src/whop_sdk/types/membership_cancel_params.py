# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MembershipCancelParams"]


class MembershipCancelParams(TypedDict, total=False):
    reason: str
    """Free-form note recording why the membership was canceled."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
