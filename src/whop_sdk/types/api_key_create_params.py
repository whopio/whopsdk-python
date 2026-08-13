# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

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
    `Api-Version-Date` header. New keys default to the latest version.
    """

    expires_at: Optional[str]
    """When the API key should stop working, as an ISO 8601 timestamp.

    Omit (or pass `null` on update) for a key that never expires.
    """

    ip_allowlist: Optional[SequenceNotStr[str]]
    """IPv4/IPv6 CIDR ranges allowed to use this key, for example `["203.0.113.0/24"]`.

    Empty or `null` allows any IP.
    """


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
