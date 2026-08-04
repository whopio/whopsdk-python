# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MethodDeleteResponse"]


class MethodDeleteResponse(BaseModel):
    id: str
    """ID of the deleted payout method, prefixed `potk_`."""

    deleted: bool
    """Always `true`."""
