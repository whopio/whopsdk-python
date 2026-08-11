# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ReachEstimate"]


class ReachEstimate(BaseModel):
    users_lower_bound: Optional[float] = None
    """Low end of how many people the targeting can reach.

    Null when the platform couldn't produce an estimate.
    """

    users_upper_bound: Optional[float] = None
    """High end of how many people the targeting can reach.

    Null when the platform couldn't produce an estimate.
    """
