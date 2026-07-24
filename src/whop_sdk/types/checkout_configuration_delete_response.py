# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CheckoutConfigurationDeleteResponse"]


class CheckoutConfigurationDeleteResponse(BaseModel):
    id: str
    """ID of the deleted checkout configuration."""

    deleted: bool
    """Always true."""
