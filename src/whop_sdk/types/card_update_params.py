# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CardUpdateParams"]


class CardUpdateParams(TypedDict, total=False):
    name: str

    spend_limit: str

    spend_limit_frequency: Literal["daily", "weekly", "monthly", "one_time"]

    transaction_limit: str
