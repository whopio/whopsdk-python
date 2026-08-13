# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["APIKey", "Grant", "GrantAction"]


class GrantAction(BaseModel):
    """The actions the grant covers on the resource, each marked granted or not."""

    action: str
    """The permission action's identifier, for example `company:basic:read`."""

    granted: bool
    """Whether the key holds the action on the grant's resource."""


class Grant(BaseModel):
    """The key's effective permissions, grouped by resource.

    Present on retrieve, create, update, and rotate responses; omitted on list.
    """

    actions: List[GrantAction]

    resource_id: str
    """ID of the resource the actions apply to."""

    resource_type: str
    """
    The type of resource the actions apply to, such as `account`, `product`, or
    `app`.
    """


class APIKey(BaseModel):
    id: str
    """API key ID, prefixed `apik_`."""

    api_version_date: Literal[
        "2025-01-01",
        "2026-06-08",
        "2026-06-09",
        "2026-06-20",
        "2026-07-01",
        "2026-07-08",
        "2026-07-08-1",
        "2026-07-18",
        "2026-07-20",
        "2026-07-22",
        "2026-07-23",
        "2026-07-25",
        "2026-07-26",
        "2026-07-27",
        "2026-07-29",
        "2026-07-29-1",
        "2026-07-31",
        "2026-08-03",
        "2026-08-05",
        "2026-08-05-1",
        "2026-08-10",
        "2026-08-12",
    ]
    """
    Dated API version used when requests authenticated with this key omit the
    `Api-Version-Date` header.
    """

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

    grants: Optional[List[Grant]] = None

    secret_key: Optional[str] = None
    """The full secret used to authenticate requests.

    Returned only once, on create and rotate responses — store it immediately.
    """
