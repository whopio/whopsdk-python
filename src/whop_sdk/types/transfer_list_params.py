# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransferListParams"]


class TransferListParams(TypedDict, total=False):
    after: str
    """Return results after this cursor.

    Use `page_info.end_cursor` from the previous response to fetch the next page.
    """

    before: str
    """Return results before this cursor.

    Use `page_info.start_cursor` from the previous response to fetch the previous
    page.
    """

    created_after: str
    """Only transfers created strictly after this ISO 8601 timestamp."""

    created_before: str
    """Only transfers created strictly before this ISO 8601 timestamp."""

    destination_id: str
    """Filter to transfers received by this account. Provide this or origin_id."""

    direction: Literal["asc", "desc"]
    """Sort direction. Defaults to desc."""

    first: int
    """Number of results to return from the start of the range."""

    last: int
    """Number of results to return from the end of the range."""

    order: Literal["created_at", "amount"]
    """Sort column. Defaults to created_at."""

    origin_id: str
    """Filter to transfers sent from this account. Provide this or destination_id."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
