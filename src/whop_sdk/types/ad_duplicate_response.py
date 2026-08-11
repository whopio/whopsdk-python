# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .ad import Ad
from .._models import BaseModel

__all__ = ["AdDuplicateResponse"]


class AdDuplicateResponse(BaseModel):
    data: List[Ad]
