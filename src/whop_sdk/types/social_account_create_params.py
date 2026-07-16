# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SocialAccountCreateParams"]


class SocialAccountCreateParams(TypedDict, total=False):
    platform: Required[Literal["facebook"]]
    """The platform to create the social account on."""

    account_id: str
    """The Account (biz\\__ identifier) to create the social account for.

    An account-scoped API key may omit this to default to its own account.
    """
