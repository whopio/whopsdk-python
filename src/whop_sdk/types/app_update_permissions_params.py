# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["AppUpdatePermissionsParams", "RequestedPermission"]


class AppUpdatePermissionsParams(TypedDict, total=False):
    requested_permissions: Required[Iterable[RequestedPermission]]
    """
    The full set of permissions the app requests on install; permissions not listed
    are removed.
    """


class RequestedPermission(TypedDict, total=False):
    action: Required[str]
    """The permission action, for example `company:basic:read`."""

    is_required: Required[bool]
    """Whether installing the app requires granting this permission."""

    justification: Required[str]
    """
    Why the app needs this permission (20-512 characters), shown to the installing
    user.
    """
