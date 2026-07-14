# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AudienceListParams"]


class AudienceListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID, prefixed `biz_`."""

    after: str
    """Cursor for the next page of audiences."""

    audience_id: str
    """Audience ID, prefixed `adaud_`, used to filter the response to one audience."""

    first: int
    """Number of audiences to return. Defaults to 20; maximum 100."""
