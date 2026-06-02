# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.direction import Direction
from .external_ad_status import ExternalAdStatus

__all__ = ["AdListParams"]


class AdListParams(TypedDict, total=False):
    ad_group_id: Optional[str]
    """Filter by ad group.

    Provide exactly one of ad_group_id, campaign_id, or company_id.
    """

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    campaign_id: Optional[str]
    """Filter by campaign.

    Provide exactly one of ad_group_id, campaign_id, or company_id.
    """

    company_id: Optional[str]
    """Filter by company.

    Provide exactly one of ad_group_id, campaign_id, or company_id.
    """

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return ads created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return ads created before this timestamp."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    include_paused: Optional[bool]
    """
    When false, excludes paused ads so pagination matches the dashboard's
    hide-paused toggle.
    """

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    order_by: Optional[Literal["spend", "roas"]]
    """Columns that the listAds query can sort by."""

    order_direction: Optional[Direction]
    """The direction of the sort."""

    query: Optional[str]
    """Case-insensitive substring match against the ad title or tag."""

    stats_from: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Start of the stats date range used when order_by is a stats column."""

    stats_to: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """End of the stats date range used when order_by is a stats column."""

    status: Optional[ExternalAdStatus]
    """The status of an external ad."""
