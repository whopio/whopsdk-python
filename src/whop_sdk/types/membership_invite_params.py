# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["MembershipInviteParams", "InviteMembershipByUser", "InviteMembershipByEmail"]


class InviteMembershipByUser(TypedDict, total=False):
    plan_id: Required[str]
    """Free plan whose membership the recipient is invited to, prefixed `plan_`."""

    user_id: Required[str]
    """Recipient user ID, prefixed `user_`."""

    email: str
    """Recipient email address. Mutually exclusive with `user_id`."""


class InviteMembershipByEmail(TypedDict, total=False):
    email: Required[str]
    """Recipient email address."""

    plan_id: Required[str]
    """Free plan whose membership the recipient is invited to, prefixed `plan_`."""

    user_id: str
    """Recipient user ID, prefixed `user_`. Mutually exclusive with `email`."""


MembershipInviteParams: TypeAlias = Union[InviteMembershipByUser, InviteMembershipByEmail]
