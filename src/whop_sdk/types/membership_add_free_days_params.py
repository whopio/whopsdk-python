# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MembershipAddFreeDaysParams"]


class MembershipAddFreeDaysParams(TypedDict, total=False):
    free_days: Required[int]
    """The number of free days to add (1-1095).

    Extends the billing period, expiration date, or Stripe trial depending on plan
    type.
    """
