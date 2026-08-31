# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MembershipUpdateParams"]


class MembershipUpdateParams(TypedDict, total=False):
    cancel_at_period_end: bool
    """
    `true` cancels at the end of the current billing period (the customer keeps
    access until then); `false` reverses a pending cancellation.
    """

    metadata: object
    """Key-value pairs to merge into the membership's metadata.

    Pass an empty object to clear it.
    """

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
