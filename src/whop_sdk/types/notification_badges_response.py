# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .notification_badge import NotificationBadge

__all__ = ["NotificationBadgesResponse"]


class NotificationBadgesResponse(BaseModel):
    data: List[NotificationBadge]
