# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .ad_group_status import AdGroupStatus
from .shared.direction import Direction

__all__ = ["AdGroupListParams"]


class AdGroupListParams(TypedDict, total=False):
    ad_campaign_id: Optional[str]
    """Filter by ad campaign. Provide exactly one of ad_campaign_id or company_id."""

    ad_campaign_ids: Optional[SequenceNotStr[str]]
    """Only return ad groups belonging to these ad campaigns (max 100).

    Can be combined with companyId or used on its own.
    """

    after: Optional[str]
    """Returns the elements in the list that come after the specified cursor."""

    before: Optional[str]
    """Returns the elements in the list that come before the specified cursor."""

    campaign_id: Optional[str]
    """Filter by campaign."""

    company_id: Optional[str]
    """Filter by company. Provide companyId or adCampaignIds."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return ad groups created after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return ad groups created before this timestamp."""

    direction: Optional[Direction]
    """The direction of the sort."""

    first: Optional[int]
    """Returns the first _n_ elements from the list."""

    last: Optional[int]
    """Returns the last _n_ elements from the list."""

    order: Optional[
        Literal[
            "created_at",
            "spend",
            "impressions",
            "clicks",
            "reach",
            "unique_clicks",
            "results",
            "click_through_rate",
            "cost_per_click",
            "cost_per_mille",
            "cost_per_result",
            "frequency",
            "return_on_ad_spend",
        ]
    ]
    """The fields the ads dashboard lists (campaigns, ad sets) can be ordered by.

    Stat columns are computed over the provided stats date range.
    """

    query: Optional[str]
    """Case-insensitive substring match against the ad group name or ID."""

    stats_from: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    Inclusive start of the window for each ad group's metric fields (spend,
    impressions, …). Omit both statsFrom and statsTo for all-time stats.
    """

    stats_to: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Inclusive end of the window for each ad group's metric fields.

    Omit both statsFrom and statsTo for all-time stats.
    """

    status: Optional[AdGroupStatus]
    """The status of an external ad group."""
