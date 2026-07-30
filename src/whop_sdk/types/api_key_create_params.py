# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["APIKeyCreateParams", "Permissions", "PermissionsStatement"]


class APIKeyCreateParams(TypedDict, total=False):
    name: Required[str]
    """A human-readable name for the API key, such as 'Production API Key'."""

    permissions: Required[Permissions]
    """
    The permissions policy for the API key: explicit permission statements, or a
    system role to inherit from. Statements without a `resources` array default to
    the owning account (Account API keys) or every key-addressable resource (App API
    keys).
    """

    resource_id: Required[str]
    """The account (`biz_`) or app (`app_`) tag to create the API key for."""

    resource_type: Required[Literal["account", "app"]]
    """The type of resource that will own this API key."""

    expires_at: Optional[str]
    """When the API key should stop working, as an ISO 8601 timestamp.

    Omit (or pass `null` on update) for a key that never expires.
    """

    ip_allowlist: Optional[SequenceNotStr[str]]
    """IPv4/IPv6 CIDR ranges allowed to use this key, for example `["203.0.113.0/24"]`.

    Empty or `null` allows any IP.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class PermissionsStatement(TypedDict, total=False):
    actions: Required[SequenceNotStr[str]]
    """Permission actions covered by this statement, for example `company:basic:read`."""

    grant: Required[bool]
    """Whether the actions are granted (`true`) or denied (`false`)."""

    resources: SequenceNotStr[str]
    """
    Resource identifiers the statement applies to, for example `biz_xxx` or
    `biz_xxx|pass_*`. Defaults to the key's owning resource when omitted.
    """


class Permissions(TypedDict, total=False):
    """
    The permissions policy for the API key: explicit permission statements, or a system role to inherit from. Statements without a `resources` array default to the owning account (Account API keys) or every key-addressable resource (App API keys).
    """

    statements: Iterable[PermissionsStatement]
    """Explicit permission statements. Required unless `system_role` is set."""

    system_role: Optional[Literal["owner", "admin", "moderator", "sales_manager", "advertiser"]]
    """A system role to inherit permissions from.

    Only Account API keys can use a system role.
    """
