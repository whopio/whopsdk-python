# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AudienceListParams"]


class AudienceListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID, prefixed `biz_`."""

    after: str
    """Cursor for the next page of audiences."""

    audience_id: str
    """Audience ID, prefixed `adaud_`, used to filter the response to one audience."""

    audience_type: Literal["custom", "lookalike"]
    """Filter by audience type: `custom` (uploaded lists) or `lookalike`."""

    first: int
    """Number of audiences to return. Defaults to 20; maximum 100."""

    source_type: Literal["csv_upload", "people_filter"]
    """
    Filter by member source: `csv_upload` (uploaded lists) or `people_filter`
    (automatic audiences built from saved People filters).
    """
