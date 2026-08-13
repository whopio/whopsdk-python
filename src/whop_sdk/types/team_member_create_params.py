# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TeamMemberCreateParams"]


class TeamMemberCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID, prefixed `biz_`."""

    role: Required[Literal["owner", "admin", "sales_manager", "moderator", "advertiser", "workforce"]]
    """The system role to grant."""

    email: str
    """Email address to invite.

    Mutually exclusive with `user_id`. If the email already belongs to a Whop
    account it is treated the same as passing that account's `user_id`; otherwise a
    pending invite is created for the email.
    """

    user_id: str
    """The user to add to the team, prefixed `user_`. Mutually exclusive with `email`."""
