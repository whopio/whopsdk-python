# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    account_id: str
    """The account whose profile override to update. Required for API key callers."""

    bio: str

    name: str
