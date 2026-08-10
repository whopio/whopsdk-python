# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WebhookListDeliveriesResponse"]


class WebhookListDeliveriesResponse(BaseModel):
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

    total_time: float
    """Total time taken to send the webhook request, in seconds."""
