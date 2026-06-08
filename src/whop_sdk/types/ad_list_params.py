# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared.direction import Direction
from .external_ad_status import ExternalAdStatus

__all__ = ["AdListParams"]


class AdListParams(TypedDict, total=False):
    ad_campaign_id: Optional[str]
    """Filter by ad campaign.

    Provide exactly one of ad_group_id, ad_campaign_id, or company_id.
    """

    ad_campaign_ids: Optional[SequenceNotStr[str]]
    """Only return ads belonging to these ad campaigns (max 100).

    Can be combined with companyId or used on its own.
    """

    ad_group_id: Optional[str]
    """Filter by ad group.

    Provide exactly one of ad_group_id, ad_campaign_id, or company_id.
    """

    ad_group_ids: Optional[SequenceNotStr[str]]
    """Only return ads belonging to these ad groups (max 100).

    Can be combined with companyId or used on its own.
    """

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    campaign_id: Optional[str]
    """Filter by campaign."""

    company_id: Optional[str]
    """Filter by company.

    Provide exactly one of ad_group_id, ad_campaign_id, or company_id.
    """

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return ads created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return ads created before this timestamp."""

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    order: Optional[Literal["created_at", "spend", "return_on_ad_spend"]]
    """The fields ad resources can be ordered by."""

    order_by: Optional[Literal["spend", "return_on_ad_spend", "roas"]]
    """Columns that the listAds query can sort by. Deprecated — use AdOrder."""

    order_direction: Optional[Direction]
    """The direction of the sort."""

    query: Optional[str]
    """Case-insensitive substring match against the ad title or ID."""

    stats_from: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    Inclusive start of the window for each ad's metric fields (spend, impressions,
    …) and for stats-column sorting. Omit both statsFrom and statsTo for all-time
    stats.
    """

    stats_to: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    Inclusive end of the window for each ad's metric fields and for stats-column
    sorting. Omit both statsFrom and statsTo for all-time stats.
    """

    status: Optional[ExternalAdStatus]
    """The status of an external ad."""
