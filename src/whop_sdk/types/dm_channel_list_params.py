# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DmChannelListParams"]


class DmChannelListParams(TypedDict, total=False):
    after: str
    """Returns the elements in the list that come after the specified cursor."""

    before: str
    """Returns the elements in the list that come before the specified cursor."""

    company_id: str
    """The unique identifier of a company to filter DM channels by.

    Only returns channels scoped to this company.
    """

    first: int
    """Returns the first _n_ elements from the list."""

    last: int
    """Returns the last _n_ elements from the list."""
