# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
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

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Start of the time range as an ISO 8601 timestamp.

    Required when person_id is omitted.
    """

    person_id: str
    """The ID of the person.

    Omit to list recent identity-linked events for the account.
    """

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of the time range as an ISO 8601 timestamp.

    Required when person_id is omitted; otherwise defaults to now.
    """
