# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.app_build_statuses import AppBuildStatuses
from .shared.app_build_platforms import AppBuildPlatforms

__all__ = ["AppBuildListParams"]


class AppBuildListParams(TypedDict, total=False):
    app_id: Required[str]
    """The ID of the app to filter app builds by"""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The minimum creation date to filter by"""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The maximum creation date to filter by"""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    platform: Optional[AppBuildPlatforms]
    """The different platforms an app build can target."""

    status: Optional[AppBuildStatuses]
    """The different statuses an AppBuild can be in."""
