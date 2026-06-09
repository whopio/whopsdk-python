# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["StatTimeSeriesParams"]


class StatTimeSeriesParams(TypedDict, total=False):
    account_id: Required[str]
    """The account to read.

    Pass a `biz_` or `user_` tag; the caller must have `stats:read` on it.
    """

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Start of the window — a unix epoch (seconds) or an ISO 8601 date/datetime."""

    resource_type: Required[Literal["wallet"]]
    """The type of resource to query. Currently only `wallet` is supported."""

    to: Required[str]
    """End of the window — a unix epoch (seconds) or an ISO 8601 date/datetime."""

    access_pass_ids: SequenceNotStr[str]
    """Filter to specific access passes (products). Omit to include all products."""

    all_currencies: bool
    """Metric mode only.

    Convert all currencies to the display currency for currency metrics.
    """

    convert_currency: str
    """Raw mode. Convert all amounts to this currency using historical exchange rates."""

    currency: str
    """Filter to rows denominated in this currency."""

    group_by: Literal["day", "week", "month"]
    """Bucket granularity for raw mode."""

    grouping: SequenceNotStr[str]
    """Raw mode. Filter to specific groupings."""

    interval: Literal["hourly", "daily", "weekly", "monthly", "yearly"]
    """Bucket granularity for metric mode."""

    line_category: SequenceNotStr[str]
    """Raw mode. Filter to specific transaction types."""

    metric: Literal[
        "gross_revenue",
        "net_revenue",
        "net_volume",
        "refunds",
        "sales_tax",
        "processing_fees",
        "whop_fees",
        "dispute_fees",
        "affiliate_fees",
        "marketplace_fees",
        "marketplace_revenue",
        "ad_spend",
        "churned_revenue",
        "successful_payments",
        "new_users",
        "new_memberships",
        "page_visits",
        "disputes_count",
        "dispute_alerts_count",
        "mrr",
        "arr",
        "average_revenue_per_paying_user",
        "average_revenue_per_subscription",
        "users_growth",
        "paid_active_members",
        "churn_rate",
        "auth_rate",
        "trial_conversion_rate",
        "wallet_balance",
        "balance_activity",
        "gross_transaction_value",
        "wallet_balance_breakdown",
        "new_users_split",
        "revenue_split",
    ]
    """Return a single predefined metric (metric mode).

    When set, `reporting_category`/`grouping`/`line_category` are ignored and
    `interval` controls bucketing.
    """

    reporting_category: str
    """Raw mode. Filter to a predefined reporting category (see the schema endpoint)."""

    timezone: str
    """IANA timezone for period boundaries."""

    week_mode: int
    """ClickHouse week-numbering mode used when bucketing by week."""
