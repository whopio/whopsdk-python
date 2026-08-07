# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .ad_campaign import AdCampaign

__all__ = ["AdCampaignDuplicateResponse"]


class AdCampaignDuplicateResponse(BaseModel):
    data: List[AdCampaign]
