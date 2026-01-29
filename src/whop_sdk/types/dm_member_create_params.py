# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DmMemberCreateParams"]


class DmMemberCreateParams(TypedDict, total=False):
    channel_id: Required[str]
    """The ID of the DM channel to add the member to"""

    user_id: Required[str]
    """The ID of the user to add to the channel"""
