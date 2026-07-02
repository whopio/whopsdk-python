# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PersonListParams"]


class PersonListParams(TypedDict, total=False):
    account_id: str
    """The ID of the account, which will look like biz\\__******\\********.

    Optional for account API keys; required for credentials that can access multiple
    accounts.
    """

    direction: Literal["asc", "desc"]
    """Sort direction. Defaults to desc."""

    filters: str
    """A JSON-encoded array of filters, each with field, operator, and value keys."""

    first: int
    """The number of people to return (default 100, max 101)."""

    from_: Annotated[int, PropertyInfo(alias="from")]
    """Start of the time range as a Unix timestamp. Defaults to 366 days before `to`."""

    offset: int
    """The number of people to skip, for offset pagination."""

    sort: str
    """Column to sort by (e.g.

    last_seen_at, ltv, purchase_count). Defaults to last_seen_at.
    """

    to: int
    """End of the time range as a Unix timestamp. Defaults to now."""
