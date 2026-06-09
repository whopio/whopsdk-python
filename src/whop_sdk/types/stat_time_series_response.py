# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["StatTimeSeriesResponse", "Data", "DataPoint", "DataPointSegment", "DataSummary"]


class DataPointSegment(BaseModel):
    name: str

    value: float


class DataPoint(BaseModel):
    segments: List[DataPointSegment]

    timestamp: int
    """Bucket start as a unix epoch (seconds)."""

    value: float
    """Headline value for the bucket."""


class DataSummary(BaseModel):
    max: float

    min: float

    avg: Optional[float] = None

    last: Optional[float] = None

    sum: Optional[float] = None


class Data(BaseModel):
    points: List[DataPoint]

    summary: DataSummary


class StatTimeSeriesResponse(BaseModel):
    data: Data

    metadata: object
