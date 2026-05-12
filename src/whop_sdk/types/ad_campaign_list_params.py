# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AdCampaignListParams"]


class AdCampaignListParams(TypedDict, total=False):
    company_id: Required[str]
    """The unique identifier of the company to list ad campaigns for."""

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return ad campaigns created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return ad campaigns created before this timestamp."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    query: Optional[str]
    """Case-insensitive substring match against the campaign title."""

    status: Optional[Literal["active", "paused", "payment_failed", "draft", "in_review", "flagged"]]
    """The status of an ad campaign."""
