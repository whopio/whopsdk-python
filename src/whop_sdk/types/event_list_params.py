# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    person_id: Required[str]
    """The ID of the person."""

    account_id: str
    """The ID of the account, which will look like biz\\__******\\********.

    Optional for account API keys; required for credentials that can access multiple
    accounts.
    """

    after: str
    """A cursor for fetching events after a previous page."""

    before: str
    """A cursor for fetching events before a later page."""

    first: int
    """The number of events to return."""

    from_: Annotated[int, PropertyInfo(alias="from")]
    """Start of the time range as a Unix timestamp."""

    to: int
    """End of the time range as a Unix timestamp. Defaults to now."""
