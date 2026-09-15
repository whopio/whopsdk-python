# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DisputeListParams"]


class DisputeListParams(TypedDict, total=False):
    account_id: str
    """Only disputes filed against this account (`biz_` tag).

    Omit it to cover every account you can read.
    """

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
    """Only disputes opened after this ISO 8601 timestamp."""

    created_before: str
    """Only disputes opened before this ISO 8601 timestamp."""

    currency: str
    """Only disputes in this three-letter ISO currency."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """Number of results to return from the start of the range."""

    last: int
    """Number of results to return from the end of the range."""

    order: Literal["created_at", "amount", "evidence_due_at"]
    """The field to sort disputes by."""

    status: List[Literal["needs_response", "under_review", "won", "lost", "closed"]]
    """Only disputes in these statuses.

    Repeat the parameter to pass several — one paginated list covers all of them.
    Covers both chargebacks and inquiries at each stage. A `needs_response` dispute
    whose evidence deadline has passed reports and filters as `under_review`
    instead.
    """

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
