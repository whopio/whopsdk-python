# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DmChannelUpdateParams"]


class DmChannelUpdateParams(TypedDict, total=False):
    custom_name: Optional[str]
    """The custom name for the DM channel"""
