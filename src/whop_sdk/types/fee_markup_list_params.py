# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FeeMarkupListParams"]


class FeeMarkupListParams(TypedDict, total=False):
    company_id: Required[str]
    """The ID (tag) of the company you want to list the fee markups for.

    If you pass your platform account, you will get the platform default markups.
    """

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""
