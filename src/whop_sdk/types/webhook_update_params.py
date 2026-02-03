# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from .api_version import APIVersion
from .webhook_event import WebhookEvent

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    api_version: Optional[APIVersion]
    """The different API versions"""

    child_resource_events: Optional[bool]
    """Whether or not to send events for child resources."""

    enabled: Optional[bool]
    """Whether or not the webhook is enabled."""

    events: Optional[List[WebhookEvent]]
    """The events to send the webhook for."""

    url: Optional[str]
    """The URL to send the webhook to."""
