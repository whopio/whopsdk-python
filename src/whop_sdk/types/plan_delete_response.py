# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PlanDeleteResponse"]


class PlanDeleteResponse(BaseModel):
    id: str
    """ID of the deleted plan."""

    deleted: bool
    """Always true."""
