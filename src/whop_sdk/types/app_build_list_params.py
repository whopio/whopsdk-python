# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AppBuildListParams"]


class AppBuildListParams(TypedDict, total=False):
    app_id: Required[str]
    """The app to list builds for, prefixed `app_`."""

    after: str
    """Return results after this cursor.

    Use `page_info.end_cursor` from the previous response to fetch the next page.
    """

    before: str
    """Return results before this cursor.

    Use `page_info.start_cursor` from the previous response to fetch the previous
    page.
    """

    created_after: Union[int, str]
    """Only return builds created after this ISO 8601 timestamp."""

    created_before: Union[int, str]
    """Only return builds created before this ISO 8601 timestamp."""

    first: int
    """Number of results to return from the start of the range."""

    last: int
    """Number of results to return from the end of the range."""

    platform: Literal["ios", "android", "web"]
    """Filter builds by target platform."""

    status: Literal["draft", "pending", "approved", "rejected"]
    """Filter builds by review status."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
