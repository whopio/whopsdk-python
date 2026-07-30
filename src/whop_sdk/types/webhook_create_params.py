# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .api_version import APIVersion
from .webhook_event import WebhookEvent

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    url: Required[str]
    """The URL to send the webhook to."""

    api_version: Optional[APIVersion]
    """The different API versions"""

    api_version_date: Optional[str]
    """
    The dated API version (Api-Version-Date) the webhook's payloads are pinned to:
    events serialize exactly like a REST read at this version (the native serializer
    where the resource has one). Only applies to v1 webhooks. Omit to leave the
    webhook unpinned on the legacy payload shape.
    """

    child_resource_events: Optional[bool]
    """Whether or not to send events for child resources.

    For example, if the webhook is created for a Company, enabling this will only
    send events from the Company's sub-merchants (child companies).
    """

    enabled: Optional[bool]
    """Whether or not the webhook is enabled."""

    events: Optional[List[WebhookEvent]]
    """The events to send the webhook for."""

    resource_id: Optional[str]
    """The resource to create the webhook for.

    By default this will use current company
    """
