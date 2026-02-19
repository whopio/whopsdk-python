# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .api_version import APIVersion
from .webhook_event import WebhookEvent

__all__ = ["Webhook"]


class Webhook(BaseModel):
    """
    A webhook endpoint that receives event notifications for a company via HTTP POST.
    """

    id: str
    """The unique identifier for the webhook."""

    api_version: APIVersion
    """The API version used to format payloads sent to this webhook endpoint."""

    child_resource_events: bool
    """Whether events are sent for child resources.

    For example, if the webhook is on a company, enabling this sends events only
    from the company's sub-merchants (child companies).
    """

    created_at: datetime
    """The datetime the webhook was created."""

    enabled: bool
    """Whether this webhook endpoint is currently active and receiving events."""

    events: List[WebhookEvent]
    """The list of event types this webhook is subscribed to."""

    resource_id: str
    """The ID of the resource (company or product) this webhook is attached to."""

    testable_events: List[WebhookEvent]
    """The subset of subscribed event types that support sending test payloads."""

    url: str
    """The destination URL where webhook payloads are delivered via HTTP POST."""
