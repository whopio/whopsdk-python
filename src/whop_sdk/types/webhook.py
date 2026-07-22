# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Webhook"]


class Webhook(BaseModel):
    id: str
    """Webhook ID, prefixed `hook_`."""

    api_version: Literal["v1", "v2", "v5"]
    """The API version used to format payloads sent to this webhook endpoint."""

    child_resource_events: bool
    """Whether events are sent for child resources.

    For example, if the webhook is on a company, enabling this sends events only
    from the company's sub-merchants (child companies).
    """

    created_at: str
    """When the webhook was created, as an ISO 8601 timestamp."""

    enabled: bool
    """Whether this webhook endpoint is currently active and receiving events."""

    events: List[str]

    resource_id: str
    """ID of the resource (company or app) this webhook is attached to."""

    testable_events: List[str]

    url: str
    """Destination URL where webhook payloads are delivered via HTTP POST."""

    webhook_secret: Optional[str] = None
    """Secret key used to sign webhook payloads for verification.

    Include this in your HMAC validation logic. Returned on the create response and
    to interactive dashboard sessions; `null` for API-key and OAuth callers on later
    reads.
    """
