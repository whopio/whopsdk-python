# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WebhookListDeliveriesResponse"]


class WebhookListDeliveriesResponse(BaseModel):
    id: str
    """Unique identifier for this delivery attempt.

    Pass it to the replay endpoint to re-send this exact payload.
    """

    event: Optional[str] = None
    """The event type this delivery carried, for example `payment.succeeded`."""

    replayed_from: Optional[str] = None
    """The id of the delivery attempt this one replayed.

    `null` for an original delivery.
    """

    request_body: object
    """Request body sent to the webhook endpoint."""

    resource_id: str
    """ID of the resource that triggered the webhook."""

    response_body: object
    """Response body received from the webhook endpoint."""

    response_code: float
    """HTTP response code received from the webhook endpoint."""

    sent_at: str
    """When the webhook was sent, as an ISO 8601 timestamp."""

    success: bool
    """Whether the endpoint acknowledged this attempt with a 2xx response."""

    total_time: float
    """Total time taken to send the webhook request, in seconds."""
