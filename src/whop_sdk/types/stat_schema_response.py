# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["StatSchemaResponse", "Grouping", "LineCategory", "ReportingCategory"]


class Grouping(BaseModel):
    line_categories: List[str]

    name: str


class LineCategory(BaseModel):
    description: str

    grouping: str

    key: str

    reporting_categories: List[str]


class ReportingCategory(BaseModel):
    line_categories: List[str]

    name: str


class StatSchemaResponse(BaseModel):
    groupings: List[Grouping]

    line_categories: List[LineCategory]

    reporting_categories: List[ReportingCategory]
