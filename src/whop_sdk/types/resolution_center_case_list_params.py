# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ResolutionCenterCaseListParams"]


class ResolutionCenterCaseListParams(TypedDict, total=False):
    account_id: str
    """Only cases filed against this account (`biz_` tag).

    With read access to the account this lists its whole queue; without, only the
    cases you opened against it.
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
    """Only cases created after this ISO 8601 timestamp."""

    created_before: str
    """Only cases created before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """Number of results to return from the start of the range."""

    last: int
    """Number of results to return from the end of the range."""

    order: Literal["created_at", "response_due_at"]
    """The field to sort cases by."""

    outcome: List[Literal["customer_won", "merchant_won", "withdrawn"]]
    """Only closed cases that ended these ways. Repeat the parameter to pass several."""

    reason: List[
        Literal[
            "fraudulent", "product_not_received", "not_as_described", "product_unacceptable", "subscription_canceled"
        ]
    ]
    """Only cases opened for these reasons. Repeat the parameter to pass several."""

    status: List[Literal["awaiting_merchant", "awaiting_customer", "under_review", "closed"]]
    """Only cases in these statuses.

    Repeat the parameter to pass several — one paginated list covers all of them.
    """

    user_id: str
    """Only cases opened by this customer — a `user_` tag, or `me` for the calling
    user.

    It narrows what you can already read, so `me` lists the cases you opened without
    the ones on accounts you are a team member of.
    """

    api_version_date: Annotated[str, PropertyInfo(alias="Api-Version-Date")]
