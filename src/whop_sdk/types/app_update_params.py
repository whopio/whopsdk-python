# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .app_type import AppType
from .shared.app_statuses import AppStatuses

__all__ = ["AppUpdateParams", "Icon"]


class AppUpdateParams(TypedDict, total=False):
    app_store_description: Optional[str]
    """The detailed description shown on the app store's in-depth app view page."""

    app_type: Optional[AppType]
    """The type of end-user an app is built for"""

    base_url: Optional[str]
    """
    The base production URL where the app is hosted, such as
    'https://myapp.example.com'.
    """

    dashboard_path: Optional[str]
    """The URL path for the company dashboard view of the app, such as '/dashboard'."""

    description: Optional[str]
    """A short description of the app shown in listings and search results."""

    discover_path: Optional[str]
    """The URL path for the discover view of the app, such as '/discover'."""

    experience_path: Optional[str]
    """
    The URL path for the member-facing hub view of the app, such as
    '/experiences/[experienceId]'.
    """

    icon: Optional[Icon]
    """The icon image for the app, used in listings and navigation."""

    name: Optional[str]
    """
    The display name for the app, shown to users on the app store and product pages.
    """

    required_scopes: Optional[List[Literal["read_user"]]]
    """The permission scopes the app will request from users when they install it."""

    status: Optional[AppStatuses]
    """The status of an experience interface"""


class Icon(TypedDict, total=False):
    """The icon image for the app, used in listings and navigation."""

    id: Required[str]
    """The ID of an existing file object."""
