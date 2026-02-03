# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .api_version import APIVersion
from .webhook_event import WebhookEvent

__all__ = ["Webhook"]


class Webhook(BaseModel):
    """A webhook object, which can be configured to be sent updates about a company"""

    id: str
    """The ID of the webhook"""

    api_version: APIVersion
    """The API version for this webhook"""

    child_resource_events: bool
    """Whether or not to send events for child resources.

    For example, if the webhook is created for a Company, enabling this will only
    send events from the Company's sub-merchants (child companies).
    """

    created_at: datetime
    """The timestamp of when the webhook was created"""

    enabled: bool
    """Whether or not this webhook is turned on or not"""

    events: List[WebhookEvent]
    """The number of events this webhooks is configured to receive"""

    resource_id: str
    """The resource ID"""

    testable_events: List[WebhookEvent]
    """The list of events that can be tested with this webhook"""

    url: str
    """The URL the webhook events will be sent to"""
