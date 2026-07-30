# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    after: str
    """A cursor; returns accounts after this position."""

    before: str
    """A cursor; returns accounts before this position."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Return only accounts created after this ISO 8601 timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Return only accounts created before this ISO 8601 timestamp."""

    direction: Literal["asc", "desc"]
    """Sort direction."""

    first: int
    """The number of accounts to return (default 10, max 50)."""

    last: int
    """The number of accounts to return from the end of the range."""

    order: Literal["created_at", "volume"]
    """The field to sort accounts by.

    `volume` requires `stats:read` on the parent account.
    """

    parent_account_id: str
    """For platforms: the parent account ID whose direct connected accounts to return.

    Requires `payout:account:read` on the parent account.
    """

    query: str
    """Free-text filter on account title or ID. `%` and `_` match literally."""

    status: Literal["active", "suspended"]
    """
    Return only accounts with this status: `active` (includes accounts that have not
    entered payments review) or `suspended`.
    """

    volume_max: float
    """Return only accounts whose lifetime USD volume is at most this value.

    Requires `stats:read` on the parent account.
    """

    volume_min: float
    """Return only accounts whose lifetime USD volume is at least this value.

    Requires `stats:read` on the parent account.
    """
