# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MembershipPauseParams"]


class MembershipPauseParams(TypedDict, total=False):
    until: str
    """ISO 8601 time to automatically resume payment collection.

    Must be in the future; only supported for memberships billed by Whop.
    """

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
