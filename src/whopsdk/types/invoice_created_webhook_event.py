# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.invoice import Invoice

__all__ = ["InvoiceCreatedWebhookEvent"]


class InvoiceCreatedWebhookEvent(BaseModel):
    id: Optional[str] = None
    """A unique ID for every single webhook request"""

    api_version: Optional[Literal["v1"]] = None
    """The API version for this webhook"""

    created_at: Optional[str] = None
    """
    The timestamp in seconds since the Unix epoch that the webhook was sent at on
    the server
    """

    data: Optional[Invoice] = None
    """A statement that defines an amount due by a customer."""

    type: Optional[Literal["invoice.created"]] = None
    """The webhook event type"""
