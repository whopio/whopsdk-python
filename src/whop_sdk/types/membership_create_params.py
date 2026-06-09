# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MembershipCreateParams"]


class MembershipCreateParams(TypedDict, total=False):
    plan_id: Required[str]
    """The unique identifier of the free plan to grant.

    The plan's initial and renewal prices must both be zero.
    """

    user_id: Required[str]
    """The unique identifier of the user to grant the membership to."""

    metadata: Optional[Dict[str, object]]
    """Custom key-value pairs to attach to the membership."""
