# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["StatListResponse", "Data"]


class Data(BaseModel):
    description: str
    """A short description of what the metric measures."""

    key: str
    """The metric's key. Pass it to GET /stats/{metric} to query its values."""

    name: str
    """Human-readable display name for the metric."""

    properties: List[str]
    """
    The properties you can use with this metric — pass one as a filter
    (property=value) to narrow the series, or as breakdown_by=property to split it.
    """

    unit: Literal["count", "currency", "percent"]
    """
    How to read the metric's values: count is an integer, currency is a decimal
    amount, and percent is a number where 1.6 means 1.6%.
    """

    windows: Optional[List[str]] = None
    """
    Snapshot metrics only: the trailing windows you can pass as snapshot_window, for
    example 30d. Absent on live metrics, which use from/to instead.
    """


class StatListResponse(BaseModel):
    data: List[Data]
    """The available metrics."""
