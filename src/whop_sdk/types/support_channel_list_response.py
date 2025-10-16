# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SupportChannelListResponse", "CustomerUser"]


class CustomerUser(BaseModel):
    id: str
    """The internal ID of the user."""

    name: Optional[str] = None
    """The name of the user from their Whop account."""

    username: str
    """The username of the user from their Whop account."""


class SupportChannelListResponse(BaseModel):
    id: str
    """The unique identifier for the entity"""

    company_id: Optional[str] = None
    """The bot ID if this is a support chat"""

    custom_name: Optional[str] = None
    """The custom name of the DM channel, if any"""

    customer_user: Optional[CustomerUser] = None
    """The customer user if this is a support chat"""

    last_message_at: Optional[datetime] = None
    """When the last message was sent"""

    resolved_at: Optional[datetime] = None
    """When the support ticket was resolved (null if unresolved)"""
