# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ProductDeleteResponse"]


class ProductDeleteResponse(BaseModel):
    id: str
    """ID of the deleted product."""

    deleted: bool
    """Always true."""
