# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PartnerLeaderboardParams"]


class PartnerLeaderboardParams(TypedDict, total=False):
    period: Literal["day", "month", "year", "last_30_days", "all_time"]
    """Time window for the rankings.

    `day`, `month`, and `year` count earnings since the start of the current
    calendar day, month, or year; `last_30_days` counts earnings over the trailing
    30 days; `all_time` ranks lifetime earnings.
    """
