# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountRecommendActionsResponse", "Data", "DataAction"]


class DataAction(BaseModel):
    """The chain's steps in run order"""

    action: str
    """
    The action definition key this step runs; new values may be added, so handle
    unknown actions gracefully
    """

    cta: str
    """The URL where this step is done by hand"""

    cta_label: str
    """Button label"""

    description: str
    """Supporting copy, or empty"""

    position: int
    """Zero-based order of this step within the chain"""

    title: str
    """Headline for the step"""


class Data(BaseModel):
    id: Literal["launch_ads", "start_selling", "revive_stalled_ads", "cut_and_reallocate", "promote_with_affiliates"]
    """The chain; new values may be added, so handle unknown chains gracefully"""

    actions: List[DataAction]

    description: str
    """What running the chain accomplishes"""

    title: str
    """Headline for the chain"""


class AccountRecommendActionsResponse(BaseModel):
    data: List[Data]
