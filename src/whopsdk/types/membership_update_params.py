# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["MembershipUpdateParams"]


class MembershipUpdateParams(TypedDict, total=False):
    metadata: Optional[Dict[str, object]]
    """The metadata to update the membership with."""
