# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountTransferOwnershipParams"]


class AccountTransferOwnershipParams(TypedDict, total=False):
    identifier: Required[str]
    """The user to transfer ownership to: a user ID (`user_*`) or an email address.

    An email address with no Whop account yet is sent an invite to create one.
    """
