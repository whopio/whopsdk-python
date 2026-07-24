# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["StatRetrieveParams"]


class StatRetrieveParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """
    Start of the range — a date (YYYY-MM-DD), expanded to the start of that day, or
    an ISO 8601 timestamp (for example 2026-07-16T16:37:00Z), used exactly.
    """

    to: Required[str]
    """
    End of the range — a date (YYYY-MM-DD), expanded to the end of that day, or an
    ISO 8601 timestamp (for example 2026-07-17T16:37:00Z), used exactly.
    """

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
    ads metrics (ad_spend, ad_delivery), pass the account's ads reporting currency
    to match the ad entity endpoints. On transaction metrics, it is ignored when you
    filter or break down by currency (those report the original transaction
    currency, unconverted).
    """

    country_code: str
    """
    Filter traffic metrics to one visitor country (uppercase ISO 3166-1 alpha-2, for
    example US). Pair with breakdown_by=country_code to split by country.
    """

    currency: str
    """Select the source currency or asset on metrics that list currency.

    For transaction metrics, for example currency=eur, values are reported without
    conversion. For market_prices, use btc or xaut and convert_to=usd. Pair with
    breakdown_by=currency to split a metric by currency.
    """

    custom_name: str
    """Filter the events metric to one merchant-defined custom event name.

    Only valid alongside event_name=pixel.custom. Pair with breakdown_by=custom_name
    to split custom events by name.
    """

    device_type: str
    """Filter traffic metrics to one device type: desktop, mobile, tablet, or unknown.

    Pair with breakdown_by=device_type to split by device.
    """

    dispute_reason: str
    """Filter disputes to a normalized reason, for example product_not_received.

    Pair with breakdown_by=dispute_reason to split dispute counts by reason.
    """

    event_name: str
    """
    Filter the events metric to one tracked event name, for example pixel.page or
    pixel.custom. Pair with breakdown_by=event_name to split by event.
    """

    event_type: Literal["page_view", "checkout_start", "other"]
    """
    Filter the events metric to a canonical group of events: page_view (pixel page
    views plus whop.com store views), checkout_start (hosted and embedded checkout
    views), or other. Pair with breakdown_by=event_type to split by group.
    """

    fee_type: str
    """Filter to a single fee type.

    Pair with breakdown_by=fee_type to split fees by type. Available on metrics that
    list fee_type.
    """

    hostname: str
    """Filter traffic metrics to one website hostname, for example shop.example.com.

    Pair with breakdown_by=hostname to split by website.
    """

    interval: Literal["minute", "five_minutes", "thirty_minutes", "hour", "day", "week", "month", "year"]
    """How wide each point is. Defaults to day. Snapshot metrics are day-only."""

    merchant: str
    """Filter to a single cashback merchant bucket, for example whop-ads.

    Pair with breakdown_by=merchant to split cashback by merchant. Available on
    metrics that list merchant.
    """

    most_recent_action: str
    """Filter to a single most-recent member action.

    Pair with breakdown_by=most_recent_action. Available on metrics that list
    most_recent_action.
    """

    page: str
    """
    Filter traffic metrics to one page — a hostname plus normalized path, for
    example shop.example.com/pricing. Pair with breakdown_by=page to split by page.
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
    """
    Filter to a single GMV source, for example payments — or, on the traffic
    metrics, a visit source (whop_ads, direct, or a utm_source value). Pair with
    breakdown_by=source to split by source. Available on metrics that list source.
    """

    status: str
    """Filter to a single membership status.

    Pair with breakdown_by=status. Available on metrics that list status.
    """

    time_zone: str
    """IANA time zone to bucket the series in, for example America/New_York.

    Defaults to UTC. Not accepted by snapshot metrics, which are UTC only.
    """
