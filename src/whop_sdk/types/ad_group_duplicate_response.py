# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .ad_group import AdGroup

__all__ = ["AdGroupDuplicateResponse"]


class AdGroupDuplicateResponse(BaseModel):
    data: List[AdGroup]
