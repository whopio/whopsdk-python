# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WebhookReplayDeliveryResponse"]


class WebhookReplayDeliveryResponse(BaseModel):
    body: str
    """The body your endpoint returned for the replayed request, as raw text.

    Empty when the endpoint could not be reached.
    """

    status: int
    """
    The HTTP response code your endpoint returned for the replayed request, or 0
    when it could not be reached (timeout, DNS, or connection failure).
    """

    success: bool
    """Whether your endpoint acknowledged the replay with a 2xx response."""
