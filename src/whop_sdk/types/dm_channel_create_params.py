# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DmChannelCreateParams"]


class DmChannelCreateParams(TypedDict, total=False):
    with_user_ids: Required[SequenceNotStr[str]]
    """The user ids to create a DM with. Can be email, username or user_id (tag)"""

    company_id: Optional[str]
    """The ID of the company to scope this DM channel to."""

    custom_name: Optional[str]
    """The custom name for the DM channel"""
