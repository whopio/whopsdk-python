# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MembershipPauseParams"]


class MembershipPauseParams(TypedDict, total=False):
    until: str
    """ISO 8601 time to automatically resume payment collection.

    Must be in the future; only supported for memberships billed by Whop.
    """
