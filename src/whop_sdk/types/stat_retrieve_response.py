# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["StatRetrieveResponse", "Data", "DataPoint", "DataPointBreakdown", "DataTotal"]


class DataPointBreakdown(BaseModel):
    name: str
    """The property value, for example usd or visa."""

    value: Optional[float] = None
    """The metric's value for this entry."""


class DataPoint(BaseModel):
    timestamp: int
    """Unix timestamp (seconds) of the period start."""

    value: Optional[float] = None
    """The metric's value for this period, in the metric's unit."""

    breakdown: Optional[List[DataPointBreakdown]] = None
    """Present only when broken down: one entry per property value in this period."""


class DataTotal(BaseModel):
    name: str
    """The property value the total is for."""

    value: Optional[float] = None
    """The metric's whole-window value for this entry."""


class Data(BaseModel):
    points: List[DataPoint]
    """One entry per period, oldest first."""

    currency: Optional[str] = None
    """ISO currency the values are denominated in.

    Present for currency-unit metrics: the convert_to currency, or usd.
    """

    totals: Optional[List[DataTotal]] = None
    """Whole-window aggregates, present when the metric computes them (e.g.

    conversions returns window count / unique-people / value per entry — uniques
    only exist at window level and cannot be summed from points).
    """


class StatRetrieveResponse(BaseModel):
    data: Data
