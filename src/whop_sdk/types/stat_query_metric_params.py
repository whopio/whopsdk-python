# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["StatQueryMetricParams"]


class StatQueryMetricParams(TypedDict, total=False):
    resource: Required[str]
    """
    Metric resource using : as separator (e.g., 'receipts:gross_revenue',
    'members:new_users').
    """

    breakdowns: Optional[SequenceNotStr[str]]
    """Columns to break down the metric by."""

    company_id: Optional[str]
    """Scope query to a specific company."""

    filters: Optional[Dict[str, object]]
    """Key-value pairs to filter the data."""

    from_: Annotated[Union[str, datetime, None], PropertyInfo(alias="from", format="iso8601")]
    """Start of time range (unix timestamp)."""

    granularity: Optional[str]
    """Time granularity (daily, weekly, monthly)."""

    time_zone: Optional[str]
    """IANA timezone for period bucketing (e.g.

    'America/New_York'). Defaults to UTC. Only applies to ClickHouse metrics.
    """

    to: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """End of time range (unix timestamp)."""

    user_id: Optional[str]
    """Scope query to a specific user."""
