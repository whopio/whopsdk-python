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
    """The JSON event payload sent to the webhook endpoint."""

    resource_id: str
    """ID of the resource that triggered the webhook."""

    response_body: Optional[object] = None
    """The endpoint's JSON response.

    A non-JSON response is stored as `{ error, raw_body }` with the first 100 bytes.
    """

    response_code: float
    """HTTP response code received from the webhook endpoint."""

    sent_at: str
    """When the webhook was sent, as an ISO 8601 timestamp."""

    success: bool
    """Whether the endpoint acknowledged this attempt with a 2xx response."""

    total_time: float
    """Total time taken to send the webhook request, in seconds."""
