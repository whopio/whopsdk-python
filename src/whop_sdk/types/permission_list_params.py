# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PermissionListParams"]


class PermissionListParams(TypedDict, total=False):
    resource_id: Required[str]
    """
    Tag of the resource to check against: an account (`biz_`), product (`prod_`),
    experience (`exp_`), or app (`app_`). A resource the credential cannot see is
    reported as granted nothing rather than as an error.
    """

    actions: str
    """
    Comma-separated permission actions to check, for example
    `stats:read,payment:basic:read`. Every action is returned when omitted.
    """
