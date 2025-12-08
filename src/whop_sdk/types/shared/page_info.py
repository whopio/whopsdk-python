# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PageInfo"]


class PageInfo(BaseModel):
    """Information about pagination in a connection."""

    end_cursor: Optional[str] = None
    """When paginating forwards, the cursor to continue."""

    has_next_page: bool
    """When paginating forwards, are there more items?"""

    has_previous_page: bool
    """When paginating backwards, are there more items?"""

    start_cursor: Optional[str] = None
    """When paginating backwards, the cursor to continue."""
