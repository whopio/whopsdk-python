# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.page_info import PageInfo
from .shared.access_pass_list_item import AccessPassListItem

__all__ = ["AccessPassListResponse"]


class AccessPassListResponse(BaseModel):
    data: Optional[List[Optional[AccessPassListItem]]] = None
    """A list of nodes."""

    page_info: PageInfo
    """Information to aid in pagination."""
