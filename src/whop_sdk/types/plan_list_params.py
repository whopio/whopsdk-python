# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["PlanListParams"]


class PlanListParams(TypedDict, total=False):
    account_id: str
    """The unique identifier of the account to list plans for.

    Required unless `product_ids` is provided for a public product-plan read.
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
    """Only return plans created after this timestamp."""

    created_before: str
    """Only return plans created before this timestamp."""

    direction: Literal["asc", "desc"]
    """The sort direction for results. Defaults to descending."""

    first: int
    """Number of results to return from the start of the range."""

    last: int
    """Number of results to return from the end of the range."""

    order: Literal["id", "active_members_count", "created_at", "internal_notes", "expiration_days"]
    """The field to sort results by. Defaults to created_at."""

    plan_types: SequenceNotStr[str]
    """Filter to only plans matching these billing types."""

    product_ids: SequenceNotStr[str]
    """Filter to only plans belonging to these product identifiers.

    When `account_id` is omitted, this is required and the response is publicly
    readable: only visible, non-invoice plans are returned.
    """

    release_methods: SequenceNotStr[str]
    """Filter to only plans matching these release methods."""

    visibilities: SequenceNotStr[str]
    """Filter to only plans matching these visibility states."""

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
