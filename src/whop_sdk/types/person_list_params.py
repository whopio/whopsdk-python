# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PersonListParams"]


class PersonListParams(TypedDict, total=False):
    account_id: str
    """The ID of the account, which will look like biz\\__******\\********.

    Optional for account API keys; required for credentials that can access multiple
    accounts.
    """

    after: str
    """A cursor for fetching people after a previous page."""

    before: str
    """A cursor for fetching people before a later page."""

    direction: Literal["asc", "desc"]
    """Sort direction. Defaults to desc."""

    filters: str
    """A JSON-encoded array of filters, each with field, operator, and value keys."""

    first: int
    """The number of people to return (default 100, max 100)."""

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Start of the time range as an ISO 8601 timestamp.

    Defaults to 366 days before `to`.
    """

    sort: str
    """Column to sort by (e.g.

    last_seen_at, ltv, purchase_count). Defaults to last_seen_at.
    """

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of the time range as an ISO 8601 timestamp. Defaults to now."""
