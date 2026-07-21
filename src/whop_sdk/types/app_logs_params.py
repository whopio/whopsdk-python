# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AppLogsParams"]


class AppLogsParams(TypedDict, total=False):
    after: str
    """A cursor for fetching logs after a previous page."""

    app_build_id: str
    """Only return logs from this build."""

    before: str
    """A cursor for fetching logs before a later page."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start of the time window as an ISO 8601 timestamp.

    Defaults to 7 days before created_before.
    """

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of the time window as an ISO 8601 timestamp. Defaults to now."""

    first: int
    """The number of log lines to return (max 500)."""

    level: Literal["log", "debug", "info", "warn", "error"]
    """Only return console lines of this level."""

    query: str
    """Only return logs whose message contains this text (case-insensitive)."""
