# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .ad_group import AdGroup

__all__ = ["AdGroupListResponse"]


class AdGroupListResponse(BaseModel):
    data: Optional[List[AdGroup]] = None

    page_info: Optional[object] = None
