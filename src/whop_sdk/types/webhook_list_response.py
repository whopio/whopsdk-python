# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .api_version import APIVersion
from .webhook_event import WebhookEvent

__all__ = ["WebhookListResponse"]


class WebhookListResponse(BaseModel):
    """
    A webhook endpoint that receives event notifications for a company via HTTP POST.
    """

    id: str
    """The unique identifier for the webhook."""

    api_version: APIVersion
    """The API version used to format payloads sent to this webhook endpoint."""

    api_version_date: Optional[str] = None
    """
    The dated API version (Api-Version-Date) that v1 payloads for this endpoint are
    pinned to: events serialize exactly like a REST read at this version (the native
    serializer where the resource has one). Null when unpinned — legacy (v2/v5)
    webhooks, and v1 webhooks on the legacy payload shape.
    """

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

    url: str
    """The destination URL where webhook payloads are delivered via HTTP POST."""

    webhook_secret: str
    """The secret key used to sign webhook payloads for verification.

    Include this in your HMAC validation logic. Returned on the create response and
    to interactive dashboard sessions; empty for API-key and OAuth callers on later
    reads.
    """
