# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SocialAccountCreateParams"]


class SocialAccountCreateParams(TypedDict, total=False):
    platform: Required[Literal["meta_business"]]
    """The platform to connect the social account on."""

    redirect_url: Required[str]
    """The Whop URL to redirect the user to after they finish connecting."""

    scopes: List[Literal["advertise"]]
    """
    Capabilities to grant for the connected social account, for example `advertise`.
    """
