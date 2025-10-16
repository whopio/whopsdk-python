# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["MembershipStatus"]

MembershipStatus: TypeAlias = Literal[
    "trialing", "active", "past_due", "completed", "canceled", "expired", "unresolved", "drafted"
]
