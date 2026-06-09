# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CardDailySpendParams"]


class CardDailySpendParams(TypedDict, total=False):
    timezone: str
    """IANA timezone (e.g.

    America/New_York) the daily buckets are computed in. Defaults to UTC.
    """
