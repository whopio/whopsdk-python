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

    access_level: str
    """Filter to a single access level.

    Pair with breakdown_by=access_level. Available on metrics that list
    access_level.
    """

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

    category: str
    """Filter to a single balance-activity category, for example payments.

    Pair with breakdown_by=category to split the activity. Available on metrics that
    list category.
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

    fee_type: str
    """Filter to a single fee type.

    Pair with breakdown_by=fee_type to split fees by type. Available on metrics that
    list fee_type.
    """

    interval: Literal["hour", "day", "week", "month", "year"]
    """How wide each point is. Defaults to day. Snapshot metrics are day-only."""

    most_recent_action: str
    """Filter to a single most-recent member action.

    Pair with breakdown_by=most_recent_action. Available on metrics that list
    most_recent_action.
    """

    payment_method: str
    """Filter to a single payment method, for example card or crypto.

    Available on metrics that list payment_method.
    """

    product: str
    """Filter to a single product (access pass id), for example prod_AbC123.

    Pair with breakdown_by=product. Available on metrics that list product.
    """

    segment: str
    """Filter to a single wallet-balance segment, for example available.

    Pair with breakdown_by=segment to split the balance. Available on metrics that
    list segment.
    """

    snapshot_window: Literal["30d"]
    """Trailing window for snapshot metrics.

    Only accepted by snapshot metrics (each lists its allowed windows in the
    catalog); defaults to the metric's first supported window. Only 30d today.
    """

    source: str
    """Filter to a single GMV source, for example payments.

    Pair with breakdown_by=source to split by source. Available on metrics that list
    source.
    """

    status: str
    """Filter to a single membership status.

    Pair with breakdown_by=status. Available on metrics that list status.
    """

    time_zone: str
    """IANA time zone to bucket the series in, for example America/New_York.

    Defaults to UTC. Not accepted by snapshot metrics, which are UTC only.
    """
