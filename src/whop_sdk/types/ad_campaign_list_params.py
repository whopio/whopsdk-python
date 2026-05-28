# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .ad_campaign_status import AdCampaignStatus

__all__ = ["AdCampaignListParams"]


class AdCampaignListParams(TypedDict, total=False):
    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    company_id: Optional[str]
    """The unique identifier of the company to list ad campaigns for."""

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

    status: Optional[AdCampaignStatus]
    """The status of an ad campaign."""
