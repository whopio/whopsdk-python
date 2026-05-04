# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AdGroupListParams"]


class AdGroupListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    campaign_id: Optional[str]
    """Filter by campaign. Provide exactly one of campaign_id or company_id."""

    company_id: Optional[str]
    """Filter by company. Provide exactly one of campaign_id or company_id."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return ad groups created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return ad groups created before this timestamp."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    query: Optional[str]
    """Case-insensitive substring match against the ad group name."""

    status: Optional[Literal["active", "paused", "inactive", "in_review", "rejected", "flagged"]]
    """The status of an external ad group."""
