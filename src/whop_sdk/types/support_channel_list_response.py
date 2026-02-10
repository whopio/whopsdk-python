# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SupportChannelListResponse", "CustomerUser"]


class CustomerUser(BaseModel):
    """The customer who initiated this support conversation.

    Null if this is not a support chat.
    """

    id: str
    """The unique identifier for the user."""

    name: Optional[str] = None
    """The user's display name shown on their public profile."""

    username: str
    """The user's unique username shown on their public profile."""


class SupportChannelListResponse(BaseModel):
    """
    A messaging channel that can be a one-on-one DM, group chat, company support conversation, or platform-level direct message.
    """

    id: str
    """The unique identifier for the entity"""

    company_id: Optional[str] = None
    """The unique identifier of the company associated with this channel.

    Null if this is not a support or company-scoped conversation.
    """

    custom_name: Optional[str] = None
    """A custom display name assigned to this channel by the user.

    Null if no custom name has been set.
    """

    customer_user: Optional[CustomerUser] = None
    """The customer who initiated this support conversation.

    Null if this is not a support chat.
    """

    last_message_at: Optional[datetime] = None
    """The timestamp when the most recent message was sent in this channel.

    Null if no messages have been sent.
    """

    resolved_at: Optional[datetime] = None
    """The timestamp when the linked support ticket was marked as resolved.

    Null if unresolved or not a support chat.
    """
