# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SocialAccountDeleteParams"]


class SocialAccountDeleteParams(TypedDict, total=False):
    account_id: str
    """The Account that the social account is connected to.

    Provide either this or user_id.
    """

    user_id: str
    """The User that the social account is connected to.

    Provide either this or account_id.
    """
