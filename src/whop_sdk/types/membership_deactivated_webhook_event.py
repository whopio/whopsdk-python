# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.membership import Membership

__all__ = ["MembershipDeactivatedWebhookEvent"]


class MembershipDeactivatedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    data: Membership
    """
    A membership represents a purchase between a User and a Company for a specific
    Product.
    """

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["membership.deactivated"]
    """The webhook event type"""
