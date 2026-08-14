# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserMeParams"]


class UserMeParams(TypedDict, total=False):
    account_id: str
    """When set, returns your account-specific profile overrides for this account."""

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Balance-history window start, ISO 8601 date or datetime.

    Defaults to 30 days ago. Only used with `include_balance_history`.
    """

    include_balance_history: bool
    """Also compute your balance history (opt-in; runs a heavier query).

    Ignored for callers without balance-read scope.
    """

    interval: Literal["hour", "day", "week", "month"]
    """Balance-history point granularity.

    Defaults to `day`. Only used with `include_balance_history`.
    """

    time_zone: str
    """IANA time zone the balance-history points are bucketed in.

    Defaults to `UTC`. Only used with `include_balance_history`.
    """

    to: str
    """Balance-history window end, ISO 8601 date or datetime.

    Defaults to now. Only used with `include_balance_history`.
    """
