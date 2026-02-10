# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .app_type import AppType
from .shared.direction import Direction
from .shared.app_view_type import AppViewType

__all__ = ["AppListParams"]


class AppListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    app_type: Optional[AppType]
    """The type of end-user an app is built for"""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    company_id: Optional[str]
    """Filter apps to only those created by this company, starting with 'biz\\__'."""

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    order: Optional[
        Literal[
            "created_at",
            "discoverable_at",
            "total_installs_last_30_days",
            "total_installs_last_7_days",
            "time_spent",
            "time_spent_last_24_hours",
            "daily_active_users",
            "ai_prompt_count",
            "total_ai_cost_usd",
            "total_ai_tokens",
            "last_ai_prompt_at",
            "ai_average_rating",
        ]
    ]
    """The order to fetch the apps in for discovery."""

    query: Optional[str]
    """A search string to filter apps by name, such as 'chat' or 'analytics'."""

    verified_apps_only: Optional[bool]
    """Whether to only return apps that have been verified by Whop.

    Useful for populating a featured apps section.
    """

    view_type: Optional[AppViewType]
    """The different types of an app view"""
