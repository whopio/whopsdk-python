# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SocialAccountConnectParams"]


class SocialAccountConnectParams(TypedDict, total=False):
    platform: Required[Literal["meta_business", "tiktok"]]
    """The platform to connect the social account on.

    Supported options are `meta_business` and `tiktok`.
    """

    account_id: str
    """The Account (biz\\__ identifier) to connect the social account for.

    An account-scoped API key may omit this to default to its own account.
    """

    redirect_url: str
    """The Whop URL to redirect the user to after they finish connecting."""

    scopes: List[Literal["advertise"]]
    """Capabilities to grant for the connected social account.

    Use `advertise` when connecting a Meta Business or TikTok account for ads.
    """
