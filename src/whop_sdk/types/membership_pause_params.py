# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MembershipPauseParams"]


class MembershipPauseParams(TypedDict, total=False):
    void_payments: Optional[bool]
    """
    Whether to void past_due payments associated with the membership to prevent
    future payment attempts.
    """
