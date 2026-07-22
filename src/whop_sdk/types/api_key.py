# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    id: str
    """API key ID, prefixed `apik_`."""

    created_at: str
    """When the API key was created, as an ISO 8601 timestamp."""

    expires_at: Optional[str] = None
    """When the API key stops working, as an ISO 8601 timestamp.

    `null` means it never expires.
    """

    ip_allowlist: Optional[List[str]] = None

    is_default_for_resource: bool
    """Whether this is the resource's default API key.

    Default keys cannot be updated or deleted, only rotated.
    """

    name: Optional[str] = None
    """Human-readable name identifying the API key, or `null` when none was set."""

    obfuscated_secret_key: str
    """
    Masked version of the secret key, so the key can be recognized without revealing
    the full secret.
    """

    system_role: Optional[Literal["owner", "admin", "moderator", "sales_manager", "advertiser"]] = None
    """
    System role the key inherits its permissions from, or `null` when it uses an
    explicit permissions policy. Only account API keys can use a system role.
    """

    updated_at: str
    """When the API key was last updated, as an ISO 8601 timestamp."""

    grants: Optional[List[object]] = None

    secret_key: Optional[str] = None
    """The full secret used to authenticate requests.

    Returned only once, on create and rotate responses — store it immediately.
    """
