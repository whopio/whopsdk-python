# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AdGroupDeleteResponse"]


class AdGroupDeleteResponse(BaseModel):
    id: str
    """ID of the deleted ad group."""

    deleted: bool
    """Always true."""
