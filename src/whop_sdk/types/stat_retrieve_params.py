# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
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

    ad_campaign_ids: SequenceNotStr[str]
    """
    Ad campaign ids (adcamp\\__...) to scope the report to; stats are summed across
    them. Available on metrics that list ad_campaign_ids.
    """

    ad_group_ids: SequenceNotStr[str]
    """Ad group ids (adgrp\\__...) to scope the report to; stats are summed across them.

    Available on metrics that list ad_group_ids.
    """

    ad_ids: SequenceNotStr[str]
    """Ad ids (ad\\__...) to scope the report to; stats are summed across them.

    Available on metrics that list ad_ids.
    """

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
    currency using the exchange rate on each period's date. Defaults to usd. For the
    ads metrics (ad_spend, ad_report), pass the account's ads reporting currency to
    match the ad entity endpoints. Ignored when you filter or break down by currency
    (those report the original transaction currency, unconverted).
    """

    currency: str
    """
    Filter to transactions made in this original ISO currency, for example eur —
    reported in that currency, not converted. Pair with breakdown_by=currency to
    split a metric by currency. Available on metrics that list currency.
    """

    dispute_reason: str
    """Filter disputes to a normalized reason, for example product_not_received.

    Pair with breakdown_by=dispute_reason to split dispute counts by reason.
    """

    fee_type: str
    """Filter to a single fee type.

    Pair with breakdown_by=fee_type to split fees by type. Available on metrics that
    list fee_type.
    """

    interval: Literal["five_minutes", "thirty_minutes", "hour", "day", "week", "month", "year"]
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

    referred_user_id: str
    """
    Filter a referral metric to the businesses attributed to one person you
    referred, for example user_AbC123. Available on metrics that list
    referred_user_id.
    """

    segment: str
    """Filter to a single wallet-balance segment, for example available.

    Pair with breakdown_by=segment to split the balance. Available on metrics that
    list segment.
    """

    snapshot_window: Literal["7d", "28d", "30d"]
    """Window used by a snapshot metric.

    Ordinary snapshots accept 30d as their trailing activity window. Cohorted
    dispute metrics accept 7d or 28d as the sales-transaction pool; their
    attribution window is fixed in the metric name. Each metric lists its accepted
    values in the catalog.
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
