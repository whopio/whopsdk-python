# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["MembershipCancelParams"]


class MembershipCancelParams(TypedDict, total=False):
    cancellation_mode: Optional[Literal["at_period_end", "immediate"]]
    """The mode of cancellation for a membership"""
