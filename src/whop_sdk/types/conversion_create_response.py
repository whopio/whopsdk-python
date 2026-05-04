# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ConversionCreateResponse"]


class ConversionCreateResponse(BaseModel):
    """A tracked conversion event"""

    id: str
    """The unique identifier for the conversion"""
