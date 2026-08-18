# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .app_type import AppType
from .shared.direction import Direction
from .shared.app_view_type import AppViewType

__all__ = ["AppListParams"]


class AppListParams(TypedDict, total=False):
    after: str
    """Returns the elements in the list that come after the specified cursor."""

    app_type: AppType
    """
    Filter apps by the type of end-user they are built for, such as consumer or
    business.
    """

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    company_id: str
    """Filter apps to only those created by this company, starting with 'biz\\__'."""

    direction: Direction
    """The sort direction for results. Accepted values: asc, desc."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    order: Literal[
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
    """The field to sort apps by.

    Defaults to discoverable_at descending, showing the most recently published apps
    first.
    """

    query: str
    """A search string to filter apps by name, such as 'chat' or 'analytics'."""

    verified_apps_only: bool
    """Whether to only return apps that have been verified by Whop.

    Useful for populating a featured apps section.
    """

    view_type: AppViewType
    """
    Filter apps to only those supporting a specific view type, such as 'dashboard'
    or 'hub'.
    """
