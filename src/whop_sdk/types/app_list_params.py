# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AppListParams"]


class AppListParams(TypedDict, total=False):
    account_id: str
    """Only return apps created by this account (`biz_` tag).

    With developer access to the account this includes its unlisted and hidden apps.
    """

    after: str
    """A cursor; returns apps after this position."""

    app_type: Literal["b2b_app", "b2c_app", "company_app", "component", "website"]
    """Filter apps by the type of end-user they are built for."""

    before: str
    """A cursor; returns apps before this position."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """The number of apps to return (default 20, max 100)."""

    last: int
    """The number of apps to return from the end of the range."""

    order: Literal["created_at", "discoverable_at", "total_installs_last_30_days", "total_installs_last_7_days"]
    """The field to sort apps by.

    Defaults to discoverable_at, showing the most recently published apps first.
    """

    query: str
    """A search string matched against app names."""

    verified_apps_only: bool
    """Whether to only return apps verified by Whop."""

    view_type: Literal["hub", "discover", "dash", "dashboard", "analytics", "skills", "openapi"]
    """Only return apps supporting this view type, such as `dashboard` or `hub`."""
