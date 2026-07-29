# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WebhookTestResponse"]


class WebhookTestResponse(BaseModel):
    body: object
    """The body of the webhook response."""

    status: int
    """The HTTP response code of this request."""

    success: bool
    """Whether or not the webhook test was successful."""
