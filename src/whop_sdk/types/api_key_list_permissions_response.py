# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .permission import Permission

__all__ = ["APIKeyListPermissionsResponse", "PageInfo"]


class PageInfo(BaseModel):
    end_cursor: Optional[str] = None

    has_next_page: bool

    has_previous_page: bool

    start_cursor: Optional[str] = None


class APIKeyListPermissionsResponse(BaseModel):
    data: List[Permission]

    page_info: PageInfo
