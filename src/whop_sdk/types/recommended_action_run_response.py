# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RecommendedActionRunResponse"]


class RecommendedActionRunResponse(BaseModel):
    chain_id: str

    execution: Literal["redirect", "executed"]
