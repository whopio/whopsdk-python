# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Permission"]


class Permission(BaseModel):
    action: str
    """The permission action's identifier, for example `company:basic:read`."""

    allowed_on_api_key: bool
    """Whether an API key can be granted the permission."""

    allowed_on_app: bool
    """Whether an app can request and be granted the permission."""

    allowed_on_user: bool
    """Whether the permission can be granted to user tokens."""

    category: Optional[str] = None
    """The category the action is grouped under, or `null` when uncategorized."""

    description: str
    """What granting the action allows."""

    granted_to_system_roles: List[Literal["owner", "admin", "moderator", "sales_manager", "advertiser"]]

    name: str
    """Human-readable name of the action."""
