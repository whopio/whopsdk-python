# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BusinessLeaderboardParams"]


class BusinessLeaderboardParams(TypedDict, total=False):
    period: Literal["day", "month", "year", "all_time"]
    """Time window for the rankings.

    `day`, `month`, and `year` count earnings since the start of the current
    calendar day, month, or year; `all_time` ranks lifetime earnings.
    """
