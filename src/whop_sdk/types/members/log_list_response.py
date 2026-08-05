# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["LogListResponse", "Actor"]


class Actor(BaseModel):
    id: str

    name: Optional[str] = None

    username: Optional[str] = None


class LogListResponse(BaseModel):
    action: Optional[str] = None

    actor: Optional[Actor] = None

    created_at: datetime
