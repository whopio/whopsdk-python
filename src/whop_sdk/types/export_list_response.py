# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .export import Export
from .._models import BaseModel

__all__ = ["ExportListResponse", "PageInfo"]


class PageInfo(BaseModel):
    end_cursor: Optional[str] = None

    has_next_page: bool

    has_previous_page: bool

    start_cursor: Optional[str] = None


class ExportListResponse(BaseModel):
    data: List[Export]

    page_info: PageInfo
