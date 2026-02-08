# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.membership import Membership

__all__ = ["MembershipCancelAtPeriodEndChangedWebhookEvent"]


class MembershipCancelAtPeriodEndChangedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    data: Membership
    """A membership represents an active relationship between a user and a product.

    It tracks the user's access, billing status, and renewal schedule.
    """

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["membership.cancel_at_period_end_changed"]
    """The webhook event type"""

    company_id: Optional[str] = None
    """The company ID that this webhook event is associated with"""
