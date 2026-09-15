# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MembershipListParams"]


class MembershipListParams(TypedDict, total=False):
    account_id: str
    """Narrow to one account (`biz_` tag).

    With read access to the account this lists all of its memberships; without, only
    the caller's own memberships in it.
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
    """Only memberships created after this ISO 8601 timestamp."""

    created_before: str
    """Only memberships created before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """Number of results to return from the start of the range."""

    last: int
    """Number of results to return from the end of the range."""

    order: Literal["created_at"]
    """Sort field."""

    plan_id: str
    """Filter to memberships of this plan (`plan_` tag).

    Repeat as plan_ids[] for several.
    """

    product_id: str
    """Filter to memberships of this product (`prod_` tag).

    Repeat as product_ids[] for several.
    """

    status: Literal["active", "trialing", "past_due", "completed", "canceled", "expired", "canceling", "paused"]
    """Filter by billing state.

    `canceling` matches active memberships set to cancel at period end; `paused`
    matches memberships with payment collection paused.
    """

    user_id: str
    """Narrow to one user's memberships (`user_` tag, or `me` for the caller).

    A user outside the caller's visible set returns an empty list.
    """

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
