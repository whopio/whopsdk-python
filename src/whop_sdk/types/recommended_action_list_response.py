# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RecommendedActionListResponse", "Data", "DataAction"]


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

    error: Optional[str] = None
    """Why the step failed, or `null`"""

    input: Optional[object] = None
    """
    The filled-in request body for the step's endpoint, or `null` when it was not
    recorded
    """

    output: Optional[object] = None
    """The API response the step produced, or `null` until it succeeds"""

    position: int
    """Zero-based order of this step within the chain"""

    reasoning: Optional[object] = None
    """Why the generator filled the step this way, or `null` for seeded chains"""

    status: Optional[Literal["pending", "redirected", "running", "succeeded", "failed"]] = None
    """Where the run step currently stands, or `null` when the chain has not been run"""

    title: str
    """Headline for the step"""


class Data(BaseModel):
    id: str
    """
    Chain ID — `rac_seed_<preset>_<nonce>` for seeded chains, `rac_chain_*` for
    generated ones
    """

    actions: List[DataAction]

    description: str
    """What running the chain accomplishes"""

    reasoning: Optional[object] = None
    """Why the generator proposed this chain, or `null` for seeded chains"""

    title: str
    """Headline for the chain"""


class RecommendedActionListResponse(BaseModel):
    data: List[Data]
