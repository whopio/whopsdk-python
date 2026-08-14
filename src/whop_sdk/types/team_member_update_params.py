# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TeamMemberUpdateParams"]


class TeamMemberUpdateParams(TypedDict, total=False):
    role: Required[Literal["owner", "admin", "sales_manager", "moderator", "advertiser", "workforce"]]
    """The system role to grant."""
