# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RecommendedActionListExecutionsResponse", "Execution"]


class Execution(BaseModel):
    id: str
    """Execution ID, prefixed `raex_`"""

    action: str
    """The action definition key the step ran"""

    completed_at: Optional[str] = None
    """When the step reached a terminal status, ISO 8601"""

    error: Optional[str] = None
    """Why the step failed, or `null`"""

    output: Optional[object] = None
    """The API response the step produced, or `null` until it succeeds"""

    position: int
    """Zero-based order of the step within the chain"""

    status: Literal["pending", "redirected", "running", "succeeded", "failed"]
    """Where the step currently stands"""


class RecommendedActionListExecutionsResponse(BaseModel):
    chain_id: str
    """The chain these executions belong to."""

    executions: List[Execution]
    """One entry per run step, in position order."""
