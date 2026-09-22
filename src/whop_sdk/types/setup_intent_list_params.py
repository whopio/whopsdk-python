# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SetupIntentListParams"]


class SetupIntentListParams(TypedDict, total=False):
    account_id: str
    """Only setup intents for this account, prefixed `biz_`."""

    after: str
    """Return results after this cursor.

    Use `page_info.end_cursor` from the previous response to fetch the next page.
    """

    before: str
    """Return results before this cursor.

    Use `page_info.start_cursor` from the previous response to fetch the previous
    page.
    """

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only setup intents created after this ISO 8601 timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only setup intents created before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """The sort direction."""

    first: int
    """Number of results to return from the start of the range."""

    last: int
    """Number of results to return from the end of the range."""

    order: Literal["created_at"]
    """The field to sort by."""

    status: Literal["processing", "succeeded", "canceled", "requires_action"]
    """Only setup intents in this state."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
