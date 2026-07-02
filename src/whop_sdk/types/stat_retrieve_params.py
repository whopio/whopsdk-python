# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StatRetrieveParams"]


class StatRetrieveParams(TypedDict, total=False):
    from_: Required[Annotated[Union[str, date], PropertyInfo(alias="from", format="iso8601")]]
    """Start of the date range (YYYY-MM-DD)."""

    to: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """End of the date range (YYYY-MM-DD)."""

    account_id: str
    """The account this query concerns, for example biz_AbC123."""

    breakdown_by: str
    """
    Split the metric out by one of its properties — each point gets a breakdown
    array. For example breakdown_by=currency returns an entry for usd, an entry for
    eur, and so on.
    """

    card_network: str
    """Filter to a single card brand, for example visa.

    A refinement of payment_method=card. Available on metrics that list
    card_network.
    """

    convert_to: str
    """
    Display currency for money metrics — every amount is converted into this ISO
    currency using the exchange rate on each period's date. Defaults to usd. Ignored
    when you filter or break down by currency (those report the original transaction
    currency, unconverted).
    """

    currency: str
    """
    Filter to transactions made in this original ISO currency, for example eur —
    reported in that currency, not converted. Pair with breakdown_by=currency to
    split a metric by currency. Available on metrics that list currency.
    """

    interval: Literal["hour", "day", "week", "month"]
    """How wide each point is. Defaults to day. Snapshot metrics are day-only."""

    payment_method: str
    """Filter to a single payment method, for example card or crypto.

    Available on metrics that list payment_method.
    """

    snapshot_window: Literal["30d"]
    """Trailing window for snapshot metrics.

    Only accepted by snapshot metrics (each lists its allowed windows in the
    catalog); defaults to the metric's first supported window. Only 30d today.
    """

    time_zone: str
    """IANA time zone to bucket the series in, for example America/New_York.

    Defaults to UTC. Not accepted by snapshot metrics, which are UTC only.
    """
