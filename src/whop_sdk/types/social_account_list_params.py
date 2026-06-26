# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["SocialAccountListParams"]


class SocialAccountListParams(TypedDict, total=False):
    account_id: str
    """The Account that the social accounts are connected to.

    Provide either this or user_id.
    """

    after: str
    """Cursor to fetch the page after (from page_info.end_cursor)."""

    before: str
    """Cursor to fetch the page before (from page_info.start_cursor)."""

    first: int
    """The number of social accounts to return."""

    last: int
    """The number of social accounts to return from the end of the range."""

    platform: Literal["x", "instagram", "youtube", "tiktok", "facebook"]
    """Only return social accounts for the platform that is specified."""

    scopes: List[Literal["advertise"]]
    """Only return social accounts that have these scopes."""

    user_id: str
    """The User that the social accounts are connected to.

    Provide either this or account_id.
    """

    verified: bool
    """Only return social accounts that are verified on the platform."""
