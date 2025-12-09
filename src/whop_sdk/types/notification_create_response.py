# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["NotificationCreateResponse"]


class NotificationCreateResponse(BaseModel):
    """Response from queuing a notification"""

    success: bool
    """Whether the notification was successfully queued for delivery"""
