# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["DmChannel"]


class DmChannel(BaseModel):
    """Represents a DM channel"""

    id: str
    """The unique identifier for the entity"""

    created_at: str
    """The time the entity was created (in milliseconds since Unix epoch)"""

    last_message_at: Optional[datetime] = None
    """When the last message was sent"""

    name: Optional[str] = None
    """The custom name of the DM channel, if any"""
