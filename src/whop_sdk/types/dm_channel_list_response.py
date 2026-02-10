# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["DmChannelListResponse"]


class DmChannelListResponse(BaseModel):
    """
    A messaging channel that can be a one-on-one DM, group chat, company support conversation, or platform-level direct message.
    """

    id: str
    """The unique identifier for the entity"""

    created_at: str
    """The time the entity was created (in milliseconds since Unix epoch)"""

    last_message_at: Optional[datetime] = None
    """The timestamp when the most recent message was sent in this channel.

    Null if no messages have been sent.
    """

    name: Optional[str] = None
    """A custom display name assigned to this channel by the user.

    Null if no custom name has been set.
    """
