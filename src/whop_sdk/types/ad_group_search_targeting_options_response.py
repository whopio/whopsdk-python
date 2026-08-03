# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .targeting_option import TargetingOption

__all__ = ["AdGroupSearchTargetingOptionsResponse"]


class AdGroupSearchTargetingOptionsResponse(BaseModel):
    data: List[TargetingOption]
