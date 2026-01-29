# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["DmMemberUpdateParams"]


class DmMemberUpdateParams(TypedDict, total=False):
    notification_preference: Optional[Literal["all", "mentions", "none"]]
    """The notification preferences for a DMs feed member"""

    status: Optional[Literal["requested", "accepted", "hidden", "closed", "archived"]]
    """The statuses of a DMs feed member"""
