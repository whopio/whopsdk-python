# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TeamMemberCreateParams"]


class TeamMemberCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID, prefixed `biz_`."""

    role: Required[Literal["owner", "admin", "sales_manager", "moderator", "advertiser"]]
    """The system role to grant."""

    user_id: Required[str]
    """The user to add to the team, prefixed `user_`."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
