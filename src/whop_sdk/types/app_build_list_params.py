# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.app_build_statuses import AppBuildStatuses
from .shared.app_build_platforms import AppBuildPlatforms

__all__ = ["AppBuildListParams"]


class AppBuildListParams(TypedDict, total=False):
    app_id: Required[str]
    """The unique identifier of the app to list builds for."""

    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return builds created after this timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return builds created before this timestamp."""

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""

    platform: AppBuildPlatforms
    """Filter builds by target platform."""

    status: AppBuildStatuses
    """Filter builds by review status."""
