# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .granularities import Granularities

__all__ = ["AdReportRetrieveParams"]


class AdReportRetrieveParams(TypedDict, total=False):
    from_: Required[Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]]
    """Inclusive start of the reporting window."""

    to: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Inclusive end of the reporting window."""

    ad_campaign_id: Optional[str]
    """The unique identifier of an ad campaign.

    Mutually exclusive with `companyId`, `adGroupId`, and `adId`.
    """

    ad_group_id: Optional[str]
    """The unique identifier of an ad group.

    Mutually exclusive with `companyId`, `adCampaignId`, and `adId`.
    """

    ad_id: Optional[str]
    """The unique identifier of an ad.

    Mutually exclusive with `companyId`, `adCampaignId`, and `adGroupId`.
    """

    breakdown: Optional[Literal["campaign", "ad_group", "ad"]]
    """Entity level to group an ad report by."""

    company_id: Optional[str]
    """The unique identifier of a company.

    Mutually exclusive with `adCampaignId`, `adGroupId`, and `adId`. Use with
    `breakdown` to fan out across every campaign, ad group, or ad in the company
    without paging.
    """

    currency: Optional[str]
    """ISO 4217 currency code to report `spend` in.

    Defaults to the company's ads reporting currency.
    """

    granularity: Optional[Granularities]
    """Bucket size for external ad stat rows."""
