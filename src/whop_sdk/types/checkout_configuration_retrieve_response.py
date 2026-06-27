# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CheckoutConfigurationRetrieveResponse"]


class CheckoutConfigurationRetrieveResponse(BaseModel):
    id: str
    """The unique identifier of the checkout configuration."""

    company_id: str
    """The ID of the company that owns this checkout configuration."""

    created_at: int
    """Unix timestamp when the checkout configuration was created."""

    mode: Literal["payment", "setup"]
    """The checkout mode."""

    updated_at: int
    """Unix timestamp when the checkout configuration was last updated."""

    affiliate_code: Optional[str] = None
    """The affiliate code applied at checkout."""

    currency: Optional[str] = None
    """The currency for this checkout configuration."""

    metadata: Optional[object] = None
    """Arbitrary key-value metadata.

    Only returned when caller has checkout_configuration:basic:read scope.
    """

    payment_method_configuration: Optional[object] = None
    """Payment method configuration."""

    plan: Optional[object] = None
    """The plan associated with this checkout configuration."""

    purchase_url: Optional[str] = None
    """The URL for the checkout page."""

    redirect_url: Optional[str] = None
    """The URL to redirect after checkout."""

    three_ds_level: Optional[str] = None
    """The 3D Secure enforcement level."""
