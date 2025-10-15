# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .shared.invoice import Invoice

__all__ = ["InvoicePastDueWebhookEvent"]


class InvoicePastDueWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    created_at: str
    """
    The timestamp in seconds since the Unix epoch that the webhook was sent at on
    the server
    """

    data: Invoice
    """A statement that defines an amount due by a customer."""

    type: Literal["invoice.past_due"]
    """The webhook event type"""
