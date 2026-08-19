# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AdDeleteResponse"]


class AdDeleteResponse(BaseModel):
    id: str
    """ID of the deleted ad."""

    deleted: bool
    """Always true."""
